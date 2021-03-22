from BaseCommandHandler import *

# Importing commands
from AdminHelloWorldCommand import *
from AdminPingCommand import *
from AdminSoundBoardCommands import *

class AdminCommandHandler(BaseCommandHandler):
    # On initialisation, define all commands in the command handler
    def __init__(self):
        BaseCommandHandler.__init__(self)
        self.addCommand('hw', AdminHelloWorldCommand())
        self.addCommand('ping', AdminPingCommand())
        self.addCommand('sbadd', AdminSBAddCommand())
        self.addCommand('sbrm', AdminSBRmCommand())
        self.addCommand('sbmv', AdminSBMvCommand())
        seld.addCommand('sbcp', AdminSBCpCommand())