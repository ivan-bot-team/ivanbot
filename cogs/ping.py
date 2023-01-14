import random
import json
from datetime import datetime, timedelta
import discord
from discord.ext import tasks, commands

# helper.py
from classes.helper import random_member

global_config = json.load(open('config.json', encoding='utf-8'))
config = global_config['ping']
targets = []


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=config['frequencies']['random'])
    async def ping_random(self):
        for channelID in config['channels']:
            channel = self.bot.get_channel(channelID)
            member = random_member(channel)
            message = random.choice(config['random_messages'])
            await channel.send(f'{member.mention} {message}')

    @tasks.loop(minutes=config['frequencies']['target'])
    async def ping_target(self):
        for target in targets:
            time = target['end_time']
            if datetime.now() > time:
                print('over')
                targets.remove(target)

            channel = self.bot.get_channel(target['channel'])
            member = self.bot.get_user(target['member'])
            message = random.choice(config['target_messages'][target['ping_type']])
            await channel.send(f'{member.mention} {message}')

    @commands.slash_command(
        guild_ids=global_config['slash_commands_guilds'],
        name='ping',
        description='ping a member to do something frequently'
    )
    async def ping(
            self, ctx,
            member: discord.Member,
            ping_type: discord.Option(str, 'What type of ping?', choices=[
                discord.OptionChoice('Kodit', 'code'),
                discord.OptionChoice('Stazovat', 'wezeo'),
                discord.OptionChoice('Kupit macbook', 'macbook')
            ]),
            end_time: discord.Option(float, 'How long should the pinging last? (in hours)')
    ):
        time = datetime.now() + timedelta(hours=end_time)
        channel = ctx.channel
        target = {
            'member': member.id,
            'author': ctx.author.id,
            'ping_type': ping_type,
            'channel': channel.id,
            'end_time': time
        }
        targets.append(target)

        await ctx.respond(f'Pinging {member.mention} to {ping_type} for {end_time} hours', ephemeral=True)

    @commands.slash_command(
        guild_ids=global_config['slash_commands_guilds'],
        name='remove-ping',
        description='remove the pingings of a member'
    )
    async def remove_ping(self, ctx, member: discord.Member = 'self'):
        member = ctx.author if member == 'self' else member
        targets.remove((next(
            (
                target for target in targets if (target['author'] == ctx.author.id or target['member'] == member.id or ctx.author.guild_permissions.administrator)
            ), None
        )))
        await ctx.respond(f'Removed pingings of {member.mention}')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog PING is online')

        # start task
        self.ping_random.start()
        self.ping_target.start()


def setup(bot):
    bot.add_cog(Ping(bot))
