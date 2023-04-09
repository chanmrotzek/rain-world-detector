import discord
import os
import re

intents = discord.Intents.all()
intents.message_content = True
intents.reactions = True

discord_user = int(os.environ['USER_ID'])

client = discord.Client(intents=intents)

rain_world_counter = 0  # initialize the counter

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

import re

# Define a regular expression pattern to match variations of "Rain World"
rain_world_pattern = re.compile(r'\b(?:rain[\s-]*world|rw)\b', re.IGNORECASE)

@client.event
async def on_message(message):
    global rain_world_counter
    print('Received message:', message.content)
    print('FULL MESSAGE:', message)

    if message.author == client.user:
        return

    # Check if the message contains a variation of "Rain World"
    if message.author.id == discord_user and rain_world_pattern.search(message.content):
        print('Recognized command:', message.content)
        rain_world_counter += 1  # increment the counter
        print('Adding flag reaction')
        await message.add_reaction("🚩")  # react with an emoji

    # Check if the message contains any GIF attachments
    for attachment in message.attachments:
        if attachment.content_type == 'image/gif':
            # Check if the GIF URL contains a variation of "Rain World"
            if rain_world_pattern.search(attachment.url):
                print('Recognized Rain World GIF:', attachment.url)
                rain_world_counter += 1  # increment the counter
                print('Adding flag reaction')
                await message.add_reaction("🚩")  # react with an emoji

    if message.content == "!rainworldcount":
        print('Recognized command:', message.content)
        await message.channel.send(f"Käselord has mentioned Rain World {rain_world_counter} times. I'll continue to monitor their usage.")  # return the counter's value


token = os.environ['DISCORD_TOKEN']

client.run(token)
