import discord
import os

intents = discord.Intents.default()
intents.messages = True

discord_user = int(os.getenv('USER_ID'))

client = discord.Client(intents=intents)

rain_world_counter = 0  # initialize the counter

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global rain_world_counter  # declare the counter as global

    if message.author == client.user:
        return

    if message.author.id == discord_user and "rain world" in message.content.lower():
        rain_world_counter += 1  # increment the counter
        await message.add_reaction("🚩")  # react with an emoji

    if message.content == "!rainworldcount":
        await message.channel.send(f"Käselord has mentioned Rain World {rain_world_counter} times. I'll continue to monitor their usage.")  # return the counter's value

token = os.getenv('DISCORD_TOKEN')

client.run(token)
