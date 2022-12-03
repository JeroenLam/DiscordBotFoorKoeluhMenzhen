from Support.BaseCommand import *
from Support.VoiceCommands import *
import os                           # Used to load the bot token and prefix character from a .env file
from dotenv import load_dotenv      # Used to load the bot token and prefix character from a .env file
import openai

class gpt3ChatbotCommand(BaseCommand):
    # Set the OpenAI API key
    load_dotenv()                       # Load variables from .env into system
    TOKEN = os.getenv('OPENAI_TOKEN')  # Retreive the discord token
    openai.api_key = TOKEN

    async def execute(self, message):
        print(message.content)

        # model = openai.Model.get("text-davinci-002")

        # response = model.generate(
        #     prompt=message.content,
        #     temperature=0.5,
        #     max_tokens=1024,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0
        # )
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=message.content,
            temperature=0.6,
        )
        
        # Send the chatbot's response to the user
        # await message.channel.send(response["data"][0]["text"])
        await message.channel.send(response.choices[0].text)

    def help(self):
        return '<question>: Return the responce of the davinci-002 openai chatbot'
