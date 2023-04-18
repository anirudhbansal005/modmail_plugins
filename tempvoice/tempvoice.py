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
        self.author_id = None

    def set_author_id(self, author_id):
        self.author_id = author_id
        
    @discord.ui.button(label="Increase User Limit", custom_id="increase")
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

    @discord.ui.button(label="Hide Channel", custom_id="persistent_view:hide")
    async def hide(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        perms = channel.permissions_for(interaction.guild.default_role)
        message = interaction.original_response()
        button = self.hide
        if interaction.user.id == self.author_id:
            if perms.view_channel:
                await channel.set_permissions(interaction.guild.default_role, view_channel=False)
                await interaction.response.send_message("Your channel is now hidden")
                button.style = discord.ButtonStyle.red    
                await interaction.response.edit_message(view=self)   
            else:
                await interaction.response.send_message(f"{channel.mention} is already hidden.", ephemeral=True)
        else:
            await interaction.response.send_message("You are not allowed to interact with this button!", ephemeral=True)

    @discord.ui.button(label="Unhide Channel", custom_id="persistent_view:unhide")
    async def unhide(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        default_role = interaction.guild.default_role
        perms = channel.permissions_for(default_role)
        hide_button = self.hide
        if interaction.user.id == self.author_id:
            if perms.view_channel:
                await interaction.response.send_message(f"{channel.mention} is already visible to everyone.", ephemeral=True)
            else:
                await channel.set_permissions(default_role, view_channel=True)
                await interaction.response.send_message("Your channel is now visible")
        else:
            await interaction.response.send_message("You are not allowed to interact with this button!", ephemeral=True)

    @discord.ui.button(label="Kick Member")
    async def kick_member(self, button: discord.ui.Button, interaction: discord.Interaction):
        members = self.members
        if not members:
            await interaction.response.send_message("There are no members in the voice channel to kick.", ephemeral=True)
            return

        dropdown = MemberDropdown(members)
        await interaction.response.send_message("Select a member to disconnect", view=dropdown)

class MemberDropdown(discord.ui.Select):
    def __init__(self, members):
        options = []
        for member in members:
            options.append(discord.SelectOption(label=member.name, value=str(member.id)))
        super().__init__(placeholder="Select a member to kick", options=options, timeout=30)

    async def callback(self, interaction: discord.Interaction):
        member_id = int(self.values[0])
        member = interaction.guild.get_member(member_id)
        if member is not None and member.voice is not None:
            await member.move_to(None)
            await interaction.response.send_message(f"Successfully kicked {member.name} from the voice channel!", ephemeral=True)
        else:
            await interaction.response.send_message("Unable to kick the selected member. They may not be connected to a voice channel.", ephemeral=True)


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
                    

                # Send message to the created channel
                    view = TempVoiceView()
                    view.set_author_id(member.id)
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
