import pafy
import discord
from discord import FFmpegPCMAudio, PCMVolumeTransformer
from discord.ext import commands
from constants import FFMPEG_OPTIONS
import urllib
import re

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.music_queue = []

    @commands.command()
    async def boom(self, ctx):
        await ctx.send("https://www.twitch.tv/itsyourboyandrew1/clip/HeartlessWittyGoatWOOP-a93YUHFgWVNww0SQ")

    @commands.command(pass_context=True)
    async def fight(self, ctx):
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

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()
        self.music_queue = []

    @commands.command(pass_context=True)
    async def play(self, ctx, *, arg):
        if ctx.message.author.voice == None:
            await ctx.reply("No Voice Channel", "You need to be in a voice channel to use this command!")
            return

        channel = ctx.message.author.voice.channel
        voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)

        if ctx.voice_client is None:
            voice_client = await voice.connect()

        if len(self.music_queue) == 0:
            self.music_queue.append(arg)
            self.play_music(arg)
            await ctx.send(f"Playing {arg}")
        else:
            # add to queue
            self.music_queue.append(arg)
            await ctx.send(f"{arg} added to queue")

    def play_music(self, query):
        source, video_id = self.get_media_source(query)
        self.bot.voice_clients[0].play(source, after=self.after_play)

    def get_media_source(self, arg):
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

    def after_play(self, error):
        self.music_queue.pop(0)
        if len(self.music_queue) > 0:
            self.play_music(self.music_queue[0])
        else:
            self.bot.voice_clients[0].disconnect()

async def setup(bot):
    await bot.add_cog(Music(bot))