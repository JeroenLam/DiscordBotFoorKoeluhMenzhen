import os                           # Used to load the bot token and prefix character from a .env file
from dotenv import load_dotenv      # Used to load the bot token and prefix character from a .env file
import discord                      # Include the discord.py[voice] library
from Commands.CommandHandler import *        # Add command handler to the path and main file
from AdminCommands.AdminCommandHandler import *   # Add admin commands handler to the path and main file
from Commands.sb_on_user_connect import *    # When a user connect, play soundboard sound

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

    async def on_voice_state_update(self, member, before, after):
        if member == self.user:   # If own message
            return
        
        if after.afk == 1:           # If you move to afk
            return
    
        print('  ' + member.name + ' moved: ' + str(before.channel) + ' => ' + str(after.channel))

        # If the user moved away from the channel
        if before.channel != after.channel:
            # If they moved to another channel on the server
            if str(after.channel) != 'None':
                await sb_on_user_connect(member, after)
            # If the user disconnects from the server
            else:
                if len(before.channel.voice_states) == 1:
                    await before.channel.guild.voice_client.disconnect()