import random
from .Parameters import *
from .IDnames import yagoo_channel

async def HumourRegister(message):
    sentence = message.content.split(' ', 1)[1]+'\n'
    if len(sentence) > humour_lenght:
        await message.channel.send(f'Trochę za długie, limit znaków: {humour_lenght}')
        return
    if sentence not in data_container.humour:
        data_container.humour.append(sentence)
    else:
        await message.channel.send('Znam już tego śmieszka ( ͡° ͜ʖ ͡°)')
    data_container.store_data()

async def RandomHumour(message):
    if message.channel.id != yagoo_channel:
        if random.randint(1,100) <= humour_probability:
            SendHumour(message)

async def SendHumour(message):
    await message.channel.send(data_container.humour[random.randint(0,len(data_container.humour))])

async def SendAllHumour(message):
    humour_lines = [line.strip() for line in data_container.humour]
    await message.channel.send(f'{humour_lines}')

async def DeleteHumour(message):
    try:
        sentence = message.content.split(' ', 1)[1]+'\n'
        data_container.humour.remove(sentence)
        data_container.store_data()
        await message.channel.send(f'Deleted "{sentence}" sucesfully')
    except Exception as e:
        await message.channel.send(f'Something went wrong: {e}')
