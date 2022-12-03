from Support.BaseCommand import *
from Support.VoiceCommands import *
import youtube_dl

class stopAudioCommand(BaseCommand):
    async def execute(self, message):
        stopVoice(message)

    def help(self):
        return ': Stop the current audio'

class pauseAudioCommand(BaseCommand):
    async def execute(self, message):
        pauseVoice(message)

    def help(self):
        return ': Pauses the current audio'

class playYTCommand(BaseCommand):
    # Set up the youtube_dl options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Create a youtube_dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    async def execute(self, message):
        # Search YouTube for the specified query
        search_results = self.ydl.extract_info(f"ytsearch1:{message.content}", download=False)

        # Get the first video from the search results
        video = search_results['entries'][0]

        # Create a youtube_dl player object and start playing the audio
        player = self.ydl.extract_info(video['webpage_url'], download=False)
        await sendAudio(message, player['url'])
        await message.channel.send(f"Now playing: {video['title']}")

    def help(self):
        return '<querry>: Searches YouTube based on the provided querry and starts playing the corresponding audio.'