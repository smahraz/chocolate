from discord.ext import commands, tasks
from chocolate.config import bot_config
from .time import LastCheck


class ProjectsTrackerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_closed_teams.start()

    @tasks.loop(seconds=450)
    async def last_closed_teams(self):
        channel_ids = bot_config.channels.projects_report
        channels = filter(
            lambda chnl: chnl is not None,
            [self.bot.get_channel(channel_id) for channel_id in channel_ids]
        )
        for chnl in channels:
            await chnl.send(f"hello {LastCheck.get_time()}")
            LastCheck.update_time()

    @last_closed_teams.before_loop
    async def before_checker(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    print(f"Loading [{__name__}]")
    await bot.add_cog(ProjectsTrackerCog(bot))
