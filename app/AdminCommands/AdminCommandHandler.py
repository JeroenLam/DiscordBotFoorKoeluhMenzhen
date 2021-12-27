from Support.BaseCommandHandler import *

# Importing commands
from AdminCommands.AdminHelloWorldCommand import *
from AdminCommands.AdminPingCommand import *
from AdminCommands.AdminSoundBoardCommands import *

class AdminCommandHandler(BaseCommandHandler):
    # On initialisation, define all commands in the command handler
    def __init__(self):
        BaseCommandHandler.__init__(self)
        self.addCommand('hw', AdminHelloWorldCommand())
        self.addCommand('ping', AdminPingCommand())
        self.addCommand('sbadd', AdminSBAddCommand())
        self.addCommand('sbrm', AdminSBRmCommand())
        self.addCommand('sbmv', AdminSBMvCommand())
        self.addCommand('sbcp', AdminSBCpCommand())