import discord.client
import json.scanner

from classes.VouchManager import VouchManager

class Bot:
    global client, config, sign, vm
    
    def __init__(self) -> None:
        config = json.load(open("json/config.json"))
        sign = config["command_sign"]
        client = discord.Client()
        vm = VouchManager(client, config["target_channel_id"])

        @client.event
        async def on_ready():
            self.botInit()

        @client.event
        async def on_message(message):
            msg = self.processMsg(message)
            if msg != "":
                await message.channel.send(msg)

        client.run(config["discord_token"])


    def botInit(self) -> None:
        print('Naruhodo.....8)')

    def processMsg(self, message) -> str:
        if message.author == client.user:
            return ""

        if message.channel.id == config["bot_channel_id"]:
            if message.content.startswith(sign + 'vouch'):
                return vm.getVouch()
        elif message.channel.id == config["target_channel_id"]:
            return vm.processVerification()