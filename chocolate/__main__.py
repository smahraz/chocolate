from chocolate.api42 import IntraV2
from chocolate.cards import ProfileCard
from discord.ext import commands
import discord
import dotenv
import os
import logging


dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


handler = logging.FileHandler(
    filename="log/discord.log",
    encoding="utf-8",
    mode="w"
)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Starting... {bot.user.name}")


@bot.event
async def on_member_join(members):
    await members.send("Mr7babik")


@bot.event
async def on_message(msg: discord.Message):
    if msg.author == bot.user:
        return
    if msg.content.lower().startswith("!delete "):
        await msg.delete()
        await msg.channel.send(
            f"{msg.author.mention} your message was deleted"
        )
    await bot.process_commands(msg)


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"pong {ctx.author.mention}")


@bot.command()
async def profile(ctx: commands.Context, login: str = ""):
    if not login:
        await ctx.message.reply("!profile <login>")
        return
    user_data = IntraV2.profile_info(login)
    await ctx.send(embed=ProfileCard.embed(user_data))


if __name__ == "__main__":
    bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
