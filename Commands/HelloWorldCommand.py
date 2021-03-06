from BaseCommand import *

class HelloWorldCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Hello World!')

    async def help(self):
        return 'hw : Hello world command.'