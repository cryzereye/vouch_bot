import discord
import json

config = json.load(open("json/config.json"))
sign = config["command_sign"]
client = discord.Client()

@client.event
async def on_ready():
    print('Naruhodo.....8)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(sign + 'hello'):
        await message.channel.send('Hello!')

client.run(config["discord_token"])