from AdminBaseCommand import *

class AdminHelloWorldCommand(AdminBaseCommand):
    async def execute(self, message):
        await message.channel.send('Hello World! (admin version :p)')