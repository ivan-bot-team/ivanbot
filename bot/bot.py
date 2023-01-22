import json
import os
from itertools import cycle
import asyncio
from dotenv import load_dotenv
from classes.config import load_config

import discord
from discord.ext import tasks

# Loading
config = None
url = ''

# load .env file
load_dotenv()


def load_conf():
    global url
    url = os.getenv('CMS_URL')
    global config
    config = asyncio.run(load_config(url))


def load():
    for cogs in config['cogs']:
        bot.load_extension(f'cogs.{cogs["filename"]}')


# bot declaration

# intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# bot variable/object init
bot = discord.Bot(intents=intents)


# launch
@bot.event
async def on_ready():
    print('Successfully connected bot to discord services!')


load_conf()
load()
bot.run(config['bot_token'])
