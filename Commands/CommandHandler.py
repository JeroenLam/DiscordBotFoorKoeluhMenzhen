# Include all other commands
from BaseCommand import *
from HelloWorldCommand import *
from SoundBoardCommand import *
from InspiroCommands import *

class CommandHandler:
    commands = {'hw' : HelloWorldCommand(),
                'sb' : SoundBoardCommand(),
                'quote' : InsiroPictureCommand(),
                'quotexmas' : InsiroPictureXMasCommand(),
                'quotem' : InsiroMusicCommand()}


    async def run(self, message):
        # Tokenize message to get first entry
        argv = message.content.split(' ')
        command = argv[0].lower()

        com = BaseCommand()
        # Attempt to run the command from the list of commands
        try:
            com = self.commands[command]
        except:
            print('ERROR: Invalid command ' + str(message.author) + ' - ' + message.content)
            return

        await com.execute(message)
        print('  executed ' + str(message.author) + ' - ' + message.content)