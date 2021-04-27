import asyncio
from .tao import TaoTeChing
from .data_storage import JeronimoMartins

data_container = JeronimoMartins()
message_timeout = 120

async def tao(message):
    taoteching = TaoTeChing()
    if message.channel.id == 805839570201608252:
        await message.channel.send(taoteching.random_quote())
    else:
        await message.delete()
        message = await message.channel.send(taoteching.random_quote())
        await asyncio.sleep(message_timeout)
        await message.delete()


async def counter_reset(message):
    data_container.clear_data()
    await message.channel.send('Data cleared!')