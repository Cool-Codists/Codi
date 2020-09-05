from discord.ext import commands


class InfoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Info Commands
    '''
    @commands.command(name='serverinfo')
    async def serverinfo(self, ctx):
        await ctx.send('serverinfo')

    @commands.command(name='userinfo')
    async def userinfo(self, ctx):
        await ctx.send('userinfo')

    @commands.command(name='avatar')
    async def avatar(self, ctx):
        await ctx.send('user avatar')


def setup(bot):
    bot.add_cog(InfoCommands(bot))
