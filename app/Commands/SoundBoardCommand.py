from Support.BaseCommand import *
import os
from Support.VoiceCommands import *
import random
import shutil

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
                counter = 0
                for name in sorted(files):
                    # Add name to the retMessage without the .mp3
                    retMessage += name[:-4] + '\n'
                    counter = counter + 1
                    if counter > 99:
                        retMessage += '```'
                        await message.author.send(retMessage)
                        retMessage = '```\n'
                        counter = 0
                retMessage += '```'
            await message.author.send(retMessage) 
            return
        elif argv[0] == 'random':
            for root, dirs, files in os.walk(soundboardDir):
                idx = random.randint(0, len(files))
                try:
                    await message.channel.send('Playing: ' + files[idx][:-4])
                    await sendAudio(message, soundboardDir + files[idx])
                except:
                    return
        else:
            try:
                await sendAudio(message, soundboardDir + argv[0] + '.mp3')
            except:
                return

    def help(self):
        return '<name | list> : Plays the audio file <name>.mp3. Will return a list of all available files when used with list.'

class SoundBoardSetJoinSoundCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to soundboard files
        soundboardDir = os.path.join(os.path.dirname(__file__), '../SoundBoard/')
        argv = message.content.split(' ')
        if len(argv) != 1:
            await message.channel.send('Please provide 1 arguments as explained in the help function')
            return
        
        bool_found = 0
        name_old = argv[0] + '.mp3'
        name_new = str(message.author) + '.mp3'
        for root, dirs, files in os.walk(soundboardDir):
            for name in files:
                if name == name_old:
                    shutil.copyfile(soundboardDir + name, soundboardDir + name_new)
                    bool_found = 1
                    await message.channel.send('copied ' + name_old + ' to ' + name_new)
        if not bool_found:
            await message.channel.send('No file found named: ' + name_old) 

    def help(self):
        return '<soundName> : Set the soundName as the users join sound. Note that the user should not have a space in their Discord name!!!'