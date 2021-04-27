import asyncio
from .tao import TaoTeChing
from .IDnames import *
from .bot_functions import message_timeout, data_container

async def tao(message):
    taoteching = TaoTeChing()
    if message.channel.id == bot_channel:
        await message.channel.send(taoteching.random_quote())
    else:
        await message.delete()
        message = await message.channel.send(taoteching.random_quote())
        await asyncio.sleep(message_timeout)
        await message.delete()


async def counter_reset(message):
    data_container.clear_data()
    await message.channel.send('Data cleared!')