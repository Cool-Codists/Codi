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
            title=ctx.guild.name,
            description='-----------',
            color=0xf92672,
            timestamp=datetime.datetime.utcnow()
        )

        statuses = [
            len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),
        ]

        fields = [
            ("Region", ctx.guild.region, True),
            ("ID", ctx.guild.id, True),
            ("Owner", ctx.guild.owner, False),
            ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
            ("Member Count", ctx.guild.member_count, True),
            ("Member Statuses",
             f":green_circle: {statuses[0]} :yellow_circle: {statuses[1]} :red_circle: {statuses[2]} :white_circle: {statuses[3]}", True),
            ("Channel Count", len(ctx.guild.channels), False),
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
            ("Created at:", member.created_at.strftime("%d/%m/%Y"), True),
            ("Joined at:", member.joined_at.strftime("%d/%m/%Y"), True),
            # ("Top Role:", member.top_role.mention, False),
        ]

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        for name, value, inline in fields:
            embed.add_field(name = name, value = value, inline = inline)

        await ctx.send(embed=embed)

    @commands.command(name='avatar')
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=discord.Color(0xffff),
            title=f"{member.name}'s Avatar"
        )
        embed.set_image(url=f"{member.avatar_url}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoCommands(bot))
