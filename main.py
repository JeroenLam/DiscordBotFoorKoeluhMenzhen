from MyClient import *              # Import the actual discrod client
import os                           # Used to load the bot token and prefix character from a .env file
from dotenv import load_dotenv      # Used to load the bot token and prefix character from a .env file

load_dotenv()                       # Load variables from .env into system
TOKEN = os.getenv('DISCORD_TOKEN')  # Retreive the discord token

client = MyClient()
client.run(TOKEN)