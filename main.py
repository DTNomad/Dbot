import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!d a'):
    text = '<@' + str(message.author.id) + '>'
    await message.channel.send(text)

client.run(os.environ['TOKEN'])