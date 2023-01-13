import random
import json
import discord
from discord.ext import tasks, commands

# helper.py
from classes.helper import random_member

global_config = json.load(open('config.json'))
config = global_config['ping']


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=config['frequencies']['code'])
    async def ping_random(self):
        for channelID in config['channels']:
            channel = self.bot.get_channel(channelID)
            member = random_member(self.bot, channel)
            message = random.choice(config['messages']['code'])
            await channel.send(f'{member.mention} {message}')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog PING is online')

        # start task
        self.ping_random.start()


def setup(bot):
    bot.add_cog(Ping(bot))
