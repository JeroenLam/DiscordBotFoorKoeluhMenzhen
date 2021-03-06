from BaseCommand import *
import sys
import os
sys.path.append('Support')
from VoiceCommands import *

class SoundBoardCommand(BaseCommand):
    async def execute(self, message):
        # Tokenize the input string
        argv = message.content.split(' ')

        # Send a list of all files when the first term is list
        if argv[1] == 'list':
            for root, dirs, files in os.walk('SoundBoard'):
                retMessage = ''
                for name in files:
                    retMessage += name + '\n'
            await message.author.send(retMessage) 
        else:
            await sendLocalMP3(message, 'SoundBoard/' + argv[1] + '.mp3')

    async def help(self):
        return 'sb <name | list> : Plays the audio file <name>.mp3. Will return a list of all available files when used with list.'