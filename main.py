import pafy
import discord
from discord import FFmpegPCMAudio, PCMVolumeTransformer
from discord.ext import commands, tasks
from constants import FFMPEG_OPTIONS
import os
from dotenv import load_dotenv
import urllib
import re

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
music_queue = []
now_playing = {}
voice_client = None

@bot.event
async def on_ready():
    print("bot is online")

@bot.command()
async def boom(ctx):
    await ctx.send("https://www.twitch.tv/itsyourboyandrew1/clip/HeartlessWittyGoatWOOP-a93YUHFgWVNww0SQ")

@bot.command()
async def fight(ctx):
    search = "shoot to thrill lyrics"
    if ctx.message.author.voice == None:
        await ctx.reply("No Voice Channel", "You need to be in a voice channel to use this command!")
        return

    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
    #TODO figure out what to do with line below
    voice_clients = []
    voice_client = discord.utils.get(voice_clients, guild=ctx.guild)

    if voice_client == None:
        voice_client = await voice.connect()
    else:
        await voice_client.move_to(channel)

    search = search.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    song = pafy.new(video_ids[0])  # creates a new pafy object
    audio = song.getbestaudio()  # gets an audio source
    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
    voice_client.play(source)  # play the source

@bot.command()
async def stop(ctx):
    await ctx.voice_client.disconnect()
    music_queue = []

@bot.command()
async def play(ctx,*,arg):
    if ctx.message.author.voice == None:
        await ctx.reply("No Voice Channel", "You need to be in a voice channel to use this command!")
        return

    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)

    if ctx.voice_client is None:
        voice_client = await voice.connect()

    if len(music_queue) == 0:
        music_queue.append(arg)
        play_music(arg)
        await ctx.send(f"Playing {arg}")
    else:
        # add to queue
        music_queue.append(arg)
        await ctx.send(f"{arg} added to queue")

@bot.command()
async def brig(ctx, offender):
    await ctx.send(f"{ctx.author} has voted to brig {offender}")


def play_music(query):
    source, video_id = get_media_source(query)
    bot.voice_clients[0].play(source, after=after_play)

def get_media_source(arg):
    if "youtube.com/" in arg:
        search = arg
    else:
        query_string = arg.replace(" ", "+")
        search = f"https://www.youtube.com/results?search_query={query_string}"
    html = urllib.request.urlopen(search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    song = pafy.new(video_ids[0])  # creates a new pafy object
    audio = song.getbestaudio()  # gets an audio source
    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
    return source, video_ids[0]

def after_play(error):
    music_queue.pop(0)
    if len(music_queue) > 0:
        play_music(music_queue[0])
    else:
        bot.voice_clients[0].disconnect()
            

if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv('TOKEN'))



