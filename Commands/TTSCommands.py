from BaseCommand import *
from VoiceCommands import *
from googletrans import Translator

# Tim to speach, converts text to a dutch voice.
class Text2SpeechCommand(BaseCommand):
    async def execute(self, message):
        await sendTTS(message, message.content, 'nl')

    async def help(self):
        return '<text>: Tim-to-speech, converts text to audio in the current channel in a dutch voice.'

# General text to speach, first word from the message will be considerd as the language
class Text2Speech2Command(BaseCommand):
    async def execute(self, message):
        argv = message.content.split(' ')
        language = argv[0]
        sentence = message.content[len(language):].lstrip()
        await sendTTS(message, sentence, language)

    async def help(self):
        return '<language> <text>: Text-to-speech, converts text to audio in the current channel in a <language> voice.'

# Translates text to text in the provided language
class Translate2TextCommand(BaseCommand):
    def __init__(self):
        self.translator = Translator()

    async def execute(self, message):
        argv = message.content.split(' ')
        language = argv[0]
        sentence = message.content[len(language):].lstrip()
        sentence_trans = self.translator.translate(sentence, dest=language).text
        await message.channel.send(sentence_trans) 

    async def help(self):
        return '<language> <text>: Translates to a language of your choise in text, e.g. nl, en, es, ja, ru.'

# Translates text to spech in the provided language
class Translate2SpeechCommand(BaseCommand):
    def __init__(self):
        self.translator = Translator()

    async def execute(self, message):
        argv = message.content.split(' ')
        language = argv[0]
        sentence = message.content[len(language):].lstrip()
        sentence_trans = self.translator.translate(sentence, dest=language).text
        await sendTTS(message, sentence_trans, language)

    async def help(self):
        return '<language> <text>: Translates to a language of your choise in voice, e.g. nl, en, es, ja, ru.'