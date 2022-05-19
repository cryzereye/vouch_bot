import discord
import json
import classes.Bot as bot

config = json.load(open("json/config.json"))
sign = config["command_sign"]
client = discord.Client()
target_channel = client.get_channel(int(config["target_channel_id"]))

@client.event
async def on_ready():
    print('Naruhodo.....8)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(sign + 'vouch'):
        await message.channel.send("still in development...")

client.run(config["discord_token"])