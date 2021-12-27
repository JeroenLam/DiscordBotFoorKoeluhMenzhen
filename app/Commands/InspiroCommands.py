from Support.BaseCommand import *
from Support.getInpiro import *
from Support.VoiceCommands import *
import os

# Downloads a InspiroBot picture quote and sends it in the text channel
class InsiroPictureCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to Temp folder
        tempDir = os.path.join(os.path.dirname(__file__), '../Temp/')
        getInspiro()
        await message.channel.send(file=discord.File(tempDir + 'inspiro.jpg'))

    def help(self):
        return ': Generates a inspirobot quote.'

# Downloads a InspiroBot Xmas picture quote and sends it in the text channel
class InsiroPictureXMasCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to Temp folder
        tempDir = os.path.join(os.path.dirname(__file__), '../Temp/')
        getInspiroXmas()
        await message.channel.send(file=discord.File(tempDir + 'inspiroXmas.jpg'))

    def help(self):
        return ': Generates a festive inspirobot quote.'

# Downloads a InsiroBot music quote and sends it in the voice channel
class InsiroMusicCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to Temp folder
        tempDir = os.path.join(os.path.dirname(__file__), '../Temp/')
        getInspiroMP3()
        await sendAudio(message, tempDir + 'inspiro.mp3')

    def help(self):
        return ': Generates a inspirobot audio quote.'