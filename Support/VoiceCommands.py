import discord

# Connect to the voice channel
async def connect2vc(message):
    if hasattr(message.author.voice, 'channel'):
        voice_channel = message.author.voice.channel
        voice = message.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        elif voice.channel != voice_channel:
            await voice.move_to(voice_channel)
        return voice
    else:
        await message.channel.send('Please enter a voice channel.')
        raise Exception('No voice channel to connect to')

# Connect to the voice channel and send local mp3 or audio stream
async def sendAudio(message, streamurl):
    try:
        voice = await connect2vc(message) 
    except:
        return
    if voice.is_playing():
        voice.stop()
    voice.play(discord.FFmpegPCMAudio(streamurl), after=lambda e: print())
   
# Stop playing audio
def stopVoice(message):
    voice = message.channel.guild.voice_client
    voice.stop()

# Pauze playing audio
def pauseVoice(message):
    voice = message.channel.guild.voice_client
    if voice.is_paused():
        voice.resume()
    else:
        voice.pause()