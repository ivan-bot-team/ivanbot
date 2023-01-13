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

bot_status = cycle(['Kodim PHP', 'Stazujem vo Wezeu', 'Predavam deodoranty', 'Kupujem macbook', 'Nadavam na Microsoft'])


@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(bot_status)))


@bot.event
async def on_ready():
    print('Successfully connected bot to discord services!')
    change_status.start()


load()
bot.run(os.getenv('TOKEN'))
