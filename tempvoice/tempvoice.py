import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from core import checks
from core.models import PermissionLevel
from discord.ui import Button, View
from discord import Interaction

class TempVoiceView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.author_id = author_id
        
    @discord.ui.button(label="Increase Limit", custom_id="increase")
    async def increase_callback(self,  interaction: discord.Interaction, button: discord.ui.Button):
         channel = interaction.channel
         print(channel)
         if interaction.user.id == self.author_id:
             await channel.edit(user_limit=channel.user_limit + 1)
             await interaction.response.send_message(f"the user limit of this channel has been increased to {channel.user_limit}.",ephemeral=True )
         else:
             await interaction.response.send_message(f"You are not allowed to interact with this button!",ephemeral=True)

    @discord.ui.button(label="Decrease User Limit", custom_id="persistent_view:decrease")
    async def decrease(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        min_limit = channel.user_limit
        if interaction.user.id == self.author_id:
            if min_limit == 1:
                await interaction.response.send_message(f"User limit cannot be less than {min_limit}", ephemeral=True)
            else:
                await channel.edit(user_limit=channel.user_limit - 1)
                await interaction.response.send_message(f"the user limit of this channel has been decreased to {channel.user_limit}.",ephemeral=True)
        else:
            await interaction.response.send_message(f"You are not allowed to interact with this button!", ephemeral=True)
    @commands.Cog.listener()
    async def on_button_click(interaction):
        if interaction.custom_id == 'increase':
        # Handle increase_limit button click here
            try:
                await interaction.response.defer()
                await interaction.message.edit(view=view)
            except discord.errors.NotFound:
                pass
            except Exception as e:
                print(e)
                await interaction.response.send_message('An error occurred while processing the request.', ephemeral=True)

 

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
                    view = TempVoiceView(author_id=member.id)
                    print(view)
                    message = await channel2.send(f"Hey there, {member.mention}! You can modify your temp channel by clicking on the buttons below.", view=view)

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
