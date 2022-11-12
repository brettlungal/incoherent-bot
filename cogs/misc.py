import discord
from discord.ext import commands
import random
from utils.constants import IDEA_LIST
from utils.embeds import generate_idea_embed

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def idea(self,ctx):
        index = random.randint(0, len(IDEA_LIST)-1)
        idea_embed = generate_idea_embed(IDEA_LIST[index])
        await ctx.send(embed=idea_embed)

async def setup(bot):
    await bot.add_cog(Misc(bot))
