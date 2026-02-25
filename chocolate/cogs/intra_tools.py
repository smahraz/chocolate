from discord.ext import commands
from chocolate.api42 import IntraV2
from chocolate.cards import ProfileCard
from chocolate.config import bot_config


class IntraTools(commands.Cog):

    @commands.command()
    @commands.has_any_role(*bot_config.roles.intra_access)
    async def profile(self, ctx: commands.Context, login: str = ""):
        if not login:
            await ctx.message.reply("!profile <login>")
            return
        user_data = IntraV2.profile_info(login)
        await ctx.send(embed=ProfileCard.embed(user_data))


async def setup(bot: commands.Bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(IntraTools(bot))
