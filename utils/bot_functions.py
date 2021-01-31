import discord
import asyncio
import datetime as dt
from .keep_alive import keep_alive
from discord.ext import tasks
from __future__ import unicode_literals
from pybooru import Danbooru
from .data_storage import jeronimo_martins
from .tao import TaoTeChing

data_container = jeronimo_martins()
client = discord.Client
message_timeout = 120


class ShinshaBrain(client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.day_summary.start()
        keep_alive()

    # funkcje poniżej obsługują wyświetlanie i czyszczenie statstyk serwera dokładnie o północy
    @tasks.loop(hours=24)
    async def day_summary(self):
        message_channel = self.get_channel(602620718441693303)
        message_channel.send(data_container.counter_status)
        data_container.clear_data()
        await message_channel.send("Nastał nowy dzień!")

    @day_summary.before_loop
    async def before_day_summary(self):
        for _ in range(60 * 60 * 24):  # loop the whole day
            if dt.datetime.now().strftime("%H:%M:%S") == dt.time(hour=0, minute=0, second=0).strftime(
                    "%H:%M:%S"):  # 24 hour format
                print('It is rewind time!')
                return
            await asyncio.sleep(1)  # wait a second before looping again. You can make it more

    # funkcje poniżej obsługują reakcje bota na wiadomości
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.delete()
            message = await message.channel.send('Hello!')
            await asyncio.sleep(message_timeout)
            await message.delete()

        elif message.content.startswith('!message_count'):
            await message.delete()
            message = await message.channel.send(data_container.counter_status)
            await asyncio.sleep(message_timeout)
            await message.delete()

        elif message.content.startswith('!commands'):
            await message.delete()
            _commands_dict = data_container.avaliable_commands
            _string = '''Lista komend:\n'''
            for key in _commands_dict:
                value = _commands_dict[key]
                _string = _string + f'{key} - {value}\n'
            message = await message.channel.send(_string)
            await asyncio.sleep(message_timeout)
            await message.delete()

        elif message.content.startswith('!tao'):
            await message.delete()
            _taoteching = TaoTeChing()
            message = await message.channel.send(_taoteching.random_quote())
            await asyncio.sleep(message_timeout)
            await message.delete()

        elif message.content.startswith('!danbo'):
            _tags = message.content[8:]
            await asyncio.sleep(message_timeout)
            await message.delete()
            danbo_client = Danbooru('danbooru')
            posts = danbo_client.post_list(tags=f'{_tags}', limit=100)
            random_pool = {}
            i = 0
            for post in posts:
                random_pool[i] = post['file_url']
                i += 1

            message = await message.channel.send(random_pool[int(TaoTeChing.random.randint(0, 99))])
            await asyncio.sleep(message_timeout)
            await message.delete()

        else:
            data_container.message_counter(message.channel.name)

        # if message.content.startswith('$counter_reset'):
        #     data_container.clear_data()
        #     await message.channel.send('Data cleared!')
