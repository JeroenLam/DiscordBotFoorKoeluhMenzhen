import os
from BaseCommand import *
import pafy
from VoiceCommands import *
from youtubesearchpython.__future__ import VideosSearch

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

class playStreamUrlCommand(BaseCommand):
    async def execute(self, message):
        try:
            await sendAudio(message, message.content)
        except:
            await message.channel.send('Invalid url!')

    def help(self):
        return '<url>: play the provided url'

class playYtUrlCommand(BaseCommand):
    async def execute(self, message):
        try:
            video = pafy.new(message.content)
            audio = video.getbestaudio()
            playurl = audio.url
            await message.channel.send('Playing: ' + video.title)
            await sendAudio(message, playurl)
        except:
            await message.channel.send('Invalid url!')

    def help(self):
        return '<url>: play the provided youtube url'

class playYtCommand(BaseCommand):
    async def execute(self, message):
        videoSearch = VideosSearch(message.content, limit = 1)
        videosResult = await videoSearch.next()
        url = videosResult['result'][0]['link']
        print(videosResult)
        print(url)
        try:
            video = pafy.new(url)
            audio = video.getbestaudio()
            playurl = audio.url
            await message.channel.send('Playing: ' + video.title)
            await sendAudio(message, playurl)
        except:
            await message.channel.send('Invalid url!')


    def help(self):
        return '<search string>: play the first youtube video found with this search string'