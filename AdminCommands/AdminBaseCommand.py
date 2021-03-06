# Base command to derive from for other commands

class AdminBaseCommand:
    async def execute(self, message):
        print("ERROR: base command not overwriten")