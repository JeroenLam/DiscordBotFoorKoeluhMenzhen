from Support.BaseCommand import *
from Support.VoiceCommands import *

class stopAudioCommand(BaseCommand):
    async def execute(self, message):
        stopVoice(message)

    def help(self):
        return ': Stop the current audio'

class pauseAudioCommand(BaseCommand):
    async def execute(self, message):
        pauseVoice(message)

    def help(self):
        return ': Pauses the current audio'