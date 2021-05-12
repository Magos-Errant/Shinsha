import random
from .Parameters import *

async def HumourRegister(message):
    sentence = message.content.split(' ', 1)[1]
    if len(sentence) > humour_lenght:
        await message.channel.send(f'Trochę za długie, limit znaków: {humour_lenght}')
        return
    if sentence not in data_container.humour:
        data_container.humour.append(sentence)
    else:
        await message.channel.send('Znam już tego śmieszka ( ͡° ͜ʖ ͡°)')
    data_container.store_data()

async def RandomHumour(message):
    if random.randint(1,100) <= humour_probability:
        await message.channel.send(data_container.humour[random.randint(0,len(data_container.humour))])