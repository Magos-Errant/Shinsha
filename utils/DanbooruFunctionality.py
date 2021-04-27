import asyncio
from .data_storage import JeronimoMartins
from pybooru import Danbooru


data_container = JeronimoMartins()
message_timeout = 120

#Main functions

async def danbo(message):
    _tags = rating_formatter(message)
    if message.channel.id == 805839570201608252:
        picture = picture_generator(_tags)
        picture = next(picture)
        answer = await waiting_and_responding(_tags, data_container.banned_tags, message, picture)
        await message.channel.send(answer)
    else:
        await message.delete()
        picture = picture_generator(_tags)
        picture = next(picture)
        answer = await waiting_and_responding(_tags, data_container.banned_tags, message, picture)
        message = await message.channel.send(answer)
        await asyncio.sleep(message_timeout)
        await message.delete()


async def danbo_count(message):
    _tags = message.content[12:]
    danbo_client = Danbooru('danbooru')
    this_many_posts = danbo_client.count_posts(_tags)['counts']['posts']
    tags_list = _tags.split(' ')

    if message.channel.id == 805839570201608252:
        if not len(tags_list) > 2:
            await message.channel.send(f'{this_many_posts} posts found for tag {_tags}, I will leave it here :3')
        else:
            await message.channel.send(f'{this_many_posts} posts found for tags {_tags}, I will leave it here :3')
    else:
        await message.delete()
        if not len(tags_list) > 2:
            await message.channel.send(f'{this_many_posts} posts found for tag {_tags}, I will leave it here :3')
        else:
            await message.channel.send(f'{this_many_posts} posts found for tags {_tags}, I will leave it here :3')

#Functions used by main functions
def picture_generator(_tags):
    danbo_client = Danbooru('danbooru')
    while 1:
        picture = danbo_client.post_list(tags=_tags, limit=1, random=True)
        yield picture


async def picture_filter(_tags, banned_tags, message, current_picture):
    _picture = picture_generator(_tags)
    x = 0
    check_counter = 0
    while x < len(banned_tags):
        current_picture_tags = current_picture[0]['tag_string'].split(' ')
        if banned_tags[x] in current_picture_tags:
            x = 0
            check_counter += 1
            current_picture = next(_picture)

        if banned_tags[x] not in current_picture_tags:
            x += 1

        if check_counter == 10:
            await message.channel.send("Po 10 próbach gejoza dalej obecna, zmień tagi ( ͡° ͜ʖ ͡°)")
            break
    else:
        return current_picture


def rating_formatter(message):
    _tags = message.content[7:]
    if 'rating:' not in _tags:
        _tags = _tags + ' rating:safe'
        return _tags
    if 'rating:any' in _tags:
        _tags = _tags.replace('rating:any', '')
        return _tags
    else:
        return _tags


async def waiting_and_responding(_tags, banned_tags, message, picture):
    _i = 20
    while len(picture) == 0 and _i != 0:
        await asyncio.sleep(1)
        _i -= 1
    if len(picture) == 0:
        response = '¯\_(ツ)_/¯'
    else:
        response = await picture_filter(_tags, banned_tags, message, picture)
        try:
            response = response[0]['large_file_url']
        except:
            response = response[0]['file_url']
    return response
