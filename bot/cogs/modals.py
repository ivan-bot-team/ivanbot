import random
import json
import discord
from discord.ext import tasks, commands


# global_config = json.load(open('config.json', encoding='utf-8'))
# config = global_config['modals']


class MyModal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # self.add_item(discord.ui.InputText(label="Názov písomky:"))
        # self.add_item(discord.ui.InputText(label="Dátum písomky:"))
        # self.add_item(discord.ui.InputText(label="Informácie k písomke:", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Písomka")
        embed.add_field(name="Názov písomky", value=self.children[0].value)
        embed.add_field(name="Dátum písomky", value=self.children[1].value)
        embed.add_field(name="Informácie", value=self.children[2].value)
        await interaction.response.send_message(embeds=[embed])

    @commands.slash_command()
    async def create_exam(self, ctx):
        """Shows an example of a modal dialog being invoked from a slash command."""
        modal = MyModal(title="Vytvoriť písomku")
        await ctx.send_modal(modal)


def setup(bot):
    bot.add_cog(Example(bot))
