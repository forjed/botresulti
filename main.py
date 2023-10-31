from googlesearch import search as s
import discord
import asyncio
from discord.ext import commands,tasks
import requests
from bs4 import BeautifulSoup
from PIL import Image

#Prefix + token
intents = discord.Intents.all()
client = commands.Bot(command_prefix = ['!'], help_command=None, intents=intents)
TOKEN = "MTE2ODMzMTczNzMxOTg3NDU3Mg.Gh8eA0.-amBzWUslEd2rOCnRB2mhlhU4h7E0ID47edqtI"

#Bot is ready
@client.event
async def on_ready():
  c = client.get_channel(1168347991694901258)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,                  name="https://resulti.net"), status=discord.Status.dnd)
  print(f"Logged in as {client.user}")
  await c.send("Hey! Im online guys!")
  
@client.command()
async def search(ctx, *, que=None):
  await ctx.send(f"Results for {que}")
  results = list(s(que, num=10, stop=10))
  for i, result in enumerate(results, 1): 
    await ctx.send(f'Result {i}: {result}')

@client.command()
async def ba(ctx, *, tesst):
  await ctx.send(tesst)

@client.command()
async def about(ctx):
  with open("about.txt", "r") as file:
    lines = file.readlines()[:22]
    for line in lines:
     await ctx.send(line) 

@client.command()
async def hi(ctx):
  await ctx.send(f"Hello {ctx.author.mention}! What can i help you with? Say !help For a list of commands!")

@client.command()
async def help(ctx):
 embed = discord.Embed(title = 'Command List!', description = 'Version Beta 1.1', color = discord.Colour.blue())
 embed.add_field(name = '!help', value = 'displays this message....')
 embed.add_field(name = '!hi', value = 'Say hi to the bot!')
 embed.add_field(name = '!about', value = 'About resulti!')
 embed.add_field(name = '!ba [string]', value = 'just a test command...')
 embed.add_field(name = '!search [query]', value = 'Searches up something using resulti!')
 await ctx.send(embed=embed)

# python is hash, js is slash and done. 
#
client.run(TOKEN)