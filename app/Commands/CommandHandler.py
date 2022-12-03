from Support.BaseCommandHandler import *

# Importing commands
from Commands.HelloWorldCommand import *
from Commands.SoundBoardCommand import *
from Commands.InspiroCommands import *
from Commands.TTSCommands import *
from Commands.DisconnectCommand import *
from Commands.playStream import *
from Commands.chatbotCommand import *

class CommandHandler(BaseCommandHandler):
    # On initialisation, define all commands in the command handler
    def __init__(self):
        BaseCommandHandler.__init__(self)
        self.addCommand('hw', HelloWorldCommand())
        self.addCommand('sb', SoundBoardCommand())
        self.addCommand('sbset', SoundBoardSetJoinSoundCommand())
        self.addCommand('quote', InsiroPictureCommand())
        self.addCommand('quotexmas', InsiroPictureXMasCommand())
        self.addCommand('quotem', InsiroMusicCommand())
        self.addCommand('tts', Text2SpeechCommand())
        self.addCommand('tts2', Text2Speech2Command())
        self.addCommand('tttt', Translate2TextCommand())
        self.addCommand('ttts', Translate2SpeechCommand())
        self.addCommand('disconnect', DisconnectCommand())
        self.addCommand('stop', stopAudioCommand())
        self.addCommand('pause', pauseAudioCommand())
        self.addCommand('play', playYTCommand())
        self.addCommand('yt', playYTCommand())
        self.addCommand('cb', gpt3ChatbotCommand())
