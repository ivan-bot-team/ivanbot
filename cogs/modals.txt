import random
import json
import discord
from discord.ext import tasks, commands

#global_config = json.load(open('config.json', encoding='utf-8'))
#config = global_config['modals']

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Short Input"))
        self.add_item(discord.ui.InputText(label="Long Input", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=self.children[0].value)
        embed.add_field(name="Long Input", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])

    @commands.slash_command()
    async def modal_slash(ctx: discord.ApplicationContext):
            """Shows an example of a modal dialog being invoked from a slash command."""
            modal = MyModal(title="Modal via Slash Command")
            await ctx.send_modal(modal)