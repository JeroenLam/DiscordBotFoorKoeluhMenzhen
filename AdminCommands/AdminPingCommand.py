from AdminBaseCommand import *

class AdminPingCommand(AdminBaseCommand):
    async def execute(self, message):
        await message.channel.send('Pong!')