import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from core import checks
from core.models import PermissionLevel


class TempVoice(commands.Cog):
    """
    Temporary Voice Channels
    """

    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel != None:
            if after.channel.id == 1052439150026047589:
                for guild in self.bot.guilds:
                    category = discord.utils.get(
                        member.guild.categories, id=906587511109865522)
                    channel2 = await member.guild.create_voice_channel(name=f'{member.display_name}', category=category)
                    await channel2.set_permissions(member, connect=True, manage_channels=True)
                    await channel2.edit(user_limit=2)
                    await member.move_to(channel2)

                    def check(x, y, z):
                        return len(channel2.members) == 0
                    await self.bot.wait_for('voice_state_update', check=check)
                    await channel2.delete()
                    return


async def setup(bot):
    await bot.add_cog(TempVoice(bot))