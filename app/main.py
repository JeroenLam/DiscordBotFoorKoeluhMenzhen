import os                           # Used to load the bot token and prefix character from a .env file
from dotenv import load_dotenv      # Used to load the bot token and prefix character from a .env file
from MyClient import *              # Import the actual discrod client

if __name__ == '__main__':
    load_dotenv()                       # Load variables from .env into system
    TOKEN = os.getenv('DISCORD_TOKEN')  # Retreive the discord token

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)

    client.run(TOKEN)
