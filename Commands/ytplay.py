import os
from BaseCommand import *
import pafy

class ytplayCommand(BaseCommand):
    async def execute(self, message):
        # Storing path to soundboard files
        tempDir = os.path.join(os.path.dirname(__file__), '../Temp/')
        argv = message.content.split(' ')

        if len(message.attachments):                                    # If there is an attachment
            url = message.attachments[0].proxy_url                          # retreive url from message
            if url[-4:] == '.png':
                fileName = url[url.rfind('/') + 1:]                             # scrape the filename
                data = download(url)

    def help(self):
        return '<url>: play the provided youtube url'