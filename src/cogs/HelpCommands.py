import discord
from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    '''
    Help Commands
    '''
    @commands.group(name='help', invoke_without_command=True)
    async def help(self, ctx):
        helpEmbed = discord.Embed(
            title="Help",
            description="How to use Codi **Properly**",
            color=0xffffff
        )
        fields = [
            ("Bot Prefix", "`$`", False),

            (
                "Info Commands", 
                '''
                `$serverinfo` - Get current server's info
                `$whois [@mention]` - Get the info of the member that's being mentioned
                `$avatar [@mention]` - Get the avatar of the member that's being mentioned
                ''', 
                True
            ),

            (
                "Code Commands", 
                '''
                `$code` - Create and share code snippets with other's in the server

                type `$help code` to know more
                ''', 
                False
            ),

            ("Music Commands", "`$help music`", True),
            ("Moderator Commands", "`$help mod`", True),
        ]
        for name, value, inline in fields:
            helpEmbed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=helpEmbed);

    @help.command(name='music')
    async def help_misc(self, ctx):
        helpMusic = discord.Embed(
            title="Music Commands",
            description="How to use them",
            color=0xf5d1f6
        )
        helpMusic.add_field(
            name="--------",
            value='''
            `$play [video link/video name]` - Play music
            `$pause` - Pause music
            `$stop` - Stop the music from playing(it will clear the queue too, beware)
            `$volume [volume]` - Adjust volume of the music
            `$queue` - Display the current queue of songs
            '''
        )
        await ctx.send(embed=helpMusic)

    @help.command(name='mod')
    async def help_mod(self, ctx):
        helpMod = discord.Embed(
            title="Music Commands",
            description="How to use them",
            color=0xf5d1f6
        )
        helpMod.add_field(
            name="--------",
            value='''
            `$kick [@mention]` - Kick member
            `$ban [@mention]` - Ban member
            `$mute [@mention] <time>` - Mute a member, by default(time not set) will be the time the mod enter unmute
            `$clear [msg count]` - clear a certain amount of messages in a channel
            `$pardon` - Unban a member
            `$unmute` - Unmute a member
            '''
        )
        await ctx.send(embed=helpMod)

    @help.command(name='code')
    async def help_code(self, ctx):
        helpCode = discord.Embed(
            title="Music Commands",
            description="How to use them",
            color=0xf5d1f6
        )
        helpCode.add_field(
            name="--------",
            value='''
            `$code [new/get] [Snippet Id]` - share/view the code snippets
            `$code delete [Snippet Id]` - delete a snippet

            __How to:__
            `$code new [Snippet Title]` - Create a new Code snippets
            `$code get [Snippet Id]` - View the code snippet through a id that's given to the author when the snippet was created
            '''
        )
        await ctx.send(embed=helpCode)


def setup(bot):
    bot.add_cog(HelpCommands(bot))
