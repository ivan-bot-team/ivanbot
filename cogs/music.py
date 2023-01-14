import random
import json
import discord
import wavelink
from discord.ext import tasks, commands

# helper.py
from classes.helper import random_member

global_config = json.load(open('config.json'), encoding='utf-8')
config = global_config['music']


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    bot = discord.Bot()

async def connect_nodes():
  """Connect to our Lavalink nodes."""
  await bot.wait_until_ready() # wait until the bot is ready

  await wavelink.NodePool.create_node(
    bot=bot,
    host='0.0.0.0',
    port=2333,
    password='youshallnotpass'
  ) # create a node

@commands.Cog.listener()
async def on_ready(self):
        print('Cog MUSIC is online')

@bot.slash_command(name="play")
async def play(ctx, search: str):
  vc = ctx.voice_client # define our voice client

  if not vc: # check if the bot is not in a voice channel
    vc = await ctx.author.voice.channel.connect(cls=wavelink.Player) # connect to the voice channel

  if ctx.author.voice.channel.id != vc.channel.id: # check if the bot is not in the voice channel
    return await ctx.respond("You must be in the same voice channel as the bot.") # return an error message

  song = await wavelink.YouTubeTrack.search(query=search, return_first=True) # search for the song

  if not song: # check if the song is not found
    return await ctx.respond("No song found.") # return an error message

  await vc.play(song) # play the song
  await ctx.respond(f"Now playing: `{vc.source.title}`") # return a message

def setup(bot):
    bot.add_cog(Music(bot))