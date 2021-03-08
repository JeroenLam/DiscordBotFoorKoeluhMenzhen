from BaseCommand import *

class HelloWorldCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Hello World!')

    def help(self):
        return ': Hello world command.'