import discord
import os
import json
from discord.ext import commands

#color
from termcolor import colored

#env
from dotenv import load_dotenv
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
#     role_react = await ctx.send(
#         '''
#         > ```md
#         > + Pick Your Programming Language
#         > ```
#         > __Back-end__:
#         > <:c_:752228123541635107> - **C**
#         > <:cpp:752227520774144090> - **C++**
#         > <:csharp:752229132963676210> - **C#**
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
#         > <:nodejs:752228422037667961> - **Node.js/Deno**
#         > 
#         > <:sprboot:754128793098125413> - **Spring Boot**
#         > <:docker:754125649450631190> - **Docker**
#         > <:dpy:754123295485591582> - **Discord.py**
#         > <:djs:754123017495380029> - **Discord.js**
#         '''
#     )
#     for emo in configData['roleEmoji']:
#         await role_react.add_reaction(emo)
    
#     for emo in configData['frameEmoji']:
#         await frame_react.add_reaction(emo)

@client.command(name='source',aliases=['src','srcb','srcbin'])
async def get_srclink(ctx):
    await ctx.send('''
    Snippets That's more than 1024 characters long can be published in here to share
    https://sourceb.in
    ''')

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
