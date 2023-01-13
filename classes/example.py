import random
import json
import discord
from discord.ext import tasks, commands

# helper.py
from classes.helper import random_member

global_config = json.load(open('config.json'))
config = global_config['example']


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog EXAMPLE is online')


def setup(bot):
    bot.add_cog(Example(bot))
