import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def tree(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def cabbage(ctx):
    img_name = random.choice(os.listdir('images2'))
    with open(f'images2/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def potato(ctx):
    img_name = random.choice(os.listdir('images3'))
    with open(f'images3/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("MTEzMDg5NDk1MDExMjk2ODgzNg.GVZU_V.d5wLU-8IEvVY4QQOWoEqTaXEYIIe8qyzFC2TZM")