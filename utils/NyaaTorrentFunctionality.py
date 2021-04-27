import asyncio
import NyaaPy

# parameters
message_timeout = 120


async def nyaar(message):
    _tags = message.content[5:]
    message_container = [message]
    _selected_animu = []
    if message.channel.id == 805839570201608252:
        Arr = NyaaPy.Nyaa
        _result = Arr.search(_tags)

        # ensuring that server will respond and catching situation when it does not
        _i = 20
        while len(_result) == 0 and _i != 0:
            await asyncio.sleep(1)
            _i -= 1
        if len(_result) == 0:
            message = await message.channel.send('¯\_(ツ)_/¯')
        else:
            for _dict in _result:
                if _dict['category'] == 'Anime - English-translated':
                    _selected_animu.append(_dict)
                else:
                    continue
    # formatting string to send as a message
    string = ""
    for _dict in _selected_animu:
        string = string + f"{_dict['name']}\n{_dict['url']} S: {_dict['seeders']} L: {_dict['leechers']} Size: {_dict['size']}\n\n"
        await chop_long_string(string, message)
    else:
        await message.delete()
        Arr = NyaaPy.Nyaa
        _result = Arr.search(_tags)
        # ensuring that server will respond and catching situation when it does not
        _i = 20
        while len(_result) == 0 and _i != 0:
            await asyncio.sleep(1)
            _i -= 1
        if len(_result) == 0:
            message = await message.channel.send('¯\_(ツ)_/¯')
        else:
            _selected_animu = []
            for _dict in _result:
                if _dict['category'] == 'Anime - English-translated':
                    _selected_animu.append(_dict)
                else:
                    continue

        # formatting string to send as a message
        string = ""
        for _dict in _selected_animu:
            string = string + f"{_dict['name']}\n{_dict['url']} S: {_dict['seeders']} L: {_dict['leechers']} Size: {_dict['size']}\n\n"

            message_container = await chop_long_string(string, message)
    await asyncio.sleep(message_timeout)
    for message in message_container:
        await message.delete()


async def chop_long_string(string, message):
    if len(string) < 2000:
        message = await message.channel.send(string)
        _resulting_list = [message]
        return _resulting_list
    else:
        firstpart, secondpart = string[:len(string) // 2], string[len(string) // 2:]
        if len(firstpart) >= 2000:
            message = await message.channel.send('Shiver me timbers maytey! Be more specific')
            _resulting_list = [message]
            return _resulting_list
        else:
            message = await message.channel.send(firstpart)
            message1 = await message.channel.send(secondpart)
            _resulting_list = [message, message1]
            return _resulting_list
