from BaseCommand import *
import os
from VoiceCommands import *
from getInpiro import download

# Add a audio file to the soundboard
class AdminSBAddCommand(BaseCommand):
    async def execute(self, message):
        if len(message.attachments):                                    # If there is an attachment
            url = message.attachments[0].proxy_url                          # retreive url from message
            if url[-4:] == '.mp3':                                          # verify the extension
                fileName = url[url.rfind('/') + 1:]                             # scrape the filename
                data = download(url)                                            # Download the data
                with open('SoundBoard/' + fileName,'wb') as output:             # Safe the data on disk
                    output.write(data.read())
                await message.channel.send('Added ' + fileName + ' to the soundboard!')
            else:
                await message.channel.send('We only accept .mp3 files')
        else:
            await message.channel.send('No valid attachments!')

    def help(self):
        return '<file.mp3> : Adds the <file>.mp3 to the soundboard folder.'

# Remove audio files to the soundboard
class AdminSBRmCommand(BaseCommand):
    async def execute(self, message):
        argv = message.content.split(' ')
        for arg in argv:
            arg += '.mp3'
            for root, dirs, files in os.walk('SoundBoard'):
                for name in files:
                    if name == arg:
                        os.remove("SoundBoard/" + name)     
                        await message.channel.send('Removed ' + fileName + ' from the soundboard!')           

    def help(self):
        return '<fileName_1> ... <fileName_N> : Remove <fileName_i>.mp3 from the soundboard folder.'

# Rename audio files to the soundboard
class AdminSBMvCommand(BaseCommand):
    async def execute(self, message):
        argv = message.content.split(' ')
        if len(argv) != 2:
            await message.channel.send('Please provide 2 arguments as explained in the help function')
            return
        
        bool_found = 0
        name_old = argv[0] + '.mp3'
        name_new = argv[1] + '.mp3'
        for root, dirs, files in os.walk('SoundBoard'):
            for name in files:
                if name == name_old:
                    os.rename("SoundBoard/" + name, "SoundBoard/" + name_new)
                    bool_found = 1
                    await message.channel.send('Renamed ' + name_old + ' to ' + name_old)
        if not bool_found:
            await message.channel.send('No file found named: ' + name_old) 

    def help(self):
        return '<fileName_old> <fileName_new> : Renames <fileName_old>.mp3 to <fileName_new>.mp3.'