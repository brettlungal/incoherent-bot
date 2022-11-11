import discord
from discord.ext import commands

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def brig(ctx, offender):
        await ctx.send(f"{ctx.author} has voted to brig {offender}")

async def setup(bot):
    await bot.add_cog(Poll(bot))