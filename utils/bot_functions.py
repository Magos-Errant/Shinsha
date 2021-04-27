from __future__ import unicode_literals
import asyncio
import urllib3
import datetime as dt
from discord.ext import tasks
#imports from internal files:
from .DanbooruFunctionality import danbo, danbo_count
from .CustomMentionsFunctionality import *
from .GraphFunctionality import GraphDataCollect, GraphMessageHandler
from .NyaaTorrentFunctionality import nyaar
from .MiscFunctionality import *
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
        GraphDataCollect(day_changed=False)

    # funkcje poniżej obsługują wyświetlanie i czyszczenie statstyk serwera dokładnie o północy
    @tasks.loop(hours=24)
    async def day_summary(self):
        guild = self.get_guild(602620718433304604)
        text_channels = guild.text_channels
        data_container.recall_data(text_channels)
        message_channel = self.get_channel(790949987609608212)
        await message_channel.send(data_container.counter_status)
        message = await message_channel.send("Nastał nowy dzień!")
        await GraphMessageHandler(message, True)
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


    # Functions below describe bot reactions to commands
    async def on_message(self, message):
        _cases = {
            '!hello': self.hello,
            '!message_count': self.message_count,
            '!help': self.commands,
            '!tao': tao,
            '!danbo': danbo,
            '!danbo_count': danbo_count,
            '!arr': nyaar,
            '!counter_reset': counter_reset,
            '!w_graph': GraphMessageHandler,
            '!register_mentions': CustomMentionsRegister,
            '!my_mentions': CustomMentionsCheck,
            '!delete_mentions': CustomMentionsDelete
        }

        #Logging
        with open("ArchiLogs2.txt", "a") as logfile:
            logfile.write(f"[{dt.datetime.now()}] on_message event triggered by {message.author}\n Posting on {message.channel.name}.\nCurrent counters: {data_container.counter_status_single_string}\n")

        #Mention check
        await CheckForMentions(message)

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
            except urllib3.exceptions.HTTPError:
                return
            except Exception as e:
                await message.channel.send('Cosik nie bangala User-kun TT_TT')
                print(e)
                return

        else:
            #counting message
            data_container.message_counter(message.channel.id)

