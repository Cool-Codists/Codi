from discord.ext import commands


class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Music Commands
    '''
    #play status
    @commands.command(name='play')
    async def play(self, ctx):
        await ctx.send('played music')
    
    @commands.command(name='pause')
    async def pause(self, ctx):
        await ctx.send('music paused')
    
    @commands.command(name='stop')
    async def stop(self, ctx):
        await ctx.send('music stopped')
    
    @commands.command(name='skip')
    async def skip(self, ctx):
        await ctx.send('skipped current song')
    
    #queue
    @commands.command(name='queue')
    async def queue(self, ctx):
        await ctx.send('queue displayed')

def setup(bot):
    bot.add_cog(MusicCommands(bot))
