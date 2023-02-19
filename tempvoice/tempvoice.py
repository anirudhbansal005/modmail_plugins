import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from core import checks
from core.models import PermissionLevel
from discord.ui import Button, View

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
                    category = discord.utils.get(member.guild.categories, id=906587511109865522)
                    channel2 = await member.guild.create_voice_channel(name=f'{member.display_name}', category=category)
                    await channel2.set_permissions(member, connect=True, manage_channels=True)
                    await channel2.edit(user_limit=2)
                    await member.move_to(channel2)
                    def check(x, y, z):
                        return len(channel2.members) == 0

                # Send message to the created channel
                message = await channel2.send(f"Hey there, {member.mention}! You can modify your temp channel by clicking on the buttons below.")

                # Define the button callback function
                async def button_callback(interaction: discord.Interaction):
                    if interaction.custom_id == "increase_limit":
                        await channel2.edit(user_limit=channel2.user_limit + 1)
                        await interaction.response.edit_message(content=f"{member.mention}, the user limit of this channel has been increased to {channel2.user_limit}.")
                    elif interaction.custom_id == "decrease_limit":
                        await channel2.edit(user_limit=channel2.user_limit - 1)
                        await interaction.response.edit_message(content=f"{member.mention}, the user limit of this channel has been decreased to {channel2.user_limit}.")
                    elif interaction.custom_id == "change_name":
                        await channel2.edit(name="New Channel Name")
                        await interaction.response.edit_message(content=f"{member.mention}, the name of this channel has been changed to 'New Channel Name'.")

                # Define the button row and add the buttons
                button_row = View()
                button_row.add_item(Button(label="Increase User Limit", custom_id="increase_limit"))
                button_row.add_item(Button(label="Decrease User Limit", custom_id="decrease_limit"))
                button_row.add_item(Button(label="Change Channel Name", custom_id="change_name"))

                # Send the button row
                await message.edit(view=button_row)

                # Wait for the voice channel to be empty before deleting it

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
