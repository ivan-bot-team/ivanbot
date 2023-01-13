import json
import os
from itertools import cycle
from dotenv import load_dotenv

import discord
from discord.ext import tasks

global_config = json.load(open('config.json'))

# Loading

# load .env file
load_dotenv()


def load():
    for cogs in global_config['cogs']:
        bot.load_extension(f'cogs.{cogs}')


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

load()
bot.run(os.getenv('TOKEN'))
