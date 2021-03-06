import sys                          # Used to include subdirectories to path
import discord                      # Include the discord.py[voice] library
sys.path.append('Commands')
from CommandHandler import *        # Add command handler to the path and main file
sys.path.append('AdminCommands')
from AdminCommandHandler import *   # Add admin commands handler to the path and main file
import os                           # Used to load the bot token and prefix character from a .env file
from dotenv import load_dotenv      # Used to load the bot token and prefix character from a .env file

class MyClient(discord.Client):
    # Import prefix and admins from .env
    load_dotenv()
    PREFIX = os.getenv('PREFIX')
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

        # Filter messages without the prefix
        if message.content.find(self.PREFIX) != 0:
            return

        # Remove prefix from the command
        message.content = message.content[len(self.PREFIX):]

        # Admin only commands
        #if self.ADMINS.count(str(message.author)):
        #    await self.adminCommandHandler.run(message)

        # Commands for everybody
        await self.commandHandler.run(message)
