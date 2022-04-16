#import
import os
from utils import bot_functions
import discord
import discord.ext.commands as commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

#logowanie błędów
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

#Uruchamianie bota i jego funkcji.
client = commands.Bot("!")
DiscordComponents(client)
bot_functions.ShinshaBrain()

with open('Token.txt', 'r') as token:
    tok = str(token.readlines()[0]).strip()
client.run(tok)
