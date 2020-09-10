import os
from termcolor import colored
from hashids import Hashids
import random
import pprint

from discord.ext import commands
from discord import Embed
import pymongo

# from '../utils' import mongo
MONGO = pymongo.MongoClient(os.getenv("DBPATH"))
db = MONGO.data
snipath = db.code_snippets

class DatabaseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Database Commands
    '''
    @commands.group(name='code')
    async def code(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid code command passed...')

    @code.command(name='new')
    async def new(self, ctx, *args):
        title = " ".join(args)
        print(title)
        msg = await ctx.send(f'Adding code snippet, Title: {title}.\nPlease enter your code')
        snippet = await self.bot.wait_for('message', check=check(ctx.author))
        if '```' not in snippet.content:
            await ctx.send('Please enter your code in a code block format!')
        else:
            sid = get_hash()

            dat = {
                "snid": sid,
                "snitle": title,
                "solved": False,
                "author": ctx.author.id,
                "content": snippet.content,
            }

            res = snipath.insert_one(dat)

            embed = Embed(title="New Snippet added", discription="share the id to share the code", color=0x0fab91)
            embed.add_field(
                name="------------",
                value=f'''
                Paste to share: `$code get {sid}`

                __**Snippet id:**__ {sid}
                __**Snippet Title:**__ {title}
                __**Code Snippet:**__
                {snippet.content}
                '''
            )

            dm = await ctx.author.send(embed=embed)
            await ctx.send('Successfully added your snippet! Check your DM for snippet id')
        

    @code.command(name='get')
    async def get(self, ctx, *args):
        res = snipath.find_one({"snid": args[0]})
        if res is not None:
            embed = Embed(title=f'Title: {res["snitle"]}', description=f'Solved: {res["solved"]}', color=0xff997e)
            embed.add_field(name="------------",value=res["content"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Can't find the snippet that matches the id: {args[0]}")

    @commands.has_permissions(administrator=True)
    @code.command(name='delete',aliases=['del'])
    async def delete(self, ctx, *args):
        dat = snipath.find_one({"snid":args[0]})
        res = snipath.delete_one(dat)
        if res is not None:
            await ctx.send(f'Snippet with the id: {args[0]} was successfully deleted')
    
    @code.command(name='solve',aliases=['solv'])
    async def solve(self, ctx, *args):
        print(args)
    
    #status
    @code.command(name='set-status', aliases=['set-sta','sta','setSta'])
    async def solve(self, ctx, *args):
        query = {"snid": args[0]}
        try:
            if args[1] == 'solved' or args[1] == 'not-solved':
                if args[1] == 'solved':
                    newvalues = {"$set": {"solved": True}}
                elif args[1] == 'not-solved':
                    newvalues = {"$set": {"solved": False}}
                
                await ctx.send(f"Snippet id `{args[0]}`'s status had changed to `{args[1]}`")    
            else:
                await ctx.send(f'Please enter a valid status type (solved, not-solved)')
        except IndexError:
            print(colored('[ERROR] {Command.code.set-Status}: No status type entered','red'))
            await ctx.send('Please enter a status type (solved, not-solved)')

'''
functions
'''
def get_hash():
    hashids = Hashids(salt='codi', min_length='6')
    rand = random.randint(1, 100000000)
    print(rand)
    sid = hashids.encode(rand)
    if snipath.find_one({"snid": sid}) is not None:
        get_hash()
    else:
        return sid

def check(author):
    def inner_check(message):
        if message.author != author:
            return False
        else:
            return True
    return inner_check

def setup(bot):
    bot.add_cog(DatabaseCommands(bot))
