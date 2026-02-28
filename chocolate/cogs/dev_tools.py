from asyncio import sleep
from discord.ext import commands
from chocolate.config import bot_config
from chocolate.cogs import reload_cogs


class DevTools(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*bot_config.roles.devs)
    async def devReload(self, ctx: commands.Context) -> None:
        cogs = await reload_cogs(self.bot)
        await self.bot.tree.sync()
        msg = await ctx.send("\n".join(cogs))
        await sleep(2)
        await msg.delete()

    @commands.command()
    @commands.has_any_role(*bot_config.roles.devs)
    async def devCommand(self, ctx: commands.Context) -> None:
        for cmd in self.bot.tree.get_commands():
            await ctx.send(cmd.name + "-" + cmd.description)


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(DevTools(bot))
