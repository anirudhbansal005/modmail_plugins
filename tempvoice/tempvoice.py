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
            if after.channel.id == 776726741937946644:
                for guild in bot.guilds:
                    maincategory = discord.utils.get(
                        guild.categories, id=700246237244555336)
                    channel2 = await guild.create_voice_channel(name=f'канал {member.display_name}', category=maincategory)
                    await channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                    await member.move_to(channel2)

                    def check(x, y, z):
                        return len(channel2.members) == 0
                    await bot.wait_for('voice_state_update', check=check)
                    await channel2.delete()



async def setup(bot):
    await bot.add_cog(TempVoice(bot))
