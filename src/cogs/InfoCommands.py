from discord.ext import commands
from discord import Embed
import discord

import datetime


class InfoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Info Commands
    '''
    @commands.command(name='serverinfo', aliases=['server-info', 'info-server', 'server'])
    async def serverinfo(self, ctx):
        embed = Embed(
            title="Server Info",
            description="------------",
            color=0xf92672,
            timestamp=datetime.datetime.utcnow()
        )

        statuses = [
            len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),
        ]

        regions = {
            "brazil": f"Brazil :flag_br:",
            "europe": f"Europe :flag_eu:",
            "hongkong": f"Hong Kong :flag_hk:",
            "india": f"India :flag_in:",
            "japan": f"Japan :flag_jp:",
            "russia": f"Russia :flag_ru:",
            "singapore": f"Singapore :flag_sg:",
            "southafrica": f"South Africa :flag_za:",
            "sydney": f"Sydney :flag_hm:",
            "us-central": f"US Central :flag_us:",
            "us-east": f"US East :flag_us:",
            "us-south": f"US South :flag_us:",
            "us-west": f"US West :flag_us:"
        }

        ver_levels = {
            "none": f"None\nNo criteria set.",
            "low": f"Low\nMember must have a verified email on their Discord account.",
            "medium": f"Medium\nMember must have a verified email and be registered on Discord for more than five minutes",
            "high": f"High\nMember must have a verified email, be registered on Discord for more than five minutes, and be a member of the guild itself for more than ten minutes.",
        }
        print(str(ctx.guild.region))
        reg = regions[str(ctx.guild.region)]
        ver = ver_levels[str(ctx.guild.verification_level)]

        fields = [
            ("<:announcements:762029375716851732> Name(ID):",
             f"**{ctx.guild.name}**(`{ctx.guild.id}`)", True),
            (":date: Created at:", ctx.guild.created_at.strftime("%m/%d/%Y %H:%M:%S"), False),
            
            ("<:owner:762029375783698462> Owner:", 
             ctx.guild.owner, True),
            ("<:globe:762029375792087080> Region:", reg, True),

            (
                "<:members:762029614117683210> Member:",
                f'''Total Members: **{ctx.guild.member_count}**
                <:online:755612534631039056> {statuses[0]} <:idle:755612534710599731> {statuses[1]} <:dnd:755612534647554048> {statuses[2]} <:offline:755612534660268083> {statuses[3]}
                ''',
                False
            ),
            # ("<:boost:762029375776227358> Boost Level:", ctx.guild.premium_tier, True),
            

            (":lock: Verification Level:", f'{ver}\n', False),

            (
                "<:role:762029375805194290> Roles:", 
                f'''
                → Total Roles: **{len(ctx.guild.roles)}**
                → Highest Role: <@&{ctx.guild.roles[len(ctx.guild.roles)-1].id}>

                ''',
                False
            ),

            (
                "<:channel:762029375859589120> Channels:", 
                f'''
                → Total Channels: **{len(ctx.guild.channels)}**
                → Categories: **{len(ctx.guild.categories)}**
                → Text Channels: **{len(ctx.guild.text_channels)}**
                → Voice Channels: **{len(ctx.guild.voice_channels)}**
                → AFK Channel: **{ctx.guild.afk_channel}**

                ''', 
                False
            ),
            (
                ":orange_book: Emojis",
                f'''
                → Total Emojis: **{len(ctx.guild.emojis)}/{ctx.guild.emoji_limit}**
                ''',
                False
            )
        ]

        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command(name='whois', aliases=['userinfo', 'getinfo'])
    async def whois(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = Embed(colour=discord.Color(0xFD971F),
                      timestamp=ctx.message.created_at)

        fields = [
            ("ID:", member.id, True),
            ("User name:", member.display_name, False),
            ("Created at:", member.created_at.strftime("%m/%d/%Y"), True),
            ("Joined at:", member.joined_at.strftime("%m/%d/%Y"), True),
            # ("Top Role:", member.top_role.mention, False),
        ]

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        for name, value, inline in fields:
            embed.add_field(name = name, value = value, inline = inline)

        await ctx.send(embed=embed)

    @commands.command(name='avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        if member is not None:
            embed = discord.Embed(
                color=discord.Color(0xffff),
                title=f"{member.name}'s Avatar"
            )
            embed.set_image(url=f"{member.avatar_url}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color=discord.Color(0xffff),
                title=f"{ctx.author.name}'s Avatar"
            )
            embed.set_image(url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embed)
    
    @commands.command(name='languages',aliases=['langs','prog-langs','programming-languages'])
    async def countMemberLang(self, ctx):
        pass

def setup(bot):
    bot.add_cog(InfoCommands(bot))
