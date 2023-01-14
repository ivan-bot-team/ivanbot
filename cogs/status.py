import random
import json
import discord
from discord.ext import tasks, commands
from itertools import cycle

# helper.py
from classes.helper import random_member

global_config = json.load(open('config.json', encoding='utf-8'))
config = global_config['status']
messages = cycle(config['messages'])


class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=config['frequency'])
    async def change_status(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(messages)))

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog STATUS is online')
        self.change_status.start()

def setup(bot):
    bot.add_cog(Status(bot))
