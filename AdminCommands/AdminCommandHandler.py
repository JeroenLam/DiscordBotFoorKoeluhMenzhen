# Include all other commands
from AdminHelloWorldCommand import *
from AdminPingCommand import *

class AdminCommandHandler:
    commands = {'hw' : AdminHelloWorldCommand(),
                'ping' : AdminPingCommand()}


    async def run(self, message):
        # Tokenize message to get first entry
        argv = message.content.split(' ')
        command = argv[0].lower()
        # Attempt to run the command from the list of commands
        try:
            await self.commands[command].execute(message)
            print(' ADMIN ' + str(message.author) + ' - ' + message.content)
        except:
            print('ERROR: Invalid command ' + str(message.author) + ' - ' + message.content)
