import discord
import asyncio
import datetime as dt
from .keep_alive import keep_alive
from discord.ext import tasks
from .data_storage import jeronimo_martins

data_container = jeronimo_martins()
client = discord.Client


class ShinshaBrain(client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.day_summary.start()
        keep_alive()
        
#funkcje poniżej obsługują wyświetlanie i czyszczenie statstyk serwera dokładnie o północy
    @tasks.loop(hours=24)
    async def day_summary(self):
       message_channel = self.get_channel(789853206053126147)
       message_channel.send(data_container.counter_status)
       data_container.clear_data()
       await message_channel.send("Nastał nowy dzień!")

    @day_summary.before_loop
    async def before_day_summary(self):
       for _ in range(60 * 60 * 24):  # loop the whole day
           if dt.datetime.now().strftime("%H:%M:%S") == dt.time(hour=0, minute=0, second=0).strftime("%H:%M:%S"):  # 24 hour format
              print('It is rewind time!')
              return
           await asyncio.sleep(1)  # wait a second before looping again. You can make it more

#funkcje poniżej obsługują reakcje bota na wiadomości
    async def on_message(self, message):
        if message.author == self.user:
            return

        data_container.message_counter(message.channel.name)

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('!message_count'):
            await message.channel.send(data_container.counter_status)

        if message.content.startswith('!commands'):
            _commands_dict = data_container.avaliable_commands
            _string = ''''''
            for key in _commands_dict:
              value = _commands_dict[key]
              _string = _string + f'{key} - {value}\n'
            await message.channel.send(_string)






        # if message.content.startswith('$counter_reset'):
        #     data_container.clear_data()
        #     await message.channel.send('Data cleared!')
