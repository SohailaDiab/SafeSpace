import responses
import discord
import config
from discord.ext import commands
import numpy as np

# make bot online to use it
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
  print("-----")
  print("Bot is online!")
  print("-----")  

#checking all sent messages 
@bot.event
async def on_message(message):
  if message.author == bot.user: # Ignore messages sent by the bot itself
    return
    
  #Enter all messages for the model to check bullying messages
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
    await message.author.send(f"{config.hello_msg}\nAccording to {message.content}\n{config.choose_msg()}")
    
bot.run(config.TOKEN)