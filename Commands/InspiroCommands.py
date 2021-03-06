from BaseCommand import *
import sys
sys.path.append('Support')
from getInpiro import *
from VoiceCommands import *
import discord

# Downloads a InspiroBot picture quote and sends it in the text channel
class InsiroPictureCommand(BaseCommand):
    async def execute(self, message):
        getInspiro()
        await message.channel.send(file=discord.File('Temp/inspiro.jpg'))

    async def help(self):
        return 'quote : Generates a inspirobot quote.'

# Downloads a InspiroBot Xmas picture quote and sends it in the text channel
class InsiroPictureXMasCommand(BaseCommand):
    async def execute(self, message):
        getInspiroXmas()
        await message.channel.send(file=discord.File('Temp/inspiroXmas.jpg'))

    async def help(self):
        return 'quoteXmas : Generates a festive inspirobot quote.'

# Downloads a InsiroBot music quote and sends it in the voice channel
class InsiroMusicCommand(BaseCommand):
    async def execute(self, message):
        getInspiroMP3()
        await sendLocalMP3(message, 'Temp/inspiro.mp3')

    async def help(self):
        return 'quotem : Generates a inspirobot audio quote.'