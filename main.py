import logging
from utils import bot_functions


#logowanie błędów
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Uruchamianie bota i jego funkcji.
client = bot_functions.ShinshaBrain()
client.run('ODA0MzQ4MjIxNzQ4OTM2NzA0.YBLBqA.iFZa05rXjQAP9rAX__pNbBgQdGA')




