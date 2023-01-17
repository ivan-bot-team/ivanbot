import json
import os
from itertools import cycle
from dotenv import load_dotenv

import discord
from discord.ext import tasks

global_config = json.load(open('config.json', encoding='utf-8'))

# Loading

# load .env file
load_dotenv()


def load():
    for cogs in global_config['cogs']:
        bot.load_extension(f'cogs.{cogs}')


# bot declaration

# intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# bot variable/object init
bot = discord.Bot(intents=intents)
#modals

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Názov písomky:"))
        self.add_item(discord.ui.InputText(label="Dátum písomky:"))
        self.add_item(discord.ui.InputText(label="Informácie k písomke:", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Písomka")
        embed.add_field(name="Názov písomky", value=self.children[0].value)
        embed.add_field(name="Dátum písomky", value=self.children[1].value)
        embed.add_field(name="Informácie", value=self.children[2].value)
        await interaction.response.send_message(embeds=[embed])

@bot.slash_command()
async def create_exam(ctx: discord.ApplicationContext):
    """Shows an example of a modal dialog being invoked from a slash command."""
    modal = MyModal(title="Vytvoriť písomku")
    await ctx.send_modal(modal)

# launch
@bot.event
async def on_ready():
    print('Successfully connected bot to discord services!')

load()
bot.run(os.getenv('TOKEN'))
