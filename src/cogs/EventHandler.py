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
    "kubernetes": 755507321710444624,
    "git": 755560711924744273,
    "sass": 755553221040144404,
    "jquery": 755553426062180359
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
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

        print(payload.message_id)

        if payload.message_id == 753057633132609536:
            print(payload.emoji.name)
            if payload.emoji.name == '✅':
                role = member.guild.get_role(752247003819409450)
                print(role)
                await member.add_roles(role)
            else:
                pass

        if payload.message_id in role_msgid:
            role = member.guild.get_role(roles[payload.emoji.name])
            print(role, member)
            if member is not None:
                print(f'Added role: {role} to member {member}')
                await member.add_roles(role)
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

        if payload.message_id == 753057633132609536:
            if payload.emoji.name == '✅':
                role = member.guild.get_role(752247003819409450)
                await member.remove_roles(role)
            else:
                pass
        if payload.message_id in role_msgid:
            role = member.guild.get_role(roles[payload.emoji.name])
            print(role, member)
            if member is not None:
                print(f'Removed role: {role} from member {member}')
                await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = member.guild.name
        roles = [
            (member.guild.get_role(754103452287631390)),
            (member.guild.get_role(754103075228090441)),
            (member.guild.get_role(754102852011425882)),
            (member.guild.get_role(754102954247585843)),
            (member.guild.get_role(755503235409641504)),
            (member.guild.get_role(755503001749422152)),
        ]
        for role in roles:
            await member.add_roles(role)

        embed = discord.Embed(
            color=discord.Color(random.randint(0x000000, 0xFFFFFF)),
            title='Welcome Message',
            description=f'Welcome to {server} {member.mention}!'
        )

        channel = self.bot.get_channel(751524642069676187)
        await member.send(embed=embed)
        await channel.send(f'Welcome {member.mention}! Please make sure that you read the <#751541905363304490> and <#751537346540863620>!')


def setup(bot):
    bot.add_cog(EventHandler(bot))
