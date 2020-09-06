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

    #volume control
    @commands.command(name='volume')
    async def volume(self, ctx, message):
        member = ctx.author

        try:
            self.volume = int(message)
            if(self.volume > 100 or self.volume < 0):
                await ctx.send("Please enter a valid number between 1-100")
            else:
                changeVolumeTo(self.volume)
                await ctx.send(f'volume changed to {self.volume}%')

        except ValueError:
            print("[ERROR] Can't convert string into int")
            await ctx.send(f"{member.mention} Please enter a valid value")
    
    # @volume.command()
    # async def higher_volume(self, ctx):
    #     await ctx.send('volume goes higher')
    
    # @volume.command()
    # async def lower_volume(self, ctx):
    #     await ctx.send('volume goes lower')
        
    
    #queue
    @commands.command(name='queue')
    async def queue(self, ctx):
        await ctx.send('queue displayed')

def changeVolumeTo(volume):
    return volume

def setup(bot):
    bot.add_cog(MusicCommands(bot))
