from BaseCommand import *
import os
from VoiceCommands import *
from getInpiro import download
from pydub import AudioSegment, effects
import shutil

# Add a audio file to the soundboard
class AdminSBAddCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to soundboard files
        soundboardDir = os.path.join(os.path.dirname(__file__), '../SoundBoard/')
        argv = message.content.split(' ')

        if len(message.attachments):                                    # If there is an attachment
            url = message.attachments[0].proxy_url                          # retreive url from message
            if url[-4:] == '.mp3':                                          # verify the extension
                fileName = url[url.rfind('/') + 1:]                             # scrape the filename
                data = download(url)                                            # Download the data
                with open(soundboardDir + fileName, 'wb') as output:             # Safe the data on disk
                    output.write(data.read())

                if (argv[0] != '-nn'):
                    not_normalised = AudioSegment.from_file(soundboardDir + fileName, "mp3")
                    normalised = not_normalised.apply_gain(-20.0 - not_normalised.dBFS)
                    normalised.export(soundboardDir + fileName, format="mp3")

                await message.channel.send('Added ' + fileName + ' to the soundboard!')
                print('Added ' + fileName + 'To the soundboard')
            else:
                await message.channel.send('We only accept .mp3 files')
        else:
            await message.channel.send('No valid attachments!')

    def help(self):
        return '<file.mp3> <-nn>: Adds the <file>.mp3 to the soundboard folder. If you use `-nn` then the volume will not be normalised.'

# Remove audio files to the soundboard
class AdminSBRmCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to soundboard files
        soundboardDir = os.path.join(os.path.dirname(__file__), '../SoundBoard/')

        argv = message.content.split(' ')
        for arg in argv:
            arg += '.mp3'
            for root, dirs, files in os.walk(soundboardDir):
                for name in files:
                    if name == arg:
                        os.remove(soundboardDir + name)
                        await message.channel.send('Removed ' + name + ' from the soundboard!')           

    def help(self):
        return '<fileName_1> ... <fileName_N> : Remove <fileName_i>.mp3 from the soundboard folder.'

# Rename audio files to the soundboard
class AdminSBMvCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to soundboard files
        soundboardDir = os.path.join(os.path.dirname(__file__), '../SoundBoard/')
        argv = message.content.split(' ')
        if len(argv) != 2:
            await message.channel.send('Please provide 2 arguments as explained in the help function')
            return
        
        bool_found = 0
        name_old = argv[0] + '.mp3'
        name_new = argv[1] + '.mp3'
        for root, dirs, files in os.walk(soundboardDir):
            for name in files:
                if name == name_old:
                    os.rename(soundboardDir + name, soundboardDir + name_new)
                    bool_found = 1
                    await message.channel.send('Renamed ' + name_old + ' to ' + name_new)
        if not bool_found:
            await message.channel.send('No file found named: ' + name_old) 

    def help(self):
        return '<fileName_old> <fileName_new> : Renames <fileName_old>.mp3 to <fileName_new>.mp3.'

# Rename audio files to the soundboard
class AdminSBCpCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to soundboard files
        soundboardDir = os.path.join(os.path.dirname(__file__), '../SoundBoard/')
        argv = message.content.split(' ')
        if len(argv) != 2:
            await message.channel.send('Please provide 2 arguments as explained in the help function')
            return
        
        bool_found = 0
        name_old = argv[0] + '.mp3'
        name_new = argv[1] + '.mp3'
        for root, dirs, files in os.walk(soundboardDir):
            for name in files:
                if name == name_old:
                    shutil.copyfile(soundboardDir + name, soundboardDir + name_new)
                    bool_found = 1
                    await message.channel.send('copied ' + name_old + ' to ' + name_new)
        if not bool_found:
            await message.channel.send('No file found named: ' + name_old) 

    def help(self):
        return '<fileName_old> <fileName_new> : Renames <fileName_old>.mp3 to <fileName_new>.mp3.'