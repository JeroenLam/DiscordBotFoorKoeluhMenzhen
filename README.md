# DiscordBotFoorKoeluhMenzhen

This repository contains the code for a discord bot used on the 'Hed huiz foor koeluh mozelen' server. Feel free to clone or fork the code for your own use.

To extend the bot you can derive a new command object from the existing `BaseCommand` and overwrite the `async def execute(self, message)` function with the actual functionallity of the command. Also overwrite the `async def help(self)` that returns the command discription for the help function.

The current framework support admin users. These can be set in the `.env` file (for an example see `ex-.env-file`). These commands can be defined in the `AdminCommands` forlder and are defined in the same way as normal commands. The only difference is that you have to extend `AdminBaseCommand` instead of `BaseCommand`.

## Features (everyone)
Currently the bot supports the following commands \
`hw` Send 'Hello World!' back to the user \
`quote` Generates a inspirobot quote (image). \
`quotexmas` Generates a festive inspirobot quote (image). \
`quotem` Generates a inspirobot audio quote. \
`sb <name | list>` Plays the audio file <name>.mp3. Will return a list of all available files when used with list. \

Features that are currently being worked on (mainly based on features that where implemented in the old bot) \
`help` Shows a list of all commands and their descriptions based on the data specified in each command object. \
`2<language> <text>` Translates 2 a language of your choise to text, e.g. nl, en, es, ja, ru. \
`3<language> <text>` Translates 2 a language of your choise to voice, e.g. nl, en, es, ja, ru. \
`<....` Some way to use discord emoticons as commands \
`reddit [hot, new, topH, topD, topW, topM, topY, topA] <subreddit>` Random post from the 25 most recent [catagory] posts. \
`pause` Pauses the audio stream of the bot. \
`stop` Stops the audio stream of the bot. \
`tts <text>` Tim-to-speech, converts text to audio in the current channel in a dutch voice. \
`tts2 <language> <text>` Text-to-speech, converts text to audio in the current channel in a <language> voice. \
  
## Features (admins)
Currently there are no administrative commands added to the bot. However in the following functions are being worked on: \
Using a seperate prefix for admin commands to make it easier to distinguish between commands for users and admins. \
`sb <add | remove | rm>` Add or remove audio from the soundboard without having acces to the server directly. \

### Future feature ideas
A ticketing system for non admins to add to ask questions which are stored in the bot until resolved. The tickets can then be send to the moderators or be pushed into a specific channel that might be set via a command. The admins will have the option to resolve the question which will remove it from the list (and possibly delete the original message). \
Combined with this ticketing system a FAQ command can be added such that admins can add or remove entries such that you do not get the same question over and over again.
