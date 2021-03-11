import os                           # Used to load the bot token and prefix character from a .env file
from dotenv import load_dotenv      # Used to load the bot token and prefix character from a .env file
import sys                          # Used to include subdirectories to path
import discord                      # Include the discord.py[voice] library
sys.path.append(os.path.join(os.path.dirname(__file__), 'Support'))          # Include support functions to active path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Commands'))
from CommandHandler import *        # Add command handler to the path and main file
sys.path.append(os.path.join(os.path.dirname(__file__), 'AdminCommands'))
from AdminCommandHandler import *   # Add admin commands handler to the path and main file


class MyClient(discord.Client):
    # Import prefix and admins from .env
    load_dotenv()
    PREFIX = os.getenv('PREFIX')
    ADMINPREFIX = os.getenv('ADMINPREFIX')
    ADMINS = os.getenv('ADMINS').split(',')

    # Import the command handler used to execute the command
    commandHandler = CommandHandler()
    adminCommandHandler = AdminCommandHandler()

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Filter our own messages
        if message.author == self.user:
            return

        # Filter messages with normal user prefix
        if message.content.find(self.PREFIX) == 0:
            message.content = message.content[len(self.PREFIX):]                # Remove prefix from the command
            await self.commandHandler.run(message)                              # Execute command

        # Filter messages with admin user prefix and the user is an admin
        if message.content.find(self.ADMINPREFIX) == 0:
            if self.ADMINS.count(str(message.author)):
                message.content = message.content[len(self.ADMINPREFIX):]       # Remove prefix from the command
                await self.adminCommandHandler.run(message)                     # Execute command