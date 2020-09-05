from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    '''
    Help Commands
    '''
    @commands.group(name='help', invoke_without_command=True)
    async def help(self, ctx):
        await ctx.send('no, do it your self')

    @help.command(name='music')
    async def help_misc(self, ctx):
        await ctx.send('this is music help')

    @help.command(name='moderator')
    async def help_mod(self, ctx):
        await ctx.send('this is moderator help')

    @help.command(name='code')
    async def help_code(self, ctx):
        await ctx.send('this is code help')


def setup(bot):
    bot.add_cog(HelpCommands(bot))
