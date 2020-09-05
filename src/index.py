import discord
import os
import json
from discord.ext import commands

#env
from dotenv import load_dotenv
load_dotenv()

#define client
client = commands.Bot(command_prefix = os.getenv("PREFIX"))
#removes default help command
client.remove_command('help')

#get json data
with open('config.json') as f:
	data = json.load(f)


@client.event
async def on_ready():
    print(f'[INFO] Logged in as {client.user}')

@client.command(name='test')
async def test(ctx):
    await ctx.send('success!')

for ext in data['cogs']:
    client.load_extension(ext)

# client.load_extension('cogs.CommandEvents')
# client.load_extension('cogs.HelpCommands')
# client.load_extension('cogs.DatabaseCommands')
# client.load_extension('cogs.InfoCommands')
# client.load_extension('cogs.ModeratorCommands')
# client.load_extension('cogs.MusicCommands')
        
client.run(os.getenv("TOKEN"))
