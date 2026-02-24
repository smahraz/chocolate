from discord.ext import commands


class EveryoneTools(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def cleardm(self, ctx: commands.Context) -> None:
        async for msg in ctx.author.history(limit=50):
            if msg.author == self.bot.user:
                await msg.delete()


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(EveryoneTools(bot))
