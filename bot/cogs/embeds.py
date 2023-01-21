import json
import discord
from discord.ext import commands

global_config = json.load(open('config.json'))
# config = global_config['embeds'] TODO: ??? maybe embeds config


def make_embed(name):
    data = json.load((open(f'data/embeds/{name}.json', encoding='utf-8')))

    embed = discord.Embed(
        title=data['title'],
        description=data['description'],
        # color=data['color'], TODO: fix this
    )

    for field in data['fields']:
        embed.add_field(
            name=field['name'],
            value=field['value'],
            inline=field['inline'],
        )

    embed.set_footer(text=data['footer'])
    embed.set_author(name=data['author']['name'], icon_url=data['author']['icon_url'])
    embed.set_thumbnail(url=data['thumbnail'])
    embed.set_image(url=data['image'])

    return embed


class Embeds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Sends an embed')
    async def mac(self, ctx):
        await ctx.respond(embed=make_embed('mac'))

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog EMBEDS is online')


def setup(bot):
    bot.add_cog(Embeds(bot))
