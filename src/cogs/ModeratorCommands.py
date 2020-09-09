from discord.ext import commands


class ModeratorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Moderator Commands
    '''
    #do
    @commands.has_permissions(administrator=True)
    @commands.command(name='kick')
    async def kick(self, ctx):
        await ctx.send('kicked')

    @commands.command(name='ban')
    async def ban(self, ctx):
        await ctx.send('banned')

    @commands.command(name='mute')
    async def mute(self, ctx):
        await ctx.send('muted')
    
    @commands.command(name='clear',aliases=['cl'])
    async def clear(self, ctx):
        await ctx.send('cleared')

    #undo
    @commands.command(name='pardon',aliases=['unban'])
    async def pardon(self, ctx):
        await ctx.send('unbanned')

    @commands.command(name='unmute')
    async def unmute(self, ctx):
        await ctx.send('unmuted')
    
    #server moderation
    @commands.group(name='role')
    async def role(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid role command passed...')

    @role.command(name='give',aliases=['->','=>'])
    async def give(self, ctx):
        await ctx.send('role gave')

    @role.command(name='take', aliases=['<-', '<='])
    async def take(self, ctx):
        await ctx.send('role taken')


def setup(bot):
    bot.add_cog(ModeratorCommands(bot))
