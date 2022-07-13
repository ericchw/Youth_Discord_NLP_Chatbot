import nextcord
import chat


intents = nextcord.Intents.all()

client = nextcord.Client(intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if(message.author.name!='2try'):
        ans=chat.outp(message.content)
        await message.channel.send(ans) 


 

client.run("OTk0ODk4OTcwMDg4MzA4NzQ2.Gr1OXL.RDU1J9Qxw7l5vmWpOiZoHN8tDEz6u6HO8m_aa0")