from BaseCommandHandler import *

# Importing commands
from HelloWorldCommand import *
from SoundBoardCommand import *
from InspiroCommands import *

class CommandHandler(BaseCommandHandler):
    # On initialisation, define all commands in the command handler
    def __init__(self):
        BaseCommandHandler.__init__(self)
        self.addCommand('hw', HelloWorldCommand())
        self.addCommand('sb', SoundBoardCommand())
        self.addCommand('quote', InsiroPictureCommand())
        self.addCommand('quotexmas', InsiroPictureXMasCommand())
        self.addCommand('quotem', InsiroMusicCommand())
