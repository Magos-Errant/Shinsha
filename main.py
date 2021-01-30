#import logging
import os
from utils import bot_functions
from flask import Flask
from threading import Thread

#logowanie błędów
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

#Uruchamianie bota i jego funkcji.
client = bot_functions.ShinshaBrain()
app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

client.run(os.getenv('TOKEN'))



