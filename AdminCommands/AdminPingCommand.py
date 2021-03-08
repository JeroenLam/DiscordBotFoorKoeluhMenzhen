from BaseCommand import *

class AdminPingCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Pong!')

    def help(self):
        return ': Sends Pong! to the user.'