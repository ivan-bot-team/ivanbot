import slovakrailways as zsr
from datetime import datetime, timedelta
import discord
from discord.ext import tasks, commands
import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
from bot import config


async def get_station_departures(station_name):
    station = zsr.search_stations(station_name)[0]
    departures = zsr.departures(station['uicCode'])[:10]
    embed = discord.Embed(
        title=f'Departures {station["name"]}',
        color=discord.Colour.green()
    )

    train_types = zsr.meta.train_types()

    for train in departures:
        destination = train['station']
        departure = str(datetime.fromtimestamp(float(str(train['timestamp'])[:-3])))[11:][:-3]
        delay = train['train']['trainDelay']
        print(delay)
        if delay != None:
            delay = f' + {delay["delayMinutes"]} min'
        else:
            delay = ''
        train_type = next((type for type in train_types if type["value"] == train['train']['type']), {'name': 'KK'})[
            'name']
        train_number = train['train']['number']
        embed.add_field(
            name=destination,
            value=str(
                departure + delay + '\n**' + train_type + '** ' + str(train_number)
            ),
            inline=False,
        )

    embed.set_footer(text='Powered by Zajebane Slovenske Skurvene Kolaje')
    embed.set_author(name='Felvidek')
    # embed.set_thumbnail(url=data['thumbnail'])
    # embed.set_image(url=data['image'])

    return embed


class Trains(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        guild_ids=config['guilds'],
        name='search-station',
        description='search departures from a station'
    )
    async def search_station(self, ctx, station: discord.Option(str, 'What station do you want to search?')):
        try:
            embed = await get_station_departures(station)
            await ctx.respond(embed=embed)
        except:
            await ctx.respond('Zajebalo sa to, jebem tie zeleznice, skus ine meno stanice')

    @commands.slash_command(
        guild_ids=config['guilds'],
        name='track-train',
        description='track a train'
    )
    async def track_train(self, ctx, train_number: discord.Option(str, 'What train do you want to track(number)?')):
        try:
            train = zsr.track_train("273")
            number = train['trainNumber']
            # type = train['trainType']
            previous_station = train['trainDelay']['previousStation']
            current_station = train['trainDelay']['currentStation']
            next_station = train['trainDelay']['nextStation']
            delay = train['trainDelay']['delayMinutes']

            embed = discord.Embed(
                title=f'Tracking train {number}',
                # color=data['color'], TODO: fix this
            )
            embed.add_field(
                name='Previous station',
                value=previous_station,
                inline=False,
            )
            embed.add_field(
                name='Current station',
                value=current_station,
                inline=False,
            )
            embed.add_field(
                name='Next station',
                value=next_station,
                inline=False,
            )
            embed.add_field(
                name='Delay',
                value=delay,
                inline=False,
            )
            await ctx.respond(embed=embed)
        except:
            await ctx.respond('Jebem ich nejde im API')

    @commands.slash_command(
        guild_ids=config['guilds'],
        name='nove-zamky',
        description='search departures from nove zamky'
    )
    async def nove_zamky(self, ctx):
        try:
            embed = await get_station_departures('Nové Zámky')
            await ctx.respond(embed=embed)
        except:
            await ctx.respond('Zajebalo sa to, jebem tie zeleznice, skus ine meno stanice')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog TRAINS is online')


def setup(bot):
    bot.add_cog(Trains(bot))
