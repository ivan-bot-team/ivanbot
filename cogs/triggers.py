import random
import json
import discord
from discord.ext import tasks, commands

# helper.py
from classes.helper import compare_strings

global_config = json.load(open('config.json', encoding='utf-8'))
config = global_config['triggers']


class Triggers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # if message author is bot, ignore
        if message.author == self.bot.user:
            return

        content = message.content.lower()

        for trigger in config:
            if compare_strings(trigger['keyword'], content):
                await message.channel.send(random.choice(trigger['messages']))
                return

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog TRIGGERS is online')


def setup(bot):
    bot.add_cog(Triggers(bot))
