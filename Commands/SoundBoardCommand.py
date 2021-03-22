from BaseCommand import *
import os
from VoiceCommands import *

class SoundBoardCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to soundboard files
        soundboardDir = os.path.join(os.path.dirname(__file__), '../SoundBoard/')
        # Tokenize the input string
        argv = message.content.split(' ')
        # Send a list of all files when the first term is list
        if argv[0] == 'list':
            for root, dirs, files in os.walk(soundboardDir):
                retMessage = '```\n'
                for name in sorted(files):
                    retMessage += name[:-4] + '\n'
                retMessage += '```'
            await message.author.send(retMessage) 
        else:
            try:
                await sendLocalMP3(message, soundboardDir + argv[0] + '.mp3')
            except:
                return

    def help(self):
        return '<name | list> : Plays the audio file <name>.mp3. Will return a list of all available files when used with list.'