from discord.ext import commands
import discord


class ModeratorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    Moderator Commands
    '''
    #do
    @commands.has_permissions(kick_members=True)
    @commands.command(name='kick')
    async def kick(self, ctx, member: discord.Member, *, reason= None):
        res = await member.kick(reason=reason)
        if reason is None:
            await ctx.send(f'{member} was kicked from the server. Reason: No reasons provided')
        else:
            await ctx.send(f'{member} was kicked from the server. Reason: {reason}')

    @commands.has_permissions(ban_members=True)
    @commands.command(name='ban')
    async def ban(self, ctx, member: discord.Member, *, reason= None):
        res = await member.ban(reason=reason)
        if reason is None:
            await ctx.send(f'{member} was banned from the server. Reason: No reasons provided')
        else:
            await ctx.send(f'{member} was banned from the server. Reason: {reason}')

    @commands.has_permissions(administrator=True)
    @commands.command(name='mute')
    async def mute(self, ctx, member: discord.Member, *, reason= None):
        role = ctx.guild.get_role(754020980183007445)
        res = await member.add_roles(role)
        if reason is None:
            await ctx.send(f'Muted {member}. Reason: No reasons provided')
        else:
            await ctx.send(f'Muted {member}. Reason: {reason}')
    
    @commands.has_permissions(manage_messages=True)
    @commands.command(name='clear',aliases=['cl'])
    async def clear(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f'Deleted {len(deleted)} message(s)', delete_after=1)

    #undo
    @commands.has_permissions(ban_members=True)
    @commands.command(name='pardon',aliases=['unban'])
    async def pardon(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        print(banned_users)
        member_name, member_discriminator = member.split('#')

        for BanEntry in banned_users:
            user = BanEntry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                res = await ctx.guild.unban(user)
                await ctx.send(f'Member {member} was unbanned')

    @commands.has_permissions(administrator=True)
    @commands.command(name='unmute')
    async def unmute(self, ctx, member: discord.Member):
        role = ctx.guild.get_role(754020980183007445)
        res = await member.remove_roles(role)
        await ctx.send(f'{member} has been unmuted')
    
    #server moderation
    @commands.has_permissions(administrator=True)
    @commands.group(name='role')
    async def role(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid role command passed...')

    '''
    Role Give/Take
    '''
    @commands.has_permissions(administrator=True)
    @role.command(name='give',aliases=['->','=>'])
    async def give(self, ctx, member: discord.Member, *, role_name= None):
        guild_id = ctx.message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
        if role_name is not None:
            role = discord.utils.get(guild.roles, name=role_name)

            if role is not None:
                res = await member.add_roles(role)
                await ctx.send(f'Role "{role}" is added to member: {member}')
            else:
                await ctx.send(f'Role "{role_name}" was not found')

        else:
            await ctx.send('Please make sure you message contains a role name')

    @commands.has_permissions(administrator=True)
    @role.command(name='take', aliases=['<-', '<='])
    async def take(self, ctx, member: discord.Member, *, role_name= None):
        guild_id = ctx.message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
        if role_name is not None:
            role = discord.utils.get(guild.roles, name=role_name)

            if role is not None:
                res = await member.remove_roles(role)
                await ctx.send(f'Role "{role}" is removed from member: {member}')
            else:
                await ctx.send(f'Role "{role_name}" was not found')

        else:
            await ctx.send('Please make sure you message contains a role name')

def setup(bot):
    bot.add_cog(ModeratorCommands(bot))
