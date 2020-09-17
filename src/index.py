import json
import os

import discord
from discord.ext import commands
#env
from dotenv import load_dotenv
#color
from termcolor import colored

load_dotenv()

#define client
client = commands.Bot(command_prefix = os.getenv("PREFIX"))
#removes default help command
client.remove_command('help')

#get json data
with open('src/config.json') as f:
	configData = json.load(f)
print(colored('[INFO] loaded config.json', 'yellow'))


@client.event
async def on_ready():
    print(colored(f'[INFO] Logged in as {client.user}', 'green'))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Code"))

# @commands.has_permissions(administrator=True)
# @client.command(name='setup')
# async def setup_role(ctx):
#     await ctx.message.delete()

#     lang_react = await ctx.send(
#         '''
#         > ```md
#         > + Pick Your Programming Language
#         > ```
#         > __Back-end__:
#         > <:c_:752228123541635107> - **C**
#         > <:cpp:752227520774144090> - **C++**
#         > <:csharp:752229132963676210> - **Cs**
#         > <:java:752227672007901265> - **Java**
#         > <:go:752228833234780321> - **Golang**
#         > <:r_:752228334657863680> - **R**
#         > <:python:752227586490499185> - **Python**
#         > <:rust:752228257738391652> - **Rust**
#         > 
#         > 
#         > __Front-end__:
#         > <:html:752227918121402378> - **HTML** [Hyper Text Markup Language]
#         > <:css:752227961146703982> - **CSS** [Cascading Style Sheet]
#         > <:sass:755553406281711646> - **Sass** [Pre-processor]
#         > <:js:752227730204000287> - **JavaScript**
#         > <:ts:752228025700974622> - **TypeScript**
#         '''
#     )

#     frame_react = await ctx.send(
#         '''
#         > ```md
#         > + Pick Your Framework
#         > ```
#         > <:vuejs:752228572961439897> - **Vue.js**
#         > <:reactjs:752228520716926997> - **React.js**
#         > 
#         > <:sprboot:754128793098125413> - **Spring Boot**
#         > <:dpy:754123295485591582> - **Discord.py**
#         > <:djs:754123017495380029> - **Discord.js**
#         '''
#     )

#     lib_react = await ctx.send(
#         '''
#         > ```md
#         > + Pick Your Libraries
#         > ```
#         > <:nodejs:752228422037667961> - **Node.js/Deno**
#         > <:jquery:755553392276799640> - **jQuery**
#         '''
#     )

#     devOps_react = await ctx.send(
#         '''
#         > ```md
#         > + Pick Your DevOps
#         > ```
#         > <:docker:754125649450631190> - **Docker**
#         > <:kubernetes:755507301091246271> - **Kubernetes**
#         > <:git:755560866233188435> - **Git**
#         '''
#     )

#     roleCate = [
#         lang_react,
#         frame_react,
#         lib_react,
#         devOps_react
#     ]
    
#     count = 0
#     for i in configData['roleEmojis']:
#         for emo in configData['roleEmojis'][i]:
#             await roleCate[count].add_reaction(emo)
#         count += 1
    
#     await ctx.author.send('Role Reaction Setup Complete, no error occurs')

@client.command(name='source',aliases=['src','srcb','srcbin'])
async def get_srclink(ctx):
    await ctx.send('''
    Snippets That's more than 1024 characters long can be published in here to share
    https://sourceb.in
    ''')


# @client.command(name='vanish', aliases=[])
# async def get_srclink(ctx):
#     await ctx.author.kick(reason="no reasons provided")
@client.command(name='update')
async def update_role(ctx, member: discord.Member = None):
    if member is not None:
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
    else:
        roles = [
            (ctx.guild.get_role(754103452287631390)),
            (ctx.guild.get_role(754103075228090441)),
            (ctx.guild.get_role(754102852011425882)),
            (ctx.guild.get_role(754102954247585843)),
            (ctx.guild.get_role(755503235409641504)),
            (ctx.guild.get_role(755503001749422152)),
        ]
        for role in roles:
            await ctx.author.add_roles(role)

@commands.has_permissions(administrator=True)
@client.command(name='announce',aliases=['anno'])
async def announce(ctx, channel_id: int, *args):
    channel = client.get_channel(channel_id)
    
    await channel.send(" ".join(args))
    await ctx.message.delete()

@client.command(name='invite', aliases=['inv', 'inv-link', 'invitation-link', 'invitation'])
async def get_invlink(ctx):
    await ctx.send('''
    Copy this link to invite others!
    https://discord.gg/bxrYFN9
    ''')

for ext in configData['cogs']:
    try:
        print(colored(f'[INFO] loaded Cog "{ext}"','yellow'))
        client.load_extension(ext)
    except AttributeError:
        print(colored(f'[ERROR] Failed to load Cog {ext}','red'))
        
        
client.run(os.getenv("TOKEN"))

