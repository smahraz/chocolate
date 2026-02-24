from asyncio import sleep
from discord.ext import commands
from chocolate.config import bot_config


class ModeratorTools(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*bot_config.moderators)
    async def clear(self, ctx: commands.Context) -> None:
        await ctx.message.reply(
            f"This channel will be clear {ctx.author.mention}"
        )
        await sleep(5)
        await ctx.channel.purge(limit=None)

    @clear.error
    async def clear_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.author.send(
                "You don't have permission for that action, sorry <3"
            )
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send("Try !cleardm")
        else:
            raise error


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(ModeratorTools(bot))
