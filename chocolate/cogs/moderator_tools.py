from asyncio import sleep
from discord.ext import commands
from chocolate.config import bot_config
from discord import app_commands as app
from discord import Interaction


class ModeratorTools(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    async def cog_check(self, ctx) -> bool:
        print("error")
        if not any(
            role.name in bot_config.roles.moderators
            for role in ctx.author.roles
        ):
            raise commands.MissingAnyRole(bot_config.roles.moderators)
        return True

    @app.command(
        name="clear",
        description="Clear all messages in this channel"
    )
    @app.checks.has_any_role(*bot_config.roles.clear_channel)
    async def clear(self, interaction: Interaction) -> None:
        await interaction.response.send_message(
            "Clearing this channel by you",
            ephemeral=True
        )
        await sleep(1)
        await interaction.channel.purge(limit=None)

    @clear.error
    async def clear_error(
            self,
            interaction: Interaction,
            error: app.AppCommandError
    ):
        if isinstance(error, app.MissingAnyRole):
            await interaction.response.send_message(
                "You don't have permission to clear this channel.",
                ephemeral=True
            )
        elif isinstance(error, app.NoPrivateMessage):
            await interaction.response.send_message(
                "You could try `/cleardm` here."
            )
        else:
            raise error

    @commands.command()
    @commands.has_any_role(*bot_config.roles.intra_access)
    async def harem(self, ctx: commands.Context) -> None:  # name just a joke.
        bot_replay = await ctx.message.reply(
            f"Clear non-bot messages {ctx.author.mention}"
        )
        async for msg in ctx.history(limit=None):
            if not msg.author.bot:
                await msg.delete()
        await bot_replay.delete()


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(ModeratorTools(bot))
