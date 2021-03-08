from BaseCommandHandler import *

# Importing commands
from HelloWorldCommand import *
from SoundBoardCommand import *
from InspiroCommands import *
from TTSCommands import *

class CommandHandler(BaseCommandHandler):
    # On initialisation, define all commands in the command handler
    def __init__(self):
        BaseCommandHandler.__init__(self)
        self.addCommand('hw', HelloWorldCommand())
        self.addCommand('sb', SoundBoardCommand())
        self.addCommand('quote', InsiroPictureCommand())
        self.addCommand('quotexmas', InsiroPictureXMasCommand())
        self.addCommand('quotem', InsiroMusicCommand())
        self.addCommand('tts', Text2SpeechCommand())
        self.addCommand('tts2', Text2Speech2Command())
        self.addCommand('tttt', Translate2TextCommand())
        self.addCommand('ttts', Translate2SpeechCommand())
