import discord
from discord.ext import commands
import stringcase
import re
import random
import unicodedata
from unidecode import unidecode
from core import checks
from core.models import PermissionLevel

class mcBridge(commands.Cog):
    """
    Report logger
    """

    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    staff_members = [667378631336525824]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 1054033775673217165:
            if "warn" in message.content:
                if message.author.id in staff_members:
                    match = re.search(r"\[\w+\s\d+:\d+:\d+\sINFO\s\]\s(.+?)\sgot\swarned\sby\sServer\sfor:\s(.+?)$", message.content)
                    if match:
                        username = match.group(1)
                        reason = match.group(2)
                        channel = self.bot.get_channel(1045997888502759505)
                        await channel.send(f"{message.author.name} issued a warning to {username} for: {reason}")

async def setup(bot):
    await bot.add_cog(mcBridge(bot))
