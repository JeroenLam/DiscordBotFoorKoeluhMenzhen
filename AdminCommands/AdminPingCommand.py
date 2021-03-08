from BaseCommand import *

class AdminPingCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Pong!')