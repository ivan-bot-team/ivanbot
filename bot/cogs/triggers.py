import random
import json
import os
import asyncio
from discord.ext import tasks, commands
import requests

url = os.getenv('CMS_URL')


class Triggers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # if message author is bot, ignore
        if message.author == self.bot.user:
            return

        content = message.content.lower()
        reply = requests.get(f'{url}/api/v1/triggers/message', params={'message': content})
        if reply.status_code == 200:
            await message.channel.send(reply.json()['data']['message'])
            return

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog TRIGGERS is online')


def setup(bot):
    bot.add_cog(Triggers(bot))
