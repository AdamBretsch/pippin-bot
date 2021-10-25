from commands.base_command  import BaseCommand
from utils                  import get_emoji
from random                 import randint
from discord                import FFmpegPCMAudio
from time                   import sleep

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Meow(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Make pippin say hello"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, arguments, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        
        #ctx = arguments[1]
        #channel = ctx.author.voice.channel
        #vc = await channel.connect()
        #await ctx.send('Started playing: something')
        #vc.play(discord.FFmpegPCMAudio('~/pippin_bot/sounds/p_meow1.mp3'), after=lambda e: print('done', e))
        voice_channel = client.get_channel(782744182497738812)
        print("Voice channel got")
        voice_client = await voice_channel.connect()
        print("Voice client connected")
        voice_client.play(FFmpegPCMAudio('./sounds/p_meow1.mp3'), after=lambda e: await voice_client)
        msg = "Meow" + get_emoji(":cat:")
        await message.channel.send(msg)
        
        
