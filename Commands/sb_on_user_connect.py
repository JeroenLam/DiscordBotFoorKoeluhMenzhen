import os
from VoiceCommands import *

async def sb_on_user_connect(member, after):
    soundboardDir = os.path.join(os.path.dirname(__file__), '../SoundBoard/')
    try:
        await sendLocalMP32(after.channel, soundboardDir + member.nick + ".mp3")
    except:
        return