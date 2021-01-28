import discord
from .data_storage import jeronimo_martins
from datetime import datetime, timedelta
import asyncio

data_container = jeronimo_martins()
client = discord.Client

def timer():
    now = datetime.now()
    seconds_till_midnight = (timedelta(hours=24) - (now - now.replace(hour=0, minute=0, second=0, microsecond=0))).total_seconds() % (24 * 3600)


class AsyncTask:
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    async def cancel(self):
        self._task.cancel()



class ShinshaBrain(client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_message(self, message):
        if message.author == self.user:
            return

        data_container.message_counter(message.channel.name)

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('$message_count'):
            await message.channel.send(data_container.counter_status)

    async def testTimerCorrectness(self):
        channel = client.get_channel(789853206053126147)
        await channel.send('Timer Dziala')





        # if message.content.startswith('$counter_reset'):
        #     data_container.clear_data()
        #     await message.channel.send('Data cleared!')
