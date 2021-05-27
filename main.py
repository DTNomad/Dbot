import discord
import os
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.content.startswith('!dinv '):
    channel = message.channel
    user_text = message.author.name
    game_text = message.content[6:]
    await channel.send(user_text + ' wants to play **' + game_text + '**. 👍 to join!')

    def check(reaction, user):
      return user == message.author and str(reaction.emoji) == '👍'

    try:
      reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
      await channel.send('👎')
    else:
      await channel.send(user.name + ' wants to join')

client.run(os.environ['TOKEN'])