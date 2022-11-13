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
    negative_embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/619699978498998294/1041459549577678949/gavel.png')
    negative_embed.add_field(name=f"{offender} has avoided the chopping block", value=".")
    return negative_embed

def generate_tie_embed(offender):
    tie_embed = discord.Embed(title=f"The Crew Is Indifferent", color=discord.Color.yellow())
    tie_embed.set_thumbnail(url=offender.avatar.url)
    tie_embed.add_field(name=f"{offender} did not warrant enough of a threat to sway the crew", value=".")
    return tie_embed

def generate_idea_embed(idea):
    idea_embed = discord.Embed(title=f"The Crews Orders...", color=discord.Color.yellow())
    idea_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/619699978498998294/1041458966573613207/penguins.png")
    idea_embed.add_field(name=idea['name'], value=idea['desc'])
    return idea_embed

def generate_sink_embed(boatname):
    boatname = boatname if boatname is not None else "Unnamed Ship"
    idea_embed = discord.Embed(title="Another Crew Fucked Around and Found Out", color=discord.Color.green())
    idea_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/619699978498998294/1041473586818469998/sinking.png")
    idea_embed.add_field(name=boatname, value="Another crew falls victim to the feared crew of the Black Sieve!")
    return idea_embed

def generate_sink_count_embed(count):
    if count == 1:
        msg = f"{count} Boat Has Fucked Around and Found Out"
    else:
        msg = f"{count} Boats Have Fucked Around and Found Out"
    idea_embed = discord.Embed(title=msg, color=discord.Color.green())
    idea_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/619699978498998294/1041476781556895825/pirate.png")
    return idea_embed