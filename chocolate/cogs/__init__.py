import os
from discord.ext.commands import Bot


async def load_cogs(bot: Bot) -> list[str]:
    cogs_path = os.path.dirname(__file__)

    cogs = [
        f"chocolate.cogs.{f[:-3]}" for f in os.listdir(cogs_path)
        if f.endswith(".py")
        and not f.startswith('_')
    ]

    for cog in cogs:
        await bot.load_extension(cog)

    return cogs


async def reload_cogs(bot: Bot) -> list[str]:
    cogs_path = os.path.dirname(__file__)

    cogs = [
        f"chocolate.cogs.{f[:-3]}" for f in os.listdir(cogs_path)
        if f.endswith(".py")
        and not f.startswith('_')
    ]

    for cog in cogs:
        await bot.reload_extension(cog)

    return cogs
