import discord
from discord.ext import commands
from asyncio import sleep
from utils.embeds import *

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def brig(self, ctx, offender:discord.Member):
        # TODO break embed generation into functions to clean up code
        vote_embed = generate_vote_embed(offender)
        message = await ctx.send(embed=vote_embed)
        await message.add_reaction('❎')
        await message.add_reaction('✅')
        await sleep(120)
        cache_msg = discord.utils.get(self.bot.cached_messages, id=message.id)
        no_votes = cache_msg.reactions[0].count
        yes_votes = cache_msg.reactions[1].count
        if yes_votes > no_votes:
            brigged_embed = generate_brigged_embed(offender)
            await self.strip_roles(offender)
            await ctx.send(embed=brigged_embed)
        elif no_votes > yes_votes:
            negative_embed = generate_negative_vote_embeded(offender)
            await ctx.send(embed=negative_embed)
        elif no_votes == yes_votes:
            tie_embed = generate_tie_embed(offender)
            await ctx.send(embed=tie_embed)

    async def strip_roles(self, user: discord.Member):
        for i in user.roles:
            try:
                await user.remove_roles(i)
            except:
                print(f"Can't remove the role {i}")

async def setup(bot):
    await bot.add_cog(Poll(bot))