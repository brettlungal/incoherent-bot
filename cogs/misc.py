import discord
from discord.ext import commands
import random
from utils.constants import IDEA_LIST
from utils.embeds import generate_idea_embed, generate_sink_embed, generate_sink_count_embed
from utils.persistence import Persistence
import mysql.connector
import os

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = mysql.connector.connect(user=os.environ['DB_USER'], password=os.environ['DB_PASS'], host=os.environ['DB_HOST'], database=os.environ['DB_NAME'])
        self.cursor = self.db.cursor()
        self.data_persistence = Persistence(self.db, self.cursor)

    @commands.command()
    async def idea(self,ctx):
        index = random.randint(0, len(IDEA_LIST)-1)
        idea_embed = generate_idea_embed(IDEA_LIST[index])
        await ctx.send(embed=idea_embed)

    @commands.command()
    async def sink(self, ctx, boatname=None):
        self.data_persistence.add_sink(boatname)
        sink_embed = generate_sink_embed(boatname)
        await ctx.send(embed=sink_embed)
    
    @commands.command()
    async def sinkcount(self,ctx):
        count = self.data_persistence.get_sink_count()
        count_embed = generate_sink_count_embed(count)
        await ctx.send(embed=count_embed)

async def setup(bot):
    await bot.add_cog(Misc(bot))
