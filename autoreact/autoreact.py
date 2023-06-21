import discord
import typing
import asyncio 
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import re

class Autoreact(commands.Cog):
    """
    Autoreact to a message on mention
    """

    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)


  # --------- BLACKLISTING A MEMBER FROM SERVER -------     
#    @commands.Cog.listener()
#    async def on_member_join(self, member):
#       un = 1046370746475229245 # THIS ROLE HAS NO PERMISSIONS IN ANY CHANNEL
#       if member.id == 1050464201916821626:
#            await member.add_roles(member.guild.get_role(un))
#        elif member.id == 836598836449116220:
#            await member.add_roles(member.guild.get_role(un))
#        elif member.id == 763023382391554048:
#            await member.add_roles(member.guild.get_role(un))
#        elif member.id == 700238768657006602:
#            await member.add_roles(member.guild.get_role(un))
#        elif member.id == 972889240872566904:
#            await member.add_roles(member.guild.get_role(un))
#        elif member.id == 745996986951663697:
#            await member.add_roles(member.guild.get_role(un))
#        elif member.id == 683869766984794124:
#            await member.add_roles(member.guild.get_role(un))
#        else:
#            return 
  # -------------------------------
#---------- Random shit ----
    @commands.Cog.listener()
    async def on_member_unban(self, guild, user: discord.Member):
        if user.id == 924694719492153444:
            await guild.ban(user, reason="lol 😂")
# ---------
    @commands.Cog.listener()
    async def on_message_edit(self, message, before, after):
         if message.guild is not None:
         verified = message.guild.get_role(906615384969474048)
            rankholder = message.guild.get_role(1003196550220099654
            minecraftstaff = message.guild.get_role(906782010033438802)
            minecraftdev = message.guild.get_role(906781843972567040)
            ytmem = message.guild.get_role(740849706204397598)
            admin = message.guild.get_role(668774420583677983)
            trial = message.guild.get_role(907868778321301545)
            voicemem = message.guild.get_role(938677488438104134)
            chatmem = message.guild.get_role(938677457442205757)
            srvstaff = message.guild.get_role(911126348372774912)
            lv10 = message.guild.get_role(906660899480272936)
            booster = message.guild.get_role(632529654812770325)
            manager = message.guild.get_role(906618549370503168)
            mcm = message.guild.get_role(1021412805808754689)
            lv10 = message.guild.get_role(1034478631017259038)
            lv90 = message.guild.get_role(1051063310071644170)
            sheeps = message.guild.get_role(1034478631017259038)
                                                
        if message.guild is not None:
            if after.content.startswith("# ") or after.content.startswith("## ") or after.content.startswith("### "):
                if srvstaff not in message.author.roles and admin not in message.author.roles and minecraftstaff not in message.author.roles and minecraftdev not in message.author.roles:

    @commands.Cog.listener()
    async def on_message(self, message):
  # --------- Roles ------------ #
        if message.guild is not None:
            sheeps = message.guild.get_role(1034478631017259038)
            lv10 = message.guild.get_role(1034478631017259038)
            lv90 = message.guild.get_role(1051063310071644170)
            mcm = message.guild.get_role(1021412805808754689)
            manager = message.guild.get_role(906618549370503168)
            booster = message.guild.get_role(632529654812770325)
            lv10 = message.guild.get_role(906660899480272936)
            srvstaff = message.guild.get_role(911126348372774912)
            chatmem = message.guild.get_role(938677457442205757)
            voicemem = message.guild.get_role(938677488438104134)
            trial = message.guild.get_role(907868778321301545)
            admin = message.guild.get_role(668774420583677983)
            ytmem = message.guild.get_role(740849706204397598)
            minecraftstaff = message.guild.get_role(906782010033438802)
            minecraftdev = message.guild.get_role(906781843972567040)
            rankholder = message.guild.get_role(1003196550220099654)
            verified = message.guild.get_role(906615384969474048)
   # -------------------
# ------- new markdown block
        if message.guild is not None:
            if message.content.startswith("# ") or message.content.startswith("## ") or message.content.startswith("### "):
                if srvstaff not in message.author.roles and admin not in message.author.roles and minecraftstaff not in message.author.roles and minecraftdev not in message.author.roles:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention}, New Markdown Feature Is Not Allowed Here!", delete_after=15) 
            elif re.search(r'.*\n# .*', message.content) or re.search(r'.*\n## .*', message.content) or re.search(r'.*\n### .*', message.content):
                if srvstaff not in message.author.roles and admin not in message.author.roles and minecraftstaff not in message.author.roles and minecraftdev not in message.author.roles:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention}, New Markdown Feature Is Not Allowed Here!", delete_after=15) 
        #        else:
               #     pass
 
  #--------- Auto React --------

        if message.author.bot:
            return
       # if "axat ke sukhe gote" in message.content.lower():
      #      await message.add_reaction("<axat_ka_gota_2:947537465000996944>")
      #      await message.add_reaction("<axat_ka_gota_1:947537433967345694>")
       #     await asyncio.sleep(0.5)
        if "ohio" in message.content.lower():
            await message.add_reaction("<AXHA:1006778596695744593>")
            await asyncio.sleep(0.5)
        if "643848345974210570" in message.content:
            await message.add_reaction("<bc_u_attack:702988306140626975>")
            await asyncio.sleep(0.5)
        if "667378631336525824" in message.content:
            await message.add_reaction("<emoji_21:1033650320636641310>")
            await message.add_reaction("<emoji_22:1033650337053167646>")
            await asyncio.sleep(0.5)
        if "735018264651890689" in message.content:
            await message.add_reaction("<emoji_35:1049663858874261545>")
            await asyncio.sleep(0.5)
        if "752152316596977704" in message.content:
            await message.add_reaction("<bc_o_carefree:984809639495479316>")
            await asyncio.sleep(0.5)
        if "chad" in message.content.lower():
            await message.add_reaction("<bc_z_chadmove:976826985546395678>")
            await asyncio.sleep(0.5)
        if "851771484635398175" in message.content:
            await message.add_reaction("<bc_o_worry_foff:979426649470799942>")
            await asyncio.sleep(0.5)
        if "860808338442158130" in message.content:
            await message.add_reaction("<bc_z_CosmicChad:1048907381121224815>") 
            await asyncio.sleep(0.5)
        if "813107139601104917" in message.content: 
            await message.add_reaction("<bc_z_bhaiTuApna:1040891783976075314>")
            await asyncio.sleep(0.5)
        if "789107450942455828" in message.content:
            await message.add_reaction("<emoji_36:1050086330916405268>")
            await asyncio.sleep(0.5)
        if "741567107673751634" in message.content:
            await message.add_reaction("🤡")
            await asyncio.sleep(0.5)
        if "866611673367969842" in message.content:
            await message.add_reaction("<bc_z_m_eating:881809045114200084>")
            await asyncio.sleep(0.5)
        if "458523367444840449" in message.content:
            await message.add_reaction("<bc_l_awhh:905638142349025301>")
            await asyncio.sleep(0.5)
        if "756061138617368608" in message.content:
            await message.add_reaction("<bc_k_DoggeLaugh:687388483920068680>")
            await asyncio.sleep(0.5) 
            return
        if message.guild is not None:
            if message.channel == message.guild.get_channel(1015633367313682502):
                if minecraftstaff not in message.author.roles and srvstaff not in message.author.roles:
                    if "help" in message.content.lower():
                        if "helping" in message.content.lower():
                            return
                        else:
                            await message.reply("Hey there,\nI see you need help related to our SMP Server but we really can't do anything since you haven't told us about your issue yet. We ask you not to spam and kindly tell us your issue and ping staff member only once. They will check it when they get time! Please be patient,\nThanks!")
    # ----_-_----_-_-------------------
    
    # ----- Sticker Permissions --------
        

        if message.guild is not None:
            if message.stickers:
                if lv10 not in message.author.roles and booster not in message.author.roles and srvstaff not in message.author.roles and chatmem not in message.author.roles and voicemem not in message.author.roles and trial not in message.author.roles and admin not in message.author.roles and ytmem not in message.author.roles and minecraftstaff not in message.author.roles and minecraftdev not in message.author.roles and verified not in message.author.roles and rankholder not in message.author.roles:
                    await message.delete()
                else:
                    return
           

   # -------------------------------
        
   #----------- MEDIA DELETION AFTER FEW SECONDS WITH ROLE BYPASS ---------
      #  testrole = message.guild.get_role(873039799777361972) # role from dank memer server
      #  testrole2 = message.guild.get_role(770694204720283718) # role 2
        for a in message.attachments:
            if a.filename.endswith(".png") or a.filename.endswith (".apng") or a.filename.endswith (".jpg") or a.filename.endswith(".jpeg"):
                gc = message.guild.get_channel(906577935874535455)
                if message.channel == gc and admin not in message.author.roles and manager not in message.author.roles:
                    await asyncio.sleep(30)
                    await message.delete()
                else:
                    return
   # ----------------------------

   # ------------ GIF DELETION AFTER A FEW SECONDS WITH ROLE BYPASS -------

        if "tenor.com" in message.content or ".gif" in message.content:
            if lv90 not in message.author.roles and admin not in message.author.roles and manager not in message.author.roles and mcm not in message.author.roles:
                await message.channel.send(f"{message.author.mention} That link is not allowed!", delete_after=10)
                await message.delete()
        if "tenor.com" in message.content or ".gif" in message.content:
            if lv90 in message.author.roles:
                await asyncio.sleep(30)
                await message.delete()
           
 # ------ 4 digit code
        if message.content.isdigit():
            if srvstaff not in message.author.roles and lv10 not in message.author.roles and sheeps not in message.author.roles:
                if len(message.content) == 4:
                    await message.reply("hey, send this code to <@1038148105704583249>")
            else:
                pass

   #--------------- IP

        if message.content.startswith("!ip") or message.content.lower().startswith("ip"):
            embed = discord.Embed(
            title = "Sheeps Minecraft Network IP",
            color=self.bot.error_color,
            description = (f"**Bedrock IP :** play.blackclue.in\n"
            f"**Port :** 19132\n"
            f"**Java IP :** java.blackclue.in"))
            if "ipa" in message.content.lower() or "ipb" in message.content.lower() or "ipc" in message.content.lower() or "ipd" in message.content.lower() or "ipe" in message.content.lower() or "ipf" in message.content.lower() or "ipg" in message.content.lower() or "iph" in message.content.lower() or "ipi" in message.content.lower() or "ipj" in message.content.lower() or "ipk" in message.content.lower() or "ipl" in message.content.lower() or "ipm" in message.content.lower() or "ipn" in message.content.lower() or "ipo" in message.content.lower() or "ipp" in message.content.lower() or "ipq" in message.content.lower() or "ipr" in message.content.lower() or "ips" in message.content.lower() or "ipt" in message.content.lower() or "ipu" in message.content.lower() or "ipv" in message.content.lower() or "ipw" in message.content.lower() or "ipx" in message.content.lower() or "ipy" in message.content.lower() or "ipz" in message.content.lower():
                return
            else:
                if message.reference is None:
                    if message.mentions:
                        user = message.mentions[0]
                        if user:
                            await message.reply(f"{user.mention}", embed=embed ,delete_after=60)
                    else:
                        await message.reply(embed=embed, delete_after=60)
            
   #------------------------- Unban Forms -----                     

        if message.content.startswith("!ban"):
            if message.reference is None:
                # Check if the user has the necessary permissions to ban members
                if any(role.permissions.administrator or role.permissions.ban_members for role in message.author.roles):
                    # Check if the message contains a mention of a user
                    if message.mentions:
                        user = message.mentions[0]
                    else:
                        try:
                            if len(message.content.split(" ")) < 2:
                                raise ValueError
                            user_id = int(message.content.split(" ")[1])
                            user = message.guild.get_member(user_id)
                        except ValueError:
                            return
                    if user:
                        if message.author.top_role.position <= user.top_role.position:
                            await message.add_reaction('❌')
                        else:
                            reason = message.content.split(" ")[2:]
                            reason = " ".join(reason)
                            await user.send(f"You have been banned from the server for the following reason: {reason}\nIf you think this was a mistake, Appeal at - https://forms.gle/tUA9R44tVimMFb8n6 ")
                            confirmation = await message.channel.send(f"{user.mention} has been banned. Reason: {reason}")
                            await confirmation.delete(delay=10)
                    else:
                        await message.add_reaction('❌')
                else:
                    await message.add_reaction('✅')
            else:
                return
        else:
            return

#  ------------- 4 digit code

async def setup(bot):
    await bot.add_cog(Autoreact(bot))
