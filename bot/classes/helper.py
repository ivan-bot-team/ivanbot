import random
import json
from thefuzz import fuzz
from thefuzz import process
import discord
from discord.ext import tasks, commands

global_config = json.load(open('config.json', encoding='utf-8'))
string_similarity = int(global_config['string_similarity'])


def random_member(channel):
    """
    Random Member, returns random member from channel also removes bots
    :param bot: self.bot
    :param channel: channel object
    :return: user object
    """
    return random.choice([member for member in channel.members if not member.bot])


def compare_strings(string1, string2):
    """
    Compare strings, returns True if strings are similar enough (75%)
    :param string1: string1
    :param string2: string2
    :return: boolean
    """
    score = fuzz.token_sort_ratio(string1, string2)
    return score > string_similarity
