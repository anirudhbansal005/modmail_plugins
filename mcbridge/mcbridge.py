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
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)


    @commands.Cog.listener
    async def on_message(self, message):
        if message.channel.id == 1054033775673217165:
            staff_roles = ["Server - Staff", "Minecraft Server - Staff"]
            author = None
            for role in message.author.roles:
                if role.name in staff_roles:
                    author = role.name
                    break
            if author:
                match = re.search(r"\[\w+\s\d+:\d+:\d+\sINFO\s\]\s(.+?)\sgot\s(.+?)\sby\sServer\sfor:\s(.+?)$", message.content)
                if match:
                    username = match.group(1)
                    action = match.group(2)
                    reason = match.group(3)
                    actions = ["warn", "ban", "tempban", "mute"]
                    if action in actions:
                        channel = self.bot.get_channel(1045997888502759505)
                        await channel.send(f"{author} issued a {action} to {username} for: {reason}")
