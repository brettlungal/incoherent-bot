import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.load_extension("cogs.music")
    await bot.load_extension("cogs.poll")
    await bot.load_extension("cogs.misc")
    print("bot is online")
    

if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv('TOKEN'))





