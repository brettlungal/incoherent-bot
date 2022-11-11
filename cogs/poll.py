import discord
from discord.ext import commands
from asyncio import sleep

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def brig(self, ctx, offender:discord.Member):
        # TODO break embed generation into functions to clean up code
        embed = discord.Embed(title=f"{offender} Has Been Voted To The Brig!", color=discord.Color.brand_red())
        embed.set_thumbnail(url=offender.avatar.url)
        embed.add_field(name="The Crew Must Vote", value="React with ✅ to vote yes, and ❎ to vote no")
        message = await ctx.send(embed=embed)
        await message.add_reaction('❎')
        await message.add_reaction('✅')
        await sleep(45)
        cache_msg = discord.utils.get(self.bot.cached_messages, id=message.id)
        most_voted = max(cache_msg.reactions, key=lambda r: r.count)
        no_votes = cache_msg.reactions[0].count
        yes_votes = cache_msg.reactions[1].count
        if yes_votes > no_votes:
            brigged_embed = discord.Embed(title=f"{offender} has been brigged and stripped of all roles!", color=discord.Color.dark_orange())
            brigged_embed.set_thumbnail(url='https://www.pngkey.com/png/full/7-76501_jail-clipart-internment-camp-im-the-daddy-coffee.png')
            await self.strip_roles(offender)
            await ctx.send(embed=brigged_embed)
        elif no_votes == yes_votes:
            # Tie!
            tie_embed = discord.Embed(title=f"Vote was a tie - {offender} goes free!", color=discord.Color.green())
            tie_embed.set_thumbnail(url=offender.avatar.url)
            await ctx.send(embed=tie_embed)
        print(most_voted)

    async def strip_roles(self, user: discord.Member):
        for i in user.roles:
            try:
                await user.remove_roles(i)
            except:
                print(f"Can't remove the role {i}")

async def setup(bot):
    await bot.add_cog(Poll(bot))