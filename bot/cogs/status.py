import random
import json
import discord
import asyncio
from discord.ext import tasks, commands
from itertools import cycle

# helper.py
from classes.helper import random_member

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
from bot import config
messages = cycle(config['status_messages'])


class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=config['status_freq'])
    async def change_status(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=next(messages)['message']))

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog STATUS is online')
        self.change_status.start()


def setup(bot):
    bot.add_cog(Status(bot))
