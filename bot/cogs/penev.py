import random
import json
from datetime import datetime, timedelta
import discord
import asyncio
import requests
import os
from discord.ext import tasks, commands

# helper.py
from classes.helper import random_member

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
from bot import config


class Penev(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=config['guilds'],
        name='penev',
        description='Oliver Penev'
    )
    async def penev(self, ctx):
        await ctx.respond('Oliver Penev!')
        members = ctx.guild.members
        for member in members:
            try:
                await member.edit(nick='Oliver Penev')
            except:
                print(f'Failed to change {member.name}\'s nickname')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog PENEV is online')


def setup(bot):
    bot.add_cog(Penev(bot))
