import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from core import checks
from core.models import PermissionLevel
from discord.ui import Button, View
from discord import Interaction

class TempVoiceView(discord.ui.View):
    def __init__(self, member, timeout=None):
        super().__init__(timeout=timeout)
        self.member = member
        self._children = []
        self.member = member
        self._children = []

    @discord.ui.button(label='Increase User Limit', custom_id='increase_limit')
    async def increase_limit(self,  interaction: discord.Interaction, button: discord.ui.Button):
         channel = interaction.channel
         await channel.edit(user_limit=channel.user_limit + 1)
         await interaction.response.edit_message(content=f"{self.member.mention}, the user limit of this channel has been increased to {channel.user_limit}.")

    @discord.ui.button(label='Decrease User Limit', custom_id='decrease_limit')
    async def decrease_limit(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        await channel.edit(user_limit=channel.user_limit - 1)
        await interaction.response.edit_message(content=f"{self.member.mention}, the user limit of this channel has been decreased to {channel.user_limit}.")

    @discord.ui.button(label='Change Channel Name', custom_id='change_name')
    async def change_name(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        await channel.edit(name='New Channel Name')
        await interaction.response.edit_message(content=f"{self.member.mention}, the name of this channel has been changed to 'New Channel Name'.")

    async def interaction_check(self, interaction: Interaction):
        if interaction.user.id == self.member.id:
            return True
        else:
            await interaction.response.send_message("You cannot interact with this view.", ephemeral=True)
            return False 

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
            if after.channel.id == 1053581804294119515:
                for guild in self.bot.guilds:
                    category = discord.utils.get(member.guild.categories, id=745514186531930164)
                    channel2 = await member.guild.create_voice_channel(name=f'{member.display_name}', category=category)
                    await channel2.set_permissions(member, connect=True, manage_channels=True)
                    await channel2.edit(user_limit=2)
                    await member.move_to(channel2)
                    

                # Send message to the created channel
                    message = await channel2.send(f"Hey there, {member.mention}! You can modify your temp channel by clicking on the buttons below.")

                    view = TempVoiceView(member)
                    print(view)
                    await message.edit(view=view)

                # Wait for the voice channel to be empty before deleting it
                    def check(x, y, z):
                        return len(channel2.members) == 0
                    await self.bot.wait_for('voice_state_update', check=check)
                    await channel2.delete()
                    return

  #  @commands.Cog.listener()
  #  async def on_voice_state_update(self, member, before, after):
   #     if after.channel != None:
   #         if after.channel.id == 1052439150026047589:
   ##             for guild in self.bot.guilds:
    #                category = discord.utils.get(
    #                    member.guild.categories, id=906587511109865522)
      #              channel2 = await member.guild.create_voice_channel(name=f'{member.display_name}', category=category)
       #             await channel2.set_permissions(member, connect=True, manage_channels=True)
       #             await channel2.edit(user_limit=2)
       #             await member.move_to(channel2)
#
          #          def check(x, y, z):
        #                return len(channel2.members) 
        #            await self.bot.wait_for('voice_state_update', check=check)
        #            await channel2.delete()
              #      return


async def setup(bot):
    await bot.add_cog(TempVoice(bot))
