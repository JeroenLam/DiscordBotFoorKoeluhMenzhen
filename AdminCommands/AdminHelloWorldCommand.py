from BaseCommand import *

class AdminHelloWorldCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Hello World! (admin version :p)')