from __future__ import unicode_literals
import datetime as dt
import discord
from discord.ext import tasks
from .CustomMentionsFunctionality import CustomMentionsRegister, CustomMentionsDelete, CustomMentionsCheck, CheckForMentions
from .DanbooruFunctionality import danbo, danbo_count
from .GraphFunctionality import GraphDataCollect, GraphMessageHandler
from .MiscFunctionality import *
from .NyaaTorrentFunctionality import nyaar
from .HumorousRandomResponsesFunctionality import *
from .Parameters import *
from .IChingFunctionality import send_reading_file
from .StrategemsFunctionality import strategems
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import  discord.ext.commands as commands
from main import client
#
#  Witty comment here
#


class ShinshaBrain(client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.day_summary.start()
        self.autobackup.start()
        guild = self.get_guild(skype_guild)
        text_channels = guild.text_channels
        data_container.recall_data(text_channels)
        # flags

    # data backup
    @tasks.loop(seconds=10)
    async def autobackup(self):
        data_container.store_data()
        GraphDataCollect(day_changed=False)

    # check for channel name change and update bot memory accordingly
    async def on_guild_channel_update(self, before, after):
        changed_channel_name = after.name
        changed_channel_ID = after.id
        data_container.channels_info[changed_channel_ID].name = changed_channel_name


    # funkcje poniżej obsługują wyświetlanie i czyszczenie statstyk serwera dokładnie o północy
    @tasks.loop(hours=24)
    async def day_summary(self):
        guild = self.get_guild(skype_guild)
        text_channels = guild.text_channels
        data_container.recall_data(text_channels)
        message_channel = self.get_channel(kucowanie_channel)
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
        if message.channel.id == bot_channel or message.guild:
            _user_name = message.author.mention
            await message.channel.send(f'Hello {_user_name}!')
        else:
            await message.delete()
            _user_name = message.author.mention
            message = await message.channel.send(f'Hello {_user_name}!')
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def message_count(self, message):
        if message.channel.id == bot_channel or message.guild:
            await message.channel.send(data_container.counter_status)
        else:
            await message.delete()
            message = await message.channel.send(data_container.counter_status)
            await asyncio.sleep(message_timeout)
            await message.delete()

    async def command_cases(self, case_group):
        if case_group == 'cases':
            cases = {
                '!hello': self.hello,
                '!message_count': self.message_count,
                '!help': self.commands,
                '!tao': tao,
                '!iching': send_reading_file,
                '!strategem': strategems,
                '!danbo': danbo,
                '!danbo_count': danbo_count,
                '!arr': nyaar,
                '!counter_reset': counter_reset,
                '!graph': GraphMessageHandler,
                '!add_mentions': CustomMentionsRegister,
                '!my_mentions': CustomMentionsCheck,
                '!delete_mentions': CustomMentionsDelete,
                '!add_humour': HumourRegister,
                '!humour_now': SendHumour
            }
            return cases

        elif case_group == 'mod_cases':
            mod_cases = {
                '!hello': self.hello,
                '!message_count': self.message_count,
                '!help': self.commands,
                '!tao': tao,
                '!iching': send_reading_file,
                '!danbo': danbo,
                '!danbo_count': danbo_count,
                '!arr': nyaar,
                '!counter_reset': counter_reset,
                '!graph': GraphMessageHandler,
                '!add_mentions': CustomMentionsRegister,
                '!my_mentions': CustomMentionsCheck,
                '!delete_mentions': CustomMentionsDelete,
                '!add_humour': HumourRegister,
                '!humour_now': SendHumour,
                '!show_humour': SendAllHumour,
                '!delete_humour': DeleteHumour
            }
            return mod_cases


    async def commands(self, message):
        if message.channel.id == bot_channel or message.guild:
            if not message.guild:
                _commands_dict = data_container.avaliable_mod_commands()
            else:
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

    async def command_detection(self, message, cases='cases'):
        cases = await self.command_cases(cases)
        command = message.content.split(' ')[0]
        if command == '!strategem':
            await cases['!strategem'](self, message)
        try:
            await cases[command](message)
        except KeyError as e:
            await message.channel.send('Nieznana komenda :<')
            print(e)
            return
        # except Exception as e:
        #     await message.channel.send('Cosik nie bangala User-kun TT_TT')
        #     await message.channel.send(f'{e}')
        #     print(e)
        #     return

    async def mod_command_detection(self, message):
        await self.command_detection(message, cases='mod_cases')



        # Functions below describe bot reactions to commands
    async def on_message(self, message):

        #Logging - enable if necessary
        # with open("ArchiLogs2.txt", "a") as logfile:
        #     logfile.write(f"[{dt.datetime.now()}] on_message event triggered by {message.author}\n Posting on {message.channel.name}.\nCurrent counters: {data_container.counter_status_single_string}\n")

        if message.author == self.user:
            return
        if not message.guild:
            moderators_id = []
            for moderator in moderators:
                moderators_id.append(moderators[moderator])
            if message.author.id in moderators_id:
                await self.mod_command_detection(message)
            else:
                await message.channel.send('Nie jesteś moderatorem')


        elif message.content.split(' ')[0][:1] == '!':
            await self.command_detection(message)
        else:
            # Mention check
            await CheckForMentions(message)
            #counting message
            data_container.message_counter(message.channel.id)
            # Humour
            await RandomHumour(message)

