# DiscordBotFoorKoeluhMenzhen

This repository contains the code for a discord bot used on the 'Hed huiz foor koeluh mozelen' server. Feel free to clone or fork the code for your own use.

To extend the bot you can derive a new command object from the existing `BaseCommand` and overwrite the `async def execute(self, message)` function with the actual functionallity of the command. Also overwrite the `async def help(self)` that returns the command discription for the help function.

The current framework support admin users. These can be set in the `.env` file (for an example see `ex-.env-file`). These commands can be defined in the `AdminCommands/` forlder and are defined in the same way as normal commands.

# Instalation
Before you start please make sure you have the following packages installed: \
`discord.py[voice]`

To use the bot you will need to clone the repository. Then you need to configure a `.env` file with all the parameters. An example `.env` file is included. To run the bot use the command `python3 main.py`. The bot should work on all operating systems supporting python.

To remove functionality from the bot or if you want to change the command names that trigger a command, then change the lines in `Commands/CommandHandler.py` or `Admin/AdminCommandHandler.py`.

If you wish to add your own functions to the bot, then derive a new command class from `BaseCommand` (located in `Support/BaseCommand`) and overwrite the corresponding functions. Also do not forget to include the newly created command in the corresponding command handler.

## Features (everyone)
Currently the bot supports the following commands:

#### HelloWorldCommand.py
`hw` Send 'Hello World!' back to the user, as well as some general information about the bot.

#### InspiroCommands.py
Dependencies: `urllib.request`, `string`, `ast` \
`quote` Generates a inspirobot quote (image). \
`quotexmas` Generates a festive inspirobot quote (image). \
`quotem` Generates a inspirobot audio quote. 

#### SoundBoardCommand.py
Dependencies: `discord.py[voice]` \
If you want to make use of the soundboard command then first add a folder `SoundBoard`. \
`sb <name | list | random>` Plays the audio file `<name>.mp3`. Will return a list of all available files when used with list. Will return a random sound when called with random. 
`sbset <name>` Set `<name>.mp3` as the join sound of the user calling the command.

#### TTSCommands.py
Dependencies: `googletrans`, `gtts` \
`tts <text>` Tim-to-speech, converts text to audio in the current channel in a dutch voice. \
`tts2 <language> <text>` Text-to-speech, converts text to audio in the current channel in a `<language>` voice. \
`tttt <language> <text>` Translates 2 a language of your choise to text, e.g. nl, en, es, ja, ru. \
`ttts <language> <text>` Translates 2 a language of your choise to voice, e.g. nl, en, es, ja, ru. \

Features that are currently being worked on (mainly based on features that where implemented in the old bot) \
- [x] `help` Shows a list of all commands and their descriptions based on the data specified in each command object. \

#### DisconnectCommand.py
`disconnect` Disconnects the bot from its current voice channel.
  
## Features (admins)
Currently the bot supports the following commands:

#### AdminSoundBoardCommands.py
This is the admin interface that corresponds with the `SoundBoardCommand.py` functions. It supports the following commands: \
`sbadd <attached file.mp3>` Adds the `<file>.mp3` to the soundboard folder. \
`sbrm <fileName_1> ... <fileName_N>` Remove `<fileName_i>.mp3` from the soundboard folder. \
`sbmv <fileName_old> <fileName_new>` Renames `<fileName_old>.mp3` to `<fileName_new>.mp3`.


### Future feature ideas
A ticketing system for non admins to add to ask questions which are stored in the bot until resolved. The tickets can then be send to the moderators or be pushed into a specific channel that might be set via a command. The admins will have the option to resolve the question which will remove it from the list (and possibly delete the original message). \
Combined with this ticketing system a FAQ command can be added such that admins can add or remove entries such that you do not get the same question over and over again.
