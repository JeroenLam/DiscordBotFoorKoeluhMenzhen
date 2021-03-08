from BaseCommand import *
from getInpiro import *
from VoiceCommands import *

# Downloads a InspiroBot picture quote and sends it in the text channel
class InsiroPictureCommand(BaseCommand):
    async def execute(self, message):
        getInspiro()
        await message.channel.send(file=discord.File('Temp/inspiro.jpg'))

    def help(self):
        return ': Generates a inspirobot quote.'

# Downloads a InspiroBot Xmas picture quote and sends it in the text channel
class InsiroPictureXMasCommand(BaseCommand):
    async def execute(self, message):
        getInspiroXmas()
        await message.channel.send(file=discord.File('Temp/inspiroXmas.jpg'))

    def help(self):
        return ': Generates a festive inspirobot quote.'

# Downloads a InsiroBot music quote and sends it in the voice channel
class InsiroMusicCommand(BaseCommand):
    async def execute(self, message):
        getInspiroMP3()
        await sendLocalMP3(message, 'Temp/inspiro.mp3')

    def help(self):
        return ': Generates a inspirobot audio quote.'