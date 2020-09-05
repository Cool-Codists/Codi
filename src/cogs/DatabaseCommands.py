from discord.ext import commands


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
    async def new(self, ctx):
        await ctx.send('new code snippets added')

    @code.command(name='get')
    async def get(self, ctx):
        await ctx.send('get code snippets')

    @code.command(name='delete')
    async def delete(self, ctx):
        await ctx.send('successfully deleted code snippet')



def setup(bot):
    bot.add_cog(DatabaseCommands(bot))
