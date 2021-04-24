from __future__ import unicode_literals
import discord
import asyncio
import datetime as dt
import NyaaPy
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from discord.ext import tasks
from pybooru import Danbooru
from .data_storage import JeronimoMartins
from .tao import TaoTeChing

#
#  Witty comment here
#
data_container = JeronimoMartins()
message_timeout = 120

class ShinshaBrain(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.day_summary.start()
        self.autobackup.start()
        guild = self.get_guild(602620718433304604)
        text_channels = guild.text_channels
        data_container.recall_data(text_channels)
        # flags

    # data backup
    @tasks.loop(seconds=10)
    async def autobackup(self):
        data_container.store_data()
        self.GraphDataCollect(self.day_changed)

    # funkcje poniżej obsługują wyświetlanie i czyszczenie statstyk serwera dokładnie o północy
    @tasks.loop(hours=24)
    async def day_summary(self):
        guild = self.get_guild(602620718433304604)
        text_channels = guild.text_channels
        data_container.recall_data(text_channels)
        message_channel = self.get_channel(790949987609608212)
        await message_channel.send(data_container.counter_status)
        message = await message_channel.send("Nastał nowy dzień!")
        await self.GraphMessageHandler(message, True)
        await asyncio.sleep(1)
        data_container.clear_data()


    @day_summary.before_loop
    async def before_day_summary(self):
        for _ in range(60 * 60 * 24):  # loop the whole day
            if dt.datetime.now().strftime("%H:%M:%S") == dt.time(hour=0, minute=0, second=0).strftime(
                    "%H:%M:%S"):  # 24 hour format
                print('It is rewind time!')
                return
            await asyncio.sleep(1)  # wait a second before looping again. Can make it more

    # definicje metody wywołwywanych on message
    async def chop_long_string(self, string, message) -> list:
        if len(string) < 2000:
            message = await message.channel.send(string)
            _resulting_list = [message]
            return _resulting_list
        else:
            firstpart, secondpart = string[:len(string) // 2], string[len(string) // 2:]

            if len(firstpart) >= 2000:
                message = await message.channel.send('Shiver me timbers maytey! Be more specific')
                _resulting_list = [message]
                return _resulting_list
            else:
                message = await message.channel.send(firstpart)
                message1 = await message.channel.send(secondpart)
                _resulting_list = [message, message1]
                return _resulting_list

    def picture_generator(self, _tags):
        danbo_client = Danbooru('danbooru')
        while 1:
            picture = danbo_client.post_list(tags=_tags, limit=1, random=True)
            yield picture

    async def picture_filter(self, _tags, banned_tags, message, current_picture):
        _picture = self.picture_generator(_tags)
        x = 0
        check_counter = 0
        while x < len(banned_tags):
            current_picture_tags = current_picture[0]['tag_string'].split(' ')
            if banned_tags[x] in current_picture_tags:
                x = 0
                check_counter += 1
                current_picture = next(_picture)

            if banned_tags[x] not in current_picture_tags:
                x += 1
                
            if check_counter == 10:
                await message.channel.send("Po 10 próbach gejoza dalej obecna, zmień tagi ( ͡° ͜ʖ ͡°)")
                break
        else:
            return current_picture

    def rating_formatter(self, message):
        _tags = message.content[7:]
        if 'rating:' not in _tags:
            _tags = _tags + ' rating:safe'
            return _tags
        if 'rating:any' in _tags:
            _tags = _tags.replace('rating:any','')
            return _tags
        else:
            return _tags

    async def waiting_and_responding(self, _tags, banned_tags, message, picture):
        _i = 20
        while len(picture) == 0 and _i != 0:
            await asyncio.sleep(1)
            _i -= 1
        if len(picture) == 0:
            response = '¯\_(ツ)_/¯'
        else:
            response = await self.picture_filter(_tags, banned_tags, message, picture)
            try:
              response = response[0]['large_file_url']
            except:
              response = response[0]['file_url']
        return response

    async def hello(self, message):
        if message.channel.id == 805839570201608252:
            _user_name = message.author.mention
            await message.channel.send(f'Hello {_user_name}!')
        else:
            await message.delete()
            _user_name = message.author.mention
            message = await message.channel.send(f'Hello {_user_name}!')
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def message_count(self, message):
        if message.channel.id == 805839570201608252:
            await message.channel.send(data_container.counter_status)
        else:
            await message.delete()
            message = await message.channel.send(data_container.counter_status)
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def commands(self, message):
        if message.channel.id == 805839570201608252:
            _commands_dict = data_container.avaliable_commands
            _string = '''Lista komend:\n'''
            for key in _commands_dict:
                value = _commands_dict[key]
                _string = _string + f'{key} - {value}\n'
            await message.channel.send(_string)
        else:
            await message.delete()
            _commands_dict = data_container.avaliable_commands
            _string = '''Lista komend:\n'''
            for key in _commands_dict:
                value = _commands_dict[key]
                _string = _string + f'{key} - {value}\n'
            message = await message.channel.send(_string)
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def tao(self, message):
        _taoteching = TaoTeChing()
        if message.channel.id == 805839570201608252:
            await message.channel.send(_taoteching.random_quote())
        else:
            await message.delete()
            message = await message.channel.send(_taoteching.random_quote())
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def danbo(self, message):
        _tags = self.rating_formatter(message)
        if message.channel.id == 805839570201608252:
            picture = self.picture_generator(_tags)
            picture = next(picture)
            answer = await self.waiting_and_responding(_tags, data_container.banned_tags, message, picture)
            await message.channel.send(answer)
        else:
            await message.delete()
            picture = self.picture_generator(_tags)
            picture = next(picture)
            answer = await self.waiting_and_responding(_tags, data_container.banned_tags, message, picture)
            message = await message.channel.send(answer)
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def danbo_count(self, message):
        _tags = message.content[12:]
        danbo_client = Danbooru('danbooru')
        this_many_posts = danbo_client.count_posts(_tags)['counts']['posts']
        tags_list = _tags.split(' ')

        if message.channel.id == 805839570201608252:
            if not len(tags_list)>2:
                await message.channel.send(f'{this_many_posts} posts found for tag {_tags}, I will leave it here :3')
            else:
                await message.channel.send(f'{this_many_posts} posts found for tags {_tags}, I will leave it here :3')
        else:
            await message.delete()
            if not len(tags_list)>2:
                await message.channel.send(f'{this_many_posts} posts found for tag {_tags}, I will leave it here :3')
            else:
                await message.channel.send(f'{this_many_posts} posts found for tags {_tags}, I will leave it here :3')

    async def nyaar(self, message):
        _tags = message.content[5:]
        message_container = [message]
        _selected_animu = []
        if message.channel.id == 805839570201608252:
            Arr = NyaaPy.Nyaa
            _result = Arr.search(_tags)

            # ensuring that server will respond and catching situation when it does not
            _i = 20
            while len(_result) == 0 and _i != 0:
                await asyncio.sleep(1)
                _i -= 1
            if len(_result) == 0:
                message = await message.channel.send('¯\_(ツ)_/¯')
            else:
                for _dict in _result:
                    if _dict['category'] == 'Anime - English-translated':
                        _selected_animu.append(_dict)
                    else:
                        continue

            # formatting string to send as a message
            string = ""
            for _dict in _selected_animu:
                string = string + f"{_dict['name']}\n{_dict['url']} S: {_dict['seeders']} L: {_dict['leechers']} Size: {_dict['size']}\n\n"

            await self.chop_long_string(string, message)
        else:
            await message.delete()
            Arr = NyaaPy.Nyaa
            _result = Arr.search(_tags)
            # ensuring that server will respond and catching situation when it does not
            _i = 20
            while len(_result) == 0 and _i != 0:
                await asyncio.sleep(1)
                _i -= 1
            if len(_result) == 0:
                message = await message.channel.send('¯\_(ツ)_/¯')
            else:
                _selected_animu = []
                for _dict in _result:
                    if _dict['category'] == 'Anime - English-translated':
                        _selected_animu.append(_dict)
                    else:
                        continue

                # formatting string to send as a message
                string = ""
                for _dict in _selected_animu:
                    string = string + f"{_dict['name']}\n{_dict['url']} S: {_dict['seeders']} L: {_dict['leechers']} Size: {_dict['size']}\n\n"

                message_container = await self.chop_long_string(string, message)

        await asyncio.sleep(message_timeout)
        for message in message_container:
            await message.delete()

    async def counter_reset(self, message):
        data_container.clear_data()
        await message.channel.send('Data cleared!')

    def GraphDataCollect(self, day_changed):
        day = dt.datetime.today().weekday()
        wdv = data_container.recall_week_data_vector()

        for ID in data_container.channels_info:
            if ID not in wdv:
                wdv[ID] = [0, 0, 0, 0, 0, 0, 0]
            elif day_changed:
                day = day-1
                if day == -1:
                    day = 6
                wdv[ID][day] = data_container.channels_info[ID].messages_count
            else:
                wdv[ID] = [data_container.channels_info[ID].messages_count if x == day else wdv[ID][x] for x in
                           range(0, 7)]
        data_container.store_week_data_vector(wdv)

    async def GraphMaker(self, message, day_changed):
        self.GraphDataCollect(day_changed)
        dni_tygodnia = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
        wdv = data_container.recall_week_data_vector()
        markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x',
                   'X', 'D', 'd', '|', '_']

        plt.style.use('dark_background')
        plt.figure(figsize=(10, 5), dpi=300)

        evenly_spaced_interval = np.linspace(0, 1, len(data_container.channels_info))
        colors = [cm.get_cmap('tab20')(x) for x in evenly_spaced_interval]


        i = 0
        for ID in data_container.channels_info:
            plt.plot(dni_tygodnia, wdv[ID], label=data_container.channels_info[ID].name, marker=markers[i],
                     markerfacecolor='none', markersize=8, color=colors[i])
            i += 1

        plt.grid()
        plt.legend(title='Kanały:')
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.title('Aktywność kanałów')
        plt.xlabel('Dni tygodnia')
        plt.ylabel('Liczba wiadomości')
        plt.gca().get_xticklabels()[dt.datetime.today().weekday()].set_color('red')
        plt.savefig('channelactivity.png', bbox_inches='tight', orientation='landscape', pad_inches=0.2)
        file = discord.File("channelactivity.png", filename="channelactivity.png")
        message = await message.channel.send("Requested graph", file=file)
        plt.clf()
        plt.close()
        os.remove("channelactivity.png")
        return message

    async def GraphMessageHandler(self, message, day_changed=False):
        if message.channel.id == 805839570201608252 or 790949987609608212:
            await self.GraphMaker(message, day_changed)
        else:
            await message.delete()
            message = await self.GraphMaker(message, day_changed)
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def CustomMentionsRegister(self, message):
        keywords = message.content.split()[1:]
        user_id = message.author.id
        _user_name = message.author.mention

        if user_id not in data_container.UserCustomMentions:
            data_container.UserCustomMentions[user_id] = []
        for word in keywords:
            if word not in data_container.UserCustomMentions[user_id]:
                data_container.UserCustomMentions[user_id].append(word)

        await message.channel.send(f'Dodano następujące wzmianki {keywords} dla {_user_name}')
        keywords.clear()

    async def CustomMentionsDelete(self, message):
        keywords = message.content.split()[1:]
        _user_id = message.author.id
        _user_name = message.author.mention

        if _user_id not in data_container.UserCustomMentions:
            await message.channel.send(f'Nie zarejestrowałeś jeszcze ani jednego highlighta {_user_name} :<')
        for word in keywords:
            if word in data_container.UserCustomMentions[_user_id]:
                data_container.UserCustomMentions[_user_id].remove(word)
        await message.channel.send(
            f'Zapisane wzmianki dla użytkownika {_user_name}:\n{data_container.UserCustomMentions[_user_id]}')

    async def CustomMentionsCheck(self, message):
        _user_name = message.author.mention
        _user_id = message.author.id
        if _user_id not in data_container.UserCustomMentions:
            await message.channel.send(f'Brak zarejestrowanych wzmianek {_user_name}')
            return
        await message.channel.send(f'Zapisane wzmianki dla użytkownika {_user_name}:\n{data_container.UserCustomMentions[_user_id]}')

    async def CheckForMentions(self, message):
        message_content = message.content.split()
        temporary_string = ''
        for ID in data_container.UserCustomMentions:
            for word in message_content:
                if word in data_container.UserCustomMentions[ID]:
                    temporary_string += f' <@{ID}>'
                    break
        try:
            await message.channel.send(temporary_string)
        except discord.errors.HTTPException:
            pass
        return


    # funkcje poniżej obsługują reakcje bota na wiadomości
    async def on_message(self, message):
        _cases = {
            '!hello': self.hello,
            '!message_count': self.message_count,
            '!help': self.commands,
            '!tao': self.tao,
            '!danbo': self.danbo,
            '!danbo_count': self.danbo_count,
            '!arr': self.nyaar,
            '!counter_reset': self.counter_reset,
            '!w_graph': self.GraphMessageHandler,
            '!register_mentions': self.CustomMentionsRegister,
            '!my_mentions': self.CustomMentionsCheck,
            '!delete_mentions': self.CustomMentionsDelete
        }

        with open("ArchiLogs2.txt", "a") as logfile:
            logfile.write(f"[{dt.datetime.now()}] on_message event triggered by {message.author}\n Posting on {message.channel.name}.\nCurrent counters: {data_container.counter_status_single_string}\n")

        await self.CheckForMentions(message)

        if message.author == self.user:
            return
        elif message.content.split(' ')[0][:1] == '!':
            command = message.content.split(' ')[0]
            try:
                await _cases[command](message)
            except KeyError as e:
                await message.channel.send('Nieznana komenda :<')
                print(e)
                return
            except Exception as e:
                await message.channel.send('Cosik nie bangala User-kun TT_TT')
                print(e)
                return
        else:
            data_container.message_counter(message.channel.id)

