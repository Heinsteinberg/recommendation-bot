import discord
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
    history = await client.get_channel(article2ID).history().flatten()
    for article in history:
        contentID = str(article.content).split('\n')[0]
        recommendedLst.append(contentID)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id == article1ID:
        print(recommendedLst)

        if str(reaction.message.id) in recommendedLst:
            return None
        recommendedLst.append(str(reaction.message.id))
        channel = client.get_channel(article2ID)
        mesg = str(reaction.message.id) + '\n'
        mesg += 'Author : ' + str(reaction.message.author) + '\n'
        mesg += 'Recommended by : ' + str(user) + '\n'
        mesg += 'Content : ' + str(reaction.message.content) + '\n'
        await channel.send(mesg)

client.run(TOKEN)