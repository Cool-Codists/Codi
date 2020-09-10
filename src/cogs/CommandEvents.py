from discord.ext import commands

from termcolor import colored

commands_tally = {}

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    '''
    Command Handler & Error Handler
    '''
    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, commands.CommandNotFound):
            print(colored(f'[ERROR] command {ctx.message.content} was not found','red'))
            return
            
        print(colored(f'[ERROR] command {ctx.command.name} was invoked incorrectly due to reasons below','red'))
        print(err)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command is not None:
            if ctx.command.name in commands_tally:
                commands_tally[ctx.command.name] += 1
            else:
                commands_tally[ctx.command.name] = 1
            print(colored(f'[INFO] command {commands_tally} is being called','yellow'))

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(colored(f'[INFO] command {ctx.command.name} was invoked successfully','green'))

def setup(bot):
    bot.add_cog(CommandEvents(bot))
