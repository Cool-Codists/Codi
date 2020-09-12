from discord.ext import commands
import discord

import random
import os
import json

#env
from dotenv import load_dotenv
load_dotenv()

#get json data
with open('src/config.json') as f:
	configData = json.load(f)

role_msgid = configData["roleReactMsg"]
roles = {
    "c_": 751526041809584168,
    "cpp": 751525042537627748,
    "csharp": 752228975127953484,
    "css": 752226862796898417,
    "html": 751525079241982033,
    "js": 751525158816317572,
    "ts": 751525213170171925,
    "vuejs": 752227111414268015,
    "reactjs": 752227077595332694,
    "nodejs": 752227035899887657,
    "go": 751525988973674556,
    "r_": 751526019025862867,
    "python": 751525058442297385,
    "java": 751525011017171041,
    "rust": 751525960968306730,
    "docker": 754125899628019802,
    "sprboot": 754129278672699473,
    "djs": 754125892120215597,
    "dpy": 754126016070287360,
}

class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Reaction Handler
    '''
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        pass

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.message_id)
        if payload.message_id in role_msgid:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            role = member.guild.get_role(roles[payload.emoji.name])
            print(role, member)
            if member is not None:
                print(f'Added role: {role} to member {member}')
                await member.add_roles(role)
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id in role_msgid:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            role = member.guild.get_role(roles[payload.emoji.name])
            print(role, member)
            if member is not None:
                print(f'Removed role: {role} from member {member}')
                await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = member.guild.name
        roles = [
            (member.guild.get_role(752247003819409450)),
            (member.guild.get_role(754103452287631390)),
            (member.guild.get_role(754103075228090441)),
            (member.guild.get_role(754102852011425882)),
            (member.guild.get_role(754102954247585843)),
        ]
        for role in roles:
            await member.add_roles(role)

        embed = discord.Embed(
            color=discord.Color(random.randint(0x000000, 0xFFFFFF)),
            title='Welcome Message',
            description=f'Welcome to {server} {member.mention}!'
        )
        await member.send(embed=embed)
        await ctx.send(f'Welcome {member}! Please make sure that you read the server rules and pick your roles!')


def setup(bot):
    bot.add_cog(EventHandler(bot))
