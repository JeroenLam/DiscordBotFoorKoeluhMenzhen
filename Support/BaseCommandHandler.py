# Include all other commands
from BaseCommand import *


class BaseCommandHandler:
    # Dict containing all commands
    def __init__(self):
        self.commands = {}

    # Adds the command to the command handler
    def addCommand(self, name, function):
        self.commands[name] = function

    async def run(self, message):
        # Tokenize message to get first entry
        argv = message.content.split(' ')
        command = argv[0].lower()

        # Remove command from the input string and remove leading whitespaces
        message.content = message.content[len(command):].lstrip()

        com = BaseCommand()
        # Attempt to run the command from the list of commands
        try:
            com = self.commands[command]
        except:
            print('ERROR: Invalid command ' + str(message.author) + ' - ' + message.content)
            return

        await com.execute(message)
        print('  executed ' + str(message.author) + ' - ' + message.content)

    # Prints the content of the commandhandler, used for debugging
    def print(self):
        print(self.commands)