# Include all other commands
from HelloWorldCommand import *

class CommandHandler:
    commands = {'hw' : HelloWorldCommand()}


    async def run(self, message):
        # Tokenize message to get first entry
        argv = message.content.split(' ')
        command = argv[0].lower()
        # Attempt to run the command from the list of commands
        try:
            await self.commands[command].execute(message)
            print(' executed ' + str(message.author) + ' - ' + message.content)
        except:
            print('ERROR: Invalid command ' + str(message.author) + ' - ' + message.content)
