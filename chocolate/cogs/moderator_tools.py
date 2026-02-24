from asyncio import sleep
from discord.ext import commands


class ModeratorTools(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def clear(self, ctx: commands.Context) -> None:
        await ctx.message.reply(
            f"This channel will be clear {ctx.author.mention}"
        )
        await sleep(5)
        await ctx.channel.purge(limit=None)

    @commands.command()
    async def spam(self, ctx: commands.Context, amount: int = 0) -> None:
        if amount > 10:
            await ctx.message.reply("WTF!")
            return
        for _ in range(amount):
            await ctx.send("spam")
            await sleep(0.2)
        await ctx.send("done spamming!")


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(ModeratorTools(bot))
