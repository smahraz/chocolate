import os
from discord.ext.commands import Bot


async def load_cogs(bot: Bot):
    cogs_path = os.path.dirname(__file__)

    files = [
        f for f in os.listdir(cogs_path)
        if f.endswith(".py")
        and not f.startswith('_')
    ]

    for fl in files:
        await bot.load_extension(f"chocolate.cogs.{fl[:-3]}")
