import random
import json
import discord
from discord.ext import tasks, commands

global_config = json.load(open('config.json'))


def random_member(bot, channel):
    """
    Random Member, returns random member from channel also removes bots
    :param bot: self.bot
    :param channel: channel object
    :return: user object
    """
    return random.choice([member for member in channel.members if not member.bot])
