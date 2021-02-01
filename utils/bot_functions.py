from __future__ import unicode_literals
import discord
import asyncio
import datetime as dt
import NyaaPy
from .keep_alive import keep_alive
from discord.ext import tasks
from pybooru import Danbooru
from .data_storage import jeronimo_martins
from .tao import TaoTeChing

data_container = jeronimo_martins()
client = discord.Client
message_timeout = 120


class ShinshaBrain(client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.day_summary.start()
        keep_alive()

    # funkcje poniżej obsługują wyświetlanie i czyszczenie statstyk serwera dokładnie o północy
    @tasks.loop(hours=24)
    async def day_summary(self):
        message_channel = self.get_channel(790949987609608212)
        message_channel.send(data_container.counter_status)
        data_container.clear_data()
        await message_channel.send("Nastał nowy dzień!")

    @day_summary.before_loop
    async def before_day_summary(self):
        for _ in range(60 * 60 * 24):  # loop the whole day
            if dt.datetime.now().strftime("%H:%M:%S") == dt.time(hour=0, minute=0, second=0).strftime(
                    "%H:%M:%S"):  # 24 hour format
                print('It is rewind time!')
                return
            await asyncio.sleep(1)  # wait a second before looping again. You can make it more

    #definicje metody wywołwywanych on message
    async def chop_long_string(self, string, message):
      if len(string) < 2000:
          message = await message.channel.send(string)
      else:
        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                    
        if len(firstpart) >= 2000:
          message = await message.channel.send('Shiver me timbers maytey! Be more specific')
        else:
            message = await message.channel.send(firstpart)
            message1 = await message.channel.send(secondpart)
            return message, message1

    async def hello(self, message):
      if message.channel.id == 805839570201608252:
        message = await message.channel.send('Hello!')
      else:
        await message.delete()
        message = await message.channel.send('Hello!')
        await asyncio.sleep(message_timeout)
        await message.delete()

    async def message_count(self, message):
      if message.channel.id == 805839570201608252:
        message = await message.channel.send(data_container.counter_status)
      else:  
        await message.delete()
        message = await message.channel.send(data_container.counter_status)
        await asyncio.sleep(message_timeout)
        await message.delete()

    async def commands(self, message):
      if message.channel.id == 805839570201608252:
        _commands_dict = data_container.avaliable_commands
        _string = '''Lista komend:\n'''
        for key in _commands_dict:
          value = _commands_dict[key]
          _string = _string + f'{key} - {value}\n'
        message = await message.channel.send(_string)
        await asyncio.sleep(message_timeout)
      else:
        await message.delete()
        _commands_dict = data_container.avaliable_commands
        _string = '''Lista komend:\n'''
        for key in _commands_dict:
          value = _commands_dict[key]
          _string = _string + f'{key} - {value}\n'
        message = await message.channel.send(_string)
        await asyncio.sleep(message_timeout)
        await message.delete()

    async def tao(self, message):
      _taoteching = TaoTeChing()
      if message.channel.id == 805839570201608252:
        message = await message.channel.send(_taoteching.random_quote())
      else:
        await message.delete()
        message = await message.channel.send(_taoteching.random_quote())
        await asyncio.sleep(message_timeout)
        await message.delete()

    async def danbo(self, message):
      _tags = message.content[7:]
      if message.channel.id == 805839570201608252:
        if 'rating:' not in _tags:
          _tags = _tags + ' rating:safe'
        danbo_client = Danbooru('danbooru')
        posts = danbo_client.post_list(tags=_tags, limit=1, random=True)
        _i = 20
        while len(posts) == 0 and _i != 0:
          await asyncio.sleep(1)
          _i -= 1
        if len(posts) == 0:
          message = await message.channel.send('¯\_(ツ)_/¯')
        else:  
          message = await message.channel.send(posts[0]['file_url'])
      else:
        await message.delete()
        if 'rating:' not in _tags:
          _tags = _tags + ' rating:safe'
        danbo_client = Danbooru('danbooru')
        posts = danbo_client.post_list(tags=_tags, limit=1, random=True)
        _i = 20
        while len(posts) == 0 and _i != 0:
          await asyncio.sleep(1)
          _i -= 1
        if len(posts) == 0:
          message = await message.channel.send('¯\_(ツ)_/¯')
        else:  
          message = await message.channel.send(posts[0]['file_url'])
        await asyncio.sleep(message_timeout)
        await message.delete()

    async def nyaar(self, message):
      _tags = message.content[5:]
      if message.channel.id == 805839570201608252:
        Arr = NyaaPy.Nyaa
        _result = Arr.search(_tags)
    
#ensuring that server will respond and catching situation when it does not
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

#formatting string to send as a message
        string = ""
        for _dict in _selected_animu:
          string = string + f"{_dict['name']}\n{_dict['url']} S: {_dict['seeders']} L: {_dict['leechers']} Size: {_dict['size']}\n\n"

        await self.chop_long_string(string, message)
      else:
        await message.delete()
        Arr = NyaaPy.Nyaa
        _result = Arr.search(_tags)
#ensuring that server will respond and catching situation when it does not
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

#formatting string to send as a message
          string = ""
          for _dict in _selected_animu:
            string = string + f"{_dict['name']}\n{_dict['url']} S: {_dict['seeders']} L: {_dict['leechers']} Size: {_dict['size']}\n\n"
           
          await self.chop_long_string(string, message)

      await asyncio.sleep(message_timeout)
      await message.delete()
      await message1.delete()


# funkcje poniżej obsługują reakcje bota na wiadomości
    async def on_message(self, message):
        if message.author == self.user:
          return

        elif message.content.startswith('!hello'):
          await self.hello(message)  

        elif message.content.startswith('!message_count'):
          await self.message_count(message)

        elif message.content.startswith('!commands'):
          await self.commands(message)

        elif message.content.startswith('!tao'):
          await self.tao(message)

        elif message.content.startswith('!danbo'):
          await self.danbo(message)

        #Some Pirate funcionality
        elif message.content.startswith('!arr '):
          await self.nyaar(message)        
          
        else:
          data_container.message_counter(message.channel.name)

        # if message.content.startswith('$counter_reset'):
        #     data_container.clear_data()
        #     await message.channel.send('Data cleared!')
