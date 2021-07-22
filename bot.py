import discord
import random
import os

client = discord.Client()
TOKEN = os.environ.get('TOKEN')
article1ID = 736438894551236710 # 전체글 channel id
article2ID = 794911922889031720 # 개념글 channel id
recommendedLst = []

@client.event
async def on_ready():
    print('Initiating \'%s\'' % client.user.name)
    await client.change_presence(status=discord.Status.online, activity=None)
    await client.user.edit(username='개추봇🎭')
    history = await client.get_channel(article2ID).history().flatten()
    for article in history:
        if article.embeds:
            recommendedLst.append(article.embeds[0].footer.text)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id == article1ID:
        if str(reaction.message.id) in recommendedLst:
            return None
        recommendedLst.append(str(reaction.message.id))
        embed = discord.Embed(title=reaction.message.content, colour=random.randint(0, 0XFFFFFF))
        embed.set_author(name=reaction.message.author.name, icon_url=reaction.message.author.avatar_url)
        embed.add_field(name='Recommended by', value=user.name, inline=False)
        embed.set_footer(text=str(reaction.message.id))
        await client.get_channel(article2ID).send(embed=embed)

client.run(TOKEN)