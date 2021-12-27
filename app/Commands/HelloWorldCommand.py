from Support.BaseCommand import *

class HelloWorldCommand(BaseCommand):
    async def execute(self, message):
        await message.channel.send('Hello World!, find out more at https://github.com/JeroenLam/DiscordBotFoorKoeluhMenzhen')

    def help(self):
        return ': Hello world command.'