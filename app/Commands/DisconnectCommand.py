from Support.BaseCommand import *

class DisconnectCommand(BaseCommand):
    async def execute(self, message):
        if hasattr(message.author.voice, 'channel'):
            await message.channel.guild.voice_client.disconnect()

    def help(self):
        return ': Disconnect the bot from your voice channel'