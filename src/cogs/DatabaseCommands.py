import os
from termcolor import colored
from hashids import Hashids
import random

from discord.ext import commands
from discord import Embed
import pymongo

# from '../utils' import mongo
MONGO = pymongo.MongoClient(os.getenv("DBPATH"))
db = MONGO.data
snipath = db.code_snippets
# pollpath = db.polls

class DatabaseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Code Snippet Commands
    '''
    @commands.group(name='code')
    async def code(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid code command passed...')

    @code.command(name='new')
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def new(self, ctx, *args):
        if len(args) <= 0:
            return
        title = " ".join(args)
        print(title)
        msg = await ctx.send(f'Adding code snippet, Title: {title}.\nPlease enter your code')
        snippet = await self.bot.wait_for('message', check=check(ctx.author))
        if '```' not in snippet.content:
            await ctx.send('Please enter your code in a code block format!')
        else:
            sid = get_hash('snippet')

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
    @new.error
    async def newsni_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You can't use it yet {ctx.author.mention}, it's still in cooldown.")
        else:
            raise error
        

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
    
    @code.command(name='sol', aliases=['solv','solve'])
    async def solv(self, ctx, *args):
        dat = snipath.find_one({'snid': args[0]})
        author = dat["author"]
        await ctx.send(f'Come here <@{author}>! {ctx.author.mention} had solved your problem!')
    
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
                
                res = snipath.update_one(query, newvalues)
                await ctx.send(f"Snippet id `{args[0]}`'s status had changed to `{args[1]}`")    
            else:
                await ctx.send(f'Please enter a valid status type (solved, not-solved)')
        except IndexError:
            print(colored('[ERROR] {Command.code.set-Status}: No status type entered','red'))
            await ctx.send('Please enter a status type (solved, not-solved)')
    
    '''
    Poll Commands
    '''
    @commands.command(name='poll')
    async def new_poll(self, ctx, *args):
        if len(args) <= 0:
            return

        await ctx.message.delete()
        pollchannel = self.bot.get_channel(755626254371258388)
        pid = get_hash('poll')
        topic = " ".join(args)
        # dat = {
        #     "pid": pid,
        #     "pname": topic,
        #     "pyes": 0,
        #     "pno": 0,
        # }

        embed = Embed(title='New Poll', description='-----------', color=0x66D9EF)
        embed.add_field(name=f"Poll for: \n{topic}", 
        value='''
        React with <:upvote:755615024428351538> for agree

        React with <:downvote:755615024432808067> for disagree
        ''')

        # res = pollpath.insert_one(dat)
        await ctx.author.send(f'Poll {topic} Created')
        poll = await pollchannel.send(embed=embed)
        await poll.add_reaction('<:upvote:755615024428351538>')
        await poll.add_reaction('<:downvote:755615024432808067>')

    @commands.has_permissions(administrator=True)
    @commands.command(name='end-poll')
    async def end_poll(self, ctx, res):
        channel = self.bot.get_channel(755626254371258388)

        await channel.send(f'Poll ended. Result: {res}')
        await ctx.message.delete()
        

'''
functions
'''
def get_hash(type):
    # if type == 'snippet':
    hashids = Hashids(salt='codi', min_length='6')
    rand = random.randint(1, 100000000)
    print(rand)
    sid = hashids.encode(rand)
    if snipath.find_one({"snid": sid}) is not None:
        get_hash(type)
    else:
        return sid
    # elif type == 'poll':
    #     hashids = Hashids(salt='copoll', min_length='6')
    #     rand = random.randint(1, 100000000)
    #     print(rand)
    #     pid = hashids.encode(rand)
    #     if pollpath.find_one({"pid": pid}) is not None:
    #         get_hash(type)
    #     else:
    #         return pid

def check(author):
    def inner_check(message):
        if message.author != author:
            return False
        else:
            return True
    return inner_check

def setup(bot):
    bot.add_cog(DatabaseCommands(bot))
