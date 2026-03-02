from discord.ext import commands
from chocolate.cogs import load_cogs
import discord
import dotenv
import os
# import logging


dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


# handler = logging.FileHandler(
#     filename="log/discord.log",
#     encoding="utf-8",
#     mode="w"
# )

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.load_extension("chocolate.tracker.cog")
    await load_cogs(bot)
    await bot.tree.sync()
    print(f"[{bot.user.name}] loaded")


@bot.event
async def on_member_join(members: discord.Member):
    await members.send(f"{members.mention} Mr7babik")


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"pong {ctx.author.mention}")


if __name__ == "__main__":
    # bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
    bot.run(TOKEN)
