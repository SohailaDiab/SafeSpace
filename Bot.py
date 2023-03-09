import responses
import discord
import config
import image_classification
from discord.ext import commands
from discord.utils import get
import numpy as np
from PIL import Image
from io import BytesIO
import requests


# make bot online to use it
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
  """
  This method to check if method is online or not
  """
  print("-----")
  print("Bot is online!")
  print("-----")  

#checking all sent messages 
@bot.event
async def on_message(message):
  """
  check if messages or images written by users are bullying or racist or bad msg
  and ignore messages or images sent by the bot itself.
  after that send removed messages or images to the moderator
  and DM users who write these bullying messages or images.
  
  Parameters:
  - message: str
  """
  if message.author == bot.user: # Ignore messages sent by the bot itself
    return
    
  #Enter all messages for the model to check bullying messages
  if message.content:
    text = message.content
    output = responses.handle_response(text)
    if output:
      await message.delete() #delete message if it's bullying
      
      # send message for the moderator about deleleted message with username
      moderator = await bot.fetch_user(config.moderator_id)
      dm_channel = await moderator.create_dm()
      await dm_channel.send(f'{message.author.name} said: {message.content}')
      print('Message sent successfully')
      
      #DMs the user
      await message.author.send(f'{config.hello_msg}\nI noticed that you sent: "{message.content}"\n{config.choose_msg()}')

  # check if the message is an image
  if message.attachments:
    for attachment in message.attachments:
      if attachment.url.endswith('.jpg') or \
      attachment.url.endswith('.jpeg') or \
      attachment.url.endswith('.png'):
        image_bytes = await attachment.read()
        image = Image.open(BytesIO(image_bytes))
        image = np.asarray(image)

        label = image_classification.classify_image(image)
        if label:
          await message.delete() # delete the image if its content is not suitable
          await message.channel.send('Deleted not suitable image')
        
 
async def start_recording(voice_channel):
  """
  Recording audio from audio channels
  
  Parameters:
  - voice_channel: dict
  
  Returns:
  - output.mp3: recorded audio
  """
  # Connect to the voice channel
  vc = await voice_channel.connect()
  # Start recording
  vc.start_recording("output.mp3")

async def stop_recording(voice_channel):
  """
  Stop recording audio from audio channels
  
  Parameters:
  - voice_channel: dict
  """
  # Disconnect from the voice channel
  vc = get(bot.voice_clients, guild=voice_channel.guild)
  if vc:
    vc.stop_recording()
    await vc.disconnect()


# make bot enter the voice channels   
@bot.event
async def on_voice_state_update(member, before, after):
  """
  Bot enter voice channels when someone enters 
  and leaves when there is no one in channels.
  
  Parameters:
  - member: dict
  - before: dict
  - after: dict
  """
  # Check if the member is the bot itself
  if member.id == bot.user.id:
    return
  
  #retrieves all the voice channels in the server
  guild = member.guild
  voice_channels = guild.voice_channels 
    
  # Check if the member joined a voice channel 
  if before.channel is None and after.channel is not None:
    channel = after.channel
    await channel.connect()
  
  # Check if the member left a voice channel
  elif before.channel is not None and after.channel is None:
    voice_channel = before.channel
    voice_client = bot.voice_clients[0]
    await voice_client.disconnect()

# To be added in the future - Voice Channel feature
"""
async def on_voice_state_update(member, before, after):
  # Check if the member is the bot itself
  if member.id == bot.user.id:
    return
  
  #retrieves all the voice channels in the server
  guild = member.guild
  voice_channels = guild.voice_channels 
    
  # Check if the member joined a voice channel 
  if before.channel is None and after.channel is not None:
    channel = after.channel
    await channel.connect()

    await start_recording(channel)
  
  # Check if the member left a voice channel
  elif before.channel is not None and after.channel is None:
    voice_channel = before.channel
    voice_client = bot.voice_clients[0]
    await voice_client.disconnect()
    # Stop recording the channel
    await stop_recording(voice_channel)

"""


bot.run(config.TOKEN)
