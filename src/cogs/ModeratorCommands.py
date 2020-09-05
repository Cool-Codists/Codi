from discord.ext import commands


class ModeratorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Moderator Commands
    '''
    #do
    @commands.command(name='kick')
    async def kick(self, ctx):
        await ctx.send('kicked')

    @commands.command(name='ban')
    async def ban(self, ctx):
        await ctx.send('banned')

    @commands.command(name='mute')
    async def mute(self, ctx):
        await ctx.send('muted')
    
    @commands.command(name='clear')
    async def clear(self, ctx):
        await ctx.send('cleared')

    #undo
    @commands.command(name='pardon')
    async def pardon(self, ctx):
        await ctx.send('unbanned')

    @commands.command(name='unmute')
    async def unmute(self, ctx):
        await ctx.send('unmuted')


def setup(bot):
    bot.add_cog(ModeratorCommands(bot))
