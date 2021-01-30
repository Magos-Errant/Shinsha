import discord
from .data_storage import jeronimo_martins
import datetime as dt
from discord.ext import tasks
import asyncio

data_container = jeronimo_martins()
client = discord.Client


class ShinshaBrain(client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.day_summary.start()

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


    async def on_message(self, message):
        if message.author == self.user:
            return

        data_container.message_counter(message.channel.name)

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('!message_count'):
            await message.channel.send(data_container.counter_status)






        # if message.content.startswith('$counter_reset'):
        #     data_container.clear_data()
        #     await message.channel.send('Data cleared!')
