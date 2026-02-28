from discord.ext import commands
from chocolate.api42 import IntraV2
from chocolate.cards import ProfileCard
from chocolate.config import bot_config
from discord import Interaction
from discord import app_commands as app


class IntraTools(commands.Cog):

    @app.command(description="Show intra profile")
    async def profile(self, interaction: Interaction, login: str):
        user_data = IntraV2.profile_info(login)
        await interaction.response.send_message(
            embed=ProfileCard.embed(user_data)
        )


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(IntraTools(bot))
