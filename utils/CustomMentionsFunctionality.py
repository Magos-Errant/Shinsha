import discord
import re
from .Parameters import *


async def CustomMentionsRegister(message):
    keywords = message.content.split()[1:]
    user_id = message.author.id
    _user_name = message.author.mention

    if user_id not in data_container.UserCustomMentions:
        data_container.UserCustomMentions[user_id] = set()
    if len(data_container.UserCustomMentions[user_id]) > mention_limit or len(keywords) > mention_limit:
        await message.channel.send(f'Przekroczono limit wzmianek {_user_name}')
        return
    for word in keywords:
        if word not in data_container.UserCustomMentions[user_id]:
            data_container.UserCustomMentions[user_id].add(word.lower())

    await message.channel.send(f'Dodano następujące wzmianki {keywords} dla {_user_name}')
    keywords.clear()


async def CustomMentionsDelete(message):
    keywords = message.content.split()[1:]
    _user_id = message.author.id
    _user_name = message.author.mention

    if _user_id not in data_container.UserCustomMentions:
        await message.channel.send(f'Nie zarejestrowałeś jeszcze ani jednego highlighta {_user_name} :<')
    for word in keywords:
        if word.lower() in data_container.UserCustomMentions[_user_id]:
            data_container.UserCustomMentions[_user_id].discard(word.lower())
        if len(data_container.UserCustomMentions[_user_id]) == 0:
            await message.channel.send(f'Brak zarejestrowanych wzmianek {_user_name}')
        else:
            await message.channel.send(f'Zapisane wzmianki dla użytkownika {_user_name}:\n{data_container.UserCustomMentions[_user_id]}')


async def CustomMentionsCheck(message):
    _user_name = message.author.mention
    _user_id = message.author.id
    if _user_id not in data_container.UserCustomMentions:
        await message.channel.send(f'Brak zarejestrowanych wzmianek {_user_name}')
        return
    elif len(data_container.UserCustomMentions[_user_id]) == 0:
        await message.channel.send(f'Brak zarejestrowanych wzmianek {_user_name}')
    else:
        await message.channel.send(f'Zapisane wzmianki dla użytkownika {_user_name}:\n{data_container.UserCustomMentions[_user_id]}')


async def CheckForMentions(message):
    message_content = message.content.split()
    regex = re.compile('[^a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]')
    filtered_message_content = [regex.sub('', element) for element in message_content]
    temporary_string = ''
    _user_id = message.author.id
    for ID in data_container.UserCustomMentions:
        if ID == _user_id:
            continue
        for word in filtered_message_content:
            if word.lower() in data_container.UserCustomMentions[ID]:
                temporary_string += f' <@{ID}>'
                break
    try:
        await message.channel.send(temporary_string)
    except discord.errors.HTTPException:
        pass
    return
