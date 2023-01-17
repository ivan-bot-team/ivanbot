import random
import json
import slovakrailways as zsr
from datetime import datetime, timedelta
import discord
from discord.ext import tasks, commands

# helper.py
from classes.helper import random_member

global_config = json.load(open('config.json', encoding='utf-8'))
# config = global_config['example']


class Trains(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
            guild_ids=global_config['slash_commands_guilds'],
            name='search-station',
            description='search departures from a station'
    )
    async def search_station(self, ctx, station: discord.Option(str, 'What station do you want to search?')):

        result = zsr.search_stations(station)
        print(result)
        departures = zsr.departures(result[0]['uicCode'])
        departures = departures[:5]
        # newdepartures = []
        # for departure in departures:
        #     departure['train']['features'] = ''
        #     newdepartures.append(departure)

        departures[0]['train']['features'] = ''

        await ctx.respond(departures[0])

        # await ctx.respond(departures['station'])
        # nz: 5613436

    @commands.slash_command(
        guild_ids=global_config['slash_commands_guilds'],
        name='nove-zamky',
        description='search departures from nove zamky'
    )
    async def nove_zamky(self, ctx):
        departures = zsr.departures('5613436')[:10]

        embed = discord.Embed(
            title='Departures Nové Zámky',
            # color=data['color'], TODO: fix this
        )

        for train in departures:
            embed.add_field(
                name=train['station'],
                value=str(datetime.fromtimestamp(int(train['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')),
                inline=False,
            )

        embed.set_footer(text='Powered by slovakrailways')
        embed.set_author(name='Felvidek')
        # embed.set_thumbnail(url=data['thumbnail'])
        # embed.set_image(url=data['image'])

        await ctx.respond(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog TRAINS is online')


def setup(bot):
    bot.add_cog(Trains(bot))
