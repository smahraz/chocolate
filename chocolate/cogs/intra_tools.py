from discord.ext import commands
from chocolate.api42 import IntraV2
from chocolate.cards import ProfileCard, PermissionErrorCard
from chocolate.config import bot_config
from discord import Interaction
from discord import app_commands as app


_INTRA_EMBED_ERROR = PermissionErrorCard.embed(
    "You dont have access to **Intra**.\n"
    "Contact _Admins_ maybe,"
)


class IntraTools(commands.Cog):

    async def cog_check(self, ctx: commands.Context) -> bool:
        if not any(
            role.name in bot_config.roles.intra_access
            for role in ctx.author.roles
        ):
            raise commands.MissingAnyRole(bot_config.roles.intra_access)
        return True

    @app.command(description="Show intra profile")
    @app.describe(login="login you wanna show")
    @app.checks.has_any_role(*bot_config.roles.intra_access)
    async def profile(self, interaction: Interaction, login: str):
        user_data = IntraV2.profile_info(login)
        await interaction.response.send_message(
            embed=ProfileCard.embed(user_data)
        )

    @profile.error
    async def profile_erro(self, interaction: Interaction, error):
        if isinstance(error, app.MissingAnyRole):
            await interaction.response.send_message(
                embed=_INTRA_EMBED_ERROR,
                ephemeral=True
            )
        else:
            raise error


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(IntraTools(bot))
