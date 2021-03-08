# Base command to derive from for other commands

class BaseCommand:
    async def execute(self, message):
        print("ERROR: base command not overwriten")

    async def help(self):
        return 'ERROR: command explination not defined by programmer'