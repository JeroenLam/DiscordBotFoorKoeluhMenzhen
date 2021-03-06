from BaseCommand import *

class HelloWorldCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Hello World!')