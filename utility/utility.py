import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
from revChatGPT.revChatGPT import Chatbot
import random
import asyncio
import time

class UtilityCommands(commands.Cog):
    """Fun commands for members to use!!"""
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.plugin_db.get_partition(self)



    @checks.has_permissions(PermissionLevel.MODERATOR)
    @commands.command()
    async def ranklog(self, ctx, member: discord.Member, gamertag = None, purchase = None , amount = None):
        """
        logs smp ranks
        """
        if member == None:
            await ctx.send_help(ctx.command)
        channel = member.guild.get_channel(960482007379497040) 
        embed = discord.Embed(title="Rank Purchase",
                color=self.bot.main_color,
                description =(
                    f"Discord Tag : {member.mention}\n"
                     f"Discord User ID : {member.id}\n"
                     f"Gamer Tag : {gamertag}\n"
                     f"Amount : {amount}\n"
                     f"Purchase type : {purchase}\n")
                )
        embed.set_footer(text="Utility Plugin v1.10")

        await channel.send(embed=embed) 
        amethyst = "amethyst" 
        ruby = "ruby"
        obsidian = "obsidian"
        carneline = "carneline"
        epidote = "epidote"
        amazonite = "amazonite"
        smprank = member.guild.get_role(1003196550220099654)       
        if purchase == amethyst.lower():                 
            purchase = member.guild.get_role(1034474426902794321)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == ruby.lower():                 
            purchase = member.guild.get_role(1034474078754570353)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == obsidian.lower():                 
            purchase = member.guild.get_role(1034474068998631454)
            await member.add_roles(purchase)
            await member.add_roles(smprank)            
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)            
        elif purchase == epidote.lower():                 
            purchase = member.guild.get_role(1034474059645329481)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == carneline.lower():                 
            purchase = member.guild.get_role(1034473986211467271)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == amazonite.lower():                 
            purchase = member.guild.get_role(1034473906863607889)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)                  
        else:
            embed = discord.Embed(
                    description = (
                       f"Couldn’t add roles to {member.mention} due to incorrect log format!\n"
                       f"Please give them roles manually"))
            await channel.send(embed=embed)
     
    @checks.has_permissions(PermissionLevel.MODERATOR)       
    @commands.command()
    async def say2(self, ctx, *, message):
        """ModMail says what you want it to say."""
        await ctx.message.delete()
        await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))


    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @commands.command()
    async def userid(self, ctx, member: discord.Member = None):
        thread = ctx.thread   
        if member:
            await ctx.send(f"{member.mention}'s ID is {member.id}",delete_after=15)
            await asyncio.sleep(15)
            await ctx.message.delete()
        elif thread == None:
            member = ctx.author
            await ctx.send(f"{member.mention}'s ID is {member.id}",delete_after=15)
            await ctx.message.delete()
        else:
            member = thread.recipient
            await ctx.message.delete()
            await ctx.send(f"{member.mention}'s ID is {member.id}")

    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command()
    async def ip(self, ctx, member:discord.Member = None):
        """
        IP address for Blackclue's SMP server
        """
        if member == None:
            embed = discord.Embed(
               title = "Surviving Sheep SMP IP",
               color=self.bot.error_color,
               description = (f"**Bedrock IP :** play.blackclue.in\n"
                       f"**Port :** 19132\n"
                       f"**Java IP :** java.blackclue.in"))
            await ctx.send(f"{ctx.author.mention}", embed=embed, delete_after=60)
        else:
           embed = discord.Embed(
               title = "Surviving Sheep SMP IP",
               color=self.bot.error_color,
               description = (f"**Bedrock IP :** play.blackclue.in\n"
                       f" **Port :** 19132\n"
                       f" **Java IP :** java.blackclue.in"))
           await ctx.send(f"{member.mention}", embed=embed ,delete_after=60)
        await ctx.message.delete()
 
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command()
    async def vote(self, ctx, member:discord.Member=None):
        if member == None:
            embed = discord.Embed(
               title = "Surviving Sheep SMP Vote Link",
               color = self.bot.error_color,
               description = (f"[Click Here](https://minecraftpocket-servers.com/server/119868/vote/) to vote for smp server!"))
            await ctx.send(f"{ctx.author.mention}\n", embed=embed, delete_after=60)
        else:
            embed = discord.Embed(
               title = "Surviving Sheep SMP Vote Link",
               color = self.bot.error_color,
               description = (f"[Click Here](https://minecraftpocket-servers.com/server/119868/vote/) to vote for smp server!"))
            await ctx.send(f"{member.mention}\n", embed=embed, delete_after=60)
        await ctx.message.delete()

      
    @commands.command()
    async def _active_members(self, ctx, chat, member1: discord.Member = None, member2 : discord.Member = None):
        if member1 is not None:
            await ctx.send(f"{member1.mention}, {member2.mention} mention a member") 
        else:
            await ctx.send(f"{ctx.author.mention}, setting up list!")
        return

    @commands.command()
    async def nuke(self, message):
        if message.author.id == 667378631336525824:
            await message.send("are you sure you want to nuke this server?")
            time.sleep(3)
            await message.send("nuking this server in 5 seconds")
            time.sleep(5)
            await message.send("deleting channels and roles")
        else:
            await message.send("Lol")
 
    @commands.command(aliases=['ask','chat'])
    async def gpt(self, ctx: commands.context, *, argument):
        chatbot = Chatbot({"session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..mVetDh10BwHgRuIF.jX-Kn7bc4tmShPgn4iv_bNFjvSeLqZrPNsjGWdRO7onz3Nj2nZa9lGRjs9iBp_rzOk2tIthVq1elrka32G32TzcvJ6ldVDDfUTzINmSRPcMzCY-boyIfq9wttv7n2zOb3t00GXqoVH46EVJ4VsrTtHWENmMYvOyvzRoGSRGm79TalmVvPM4KG0DXSsE_88LmTaIbWXK2iM7IITtvWMT5nJ5nSD6-BuPlUVC_ouPpEnO8vTYx8azoV_dRiprdLywGqTV9iOEm18ESRBVOuPq7lLR-db3v0Gwo2Dbml1MqxOjdgF5D6_5Ky1RpztVevE19jC3W1zNOTr-4x37jNmf7aXuRmD2iiixQ5WHK2gbKt-712YhWKFbGM1Rf29vJc1n2zaNukEbZAgUK4_Jk1atelsVcuf_5YwqvjNqcqN_GUBF5eDf2mYhtv5YkOrdo24x4ux-fzI39KrC9W8VAOFN0XMOqpiN8S0TdUEHKhGNspGRFfsubykDhR1QfJh1ZhlvVSbLjgGTFfch1HpyCOSIC5Dzi17Tq8dPBN-EDkpNAS4Amu_C3312qpmohRlofRTokjC_TCQcNA-5jmaj0Iar_KMi-t5LwtXg9nWJKIxbxjKj4NaXPgnj9Cmewk_QypETJz8foSe6wkf2h0JFIlpnfy-ovOGgQ1GVE3lW_pYBe8ovqcrAcYQPtBapm7JspRkA6MSKeXdcTRdHCirhVMiuYhyPLZpIcPWILnY5ZBgYHE7PV0gjTNjjp-8yNCXwHa1nnzpT0JqakaAo5L2dWyiuxSYmXL4QjKPwBnXtsLSvIUeQ1iUxrEkuArWclJGC-V_4RaLhwyCgKTiP_oTK1N8x_Xlmm77MPIvkeLUN4s2HPda9PSjjTt0rrD0rksNzrIoP3RsWdnBIW6yVEUSbMIu5wFdsEgceX1JA5EaNJbRiG4RzW1vLBhhxvXSk-S12vVkdB7ww8ihIrbhGWmi2oD7rosNezVn-3QG-DZUbAkZ0ZH0hqTHuLuLlD-kEfnrE0K3QWRGiE4ykjDaqY2WI2Do__KXRqJWb5KrGY0zTmmHFIFaDkIESitITXEu-TgN_wueWtps1EJaAdh6MZBhyz974PcWHdW9pTFfn7lB1hIYBYIXKcQuYDNoLtUxUC0Z8Sbkt-UWTGDn7ZO-rg_lJ4kmMIVZd5-Vj5KegEvsX4rwiGqgT660IL9FNTb_PVZxqcTLCXLDl7ZXTbnzqrtzffIhhWRxOwAnks_auW2g0juW5XWz2mmvB0SB6T5tZN7ttTH49XOGrRyNg8nrqjZ7CI-hiHz886Ro7XmjtP1M6_BRCmWYVGJotREnfhON2PBbD7nM0igfCPvqjSu2QSvqely73vaGnmTEwqpt0CQNAsg6m3exJzH3IvO4n6Us2pKwtnqyesKmvDaXwYePCIimmPc1wcIP8qPb4lY3KiMTm49UTkMCH6yYKxbgMPOMpbFiz8ivagasVMgwhwEiEwWS9Ag9xRinTJdXRr94AUxb1YHi-3zAa6zIgoZFJogw-gh7ewniEDMHM8EABKrFSVeiD-n07WiKeamX0JzJmA6zMg8NfGAXGwz4W3lju42lIjb-7nrXbPiwYDpmL09n7YUT08c3l03cjFHxRwb4vsGz-Xge9w_1zksPkxU8xNZ2uEmhvAElv9SAy9EzKTaRELZDwMuMdwmzzyeJZvlXomtiDAYG8jwZfyCgYeEAHgg9RvtgQPXaWpGKAy00-sN5uYW_yHFB-lJWwJ6QT-dMQ5liw8ZwXBa0lZ9v7rdlR-aT0IGUKTuAuecZ2VaIIJfo4k3xyIKezpqCuEqK8i5Bchc5Lpc4AlPXdVgyru7jRZx7XsVaHrCSw6a2bT6RmcDmEsy6zHnekclluuBYFKADKE7DXqrSgddSZuq-4uC0K1wr_pnd8gcDkyTdvGWfDqef-2DF5j-7fcpkPmaJbjiX445kDskohh8zB5Xorv7_Co6bVklVJoECFDMe9miT6O_ZzlkG4k927J0OHVBr8UhcL2-wgf4Wsr_s-8knXrI3tr7x-khBVM3hK9nJ9iHhu8g6m3o1DvGtqni_KsHsHQIkdbg_FH_aG00h9PNSnHWlT260J2tB1HToXs_uc3yiIHivR4jxV4UruolvBrxW9uTgOpm2b2F4ycA31bJSkHxt5wbNDNQIFT5hanv3rclWq-OI7JFP1c3QzjUpePFR7G_4NEQa7_CbDWyfxARvUz9_KN-09aBAtqaxkufSPszNQyc9dt-aV1YmmyRGbGI4Razb8XuyW-uiYjC9m5tmFK3v-ZLB410S4.kQCJmPugx_T4B4IE9SG5wQ"}, conversation_id=None, parent_id=None)
        response = chatbot.ask(argument, conversation_id=None, parent_id=None) 
        await ctx.reply(response['message'])


async def setup(bot):
    await bot.add_cog(UtilityCommands(bot))
