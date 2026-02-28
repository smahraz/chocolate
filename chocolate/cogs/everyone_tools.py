from discord.ext import commands
from discord import app_commands as app
from discord import Interaction


class EveryoneTools(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app.command(
        description="Delete all the messages sent by bot in your DM"
    )
    async def cleardm(self, interaction: Interaction) -> None:
        async for msg in interaction.user.history(limit=None):
            if msg.author == self.bot.user:
                await msg.delete()
        await interaction.response.send_message(
            "Your `DM` is clean.",
            ephemeral=True
        )


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(EveryoneTools(bot))
