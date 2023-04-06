import discord
import os

intents = discord.Intents.all()
intents.message_content = True

discord_user = os.environ['USER_ID']

client = discord.Client(intents=intents)

rain_world_counter = 0  # initialize the counter

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print('Received message:', message.content)
    print('FULL MESSAGE:', message)
    
    if message.author == client.user:
        return

    if message.author.id == discord_user and "rain world" in message.content.lower():
        print('Recognized command:', message.content)
        rain_world_counter += 1  # increment the counter
        await message.add_reaction("🚩")  # react with an emoji

    if message.content == "!rainworldcount":
        print('Recognized command:', message.content)
        await message.channel.send(f"Käselord has mentioned Rain World {rain_world_counter} times. I'll continue to monitor their usage.")  # return the counter's value


token = os.environ['DISCORD_TOKEN']

client.run(token)
