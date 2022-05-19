import discord
import json

class Bot:
    global client, config, sign
    
    def __init__(self):
        config = json.load(open("json/config.json"))
        sign = config["command_sign"]
        client = discord.Client()

        client.run(config["discord_token"])

        @client.event
        async def on_ready():
            self.botInit()

        @client.event
        async def on_message(message):
            await message.channel.send(self.processMsg(message))


    def botInit() -> None:
        print('Naruhodo.....8)')

    def processMsg(message) -> str:
        if message.author == client.user:
            return ""

        if message.content.startswith(sign + 'vouch'):
            return ""