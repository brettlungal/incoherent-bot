import discord

def generate_vote_embed(offender):
    embed = discord.Embed(title=f"{offender} Has Been Voted To The Brig!", color=discord.Color.brand_red())
    embed.set_thumbnail(url=offender.avatar.url)
    embed.add_field(name="The Crew Must Vote", value="React with ✅ to vote yes, and ❎ to vote no")
    return embed

def generate_brigged_embed(offender):
    brigged_embed = discord.Embed(title="The Tribe Has Spoken", color=discord.Color.dark_orange())
    brigged_embed.set_thumbnail(url='https://www.pngkey.com/png/full/7-76501_jail-clipart-internment-camp-im-the-daddy-coffee.png')
    brigged_embed.add_field(name=f"{offender} has been brigged and stripped of all roles!", value=".")
    return brigged_embed

def generate_negative_vote_embeded(offender):
    negative_embed = discord.Embed(title="Mercy Has Been Shown", color=discord.Color.green())
    negative_embed.set_thumbnail(url='https://www.clipartmax.com/png/small/231-2315140_the-gallery-for-gavel-clipart-transparent-judge-gavel-png.png')
    negative_embed.add_field(name=f"{offender} has avoided the chopping block", value=".")
    return negative_embed

def generate_tie_embed(offender):
    tie_embed = discord.Embed(title=f"The Crew Is Indifferent", color=discord.Color.yellow())
    tie_embed.set_thumbnail(url=offender.avatar.url)
    tie_embed.add_field(name=f"{offender} did not warrant enough of a threat to sway the crew", value=".")
    return tie_embed