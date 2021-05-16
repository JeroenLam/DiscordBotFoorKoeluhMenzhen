from BaseCommand import *

class TexCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Hello World!')

    def help(self):
        return ': Converst the input into a Latex math mode image.'