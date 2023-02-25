import random
import jieba

# load dataset
import json
with open('data.json', 'r',encoding='utf-8') as f:
    intents = json.load(f)

bot.event_variable1 = ""
bot.event_variable2 = ""
bot.event_variable3 = ""

# define a function to get the response
def get_response(input_text):
    # tokenize the input text
    tokens = jieba.lcut(input_text)
    # find matching patterns
    matching_patterns = []
    for token in tokens:
        if token in patterns:
            matching_patterns.extend(patterns[token])
    # select a random response from the matching patterns
    if matching_patterns:
        tag = random.choice(matching_patterns)
        for intent in intents['intents']:
            if intent['tag'] == tag:
                response = random.choice(intent['responses'])
                return response
    else:
        return "對不起，我不太明白你的意思。"

class Event(View):
    @button(label="1:Apex", style=discord.ButtonStyle.blurple)
    async def callback1(self, button, interaction):
        if bot.event_variable1.find(str(interaction.user))<0:
            bot.event_variable1=bot.event_variable1+str(interaction.user)+"\n"
        await interaction.response.edit_message(content=f"List:\n1.Apex:\n{bot.event_variable1}\n2.LOL:\n{bot.event_variable2}\n3.PUBG:\n{bot.event_variable3}\nPlease select ", view=self)
    @button(label="2:LOL", style=discord.ButtonStyle.green)
    async def callback2(self, button, interaction):
        if bot.event_variable2.find(str(interaction.user))<0:
            bot.event_variable2=bot.event_variable2+str(interaction.user)+"\n"
        await interaction.response.edit_message(content=f"List:\n1.Apex:\n{bot.event_variable1}\n2.LOL:\n{bot.event_variable2}\n3.PUBG:\n{bot.event_variable3}\nPlease select ", view=self)
    @button(label="3:PUBG", style=discord.ButtonStyle.red)
    async def callback3(self, button, interaction):
        if bot.event_variable3.find(str(interaction.user))<0:
            bot.event_variable3=bot.event_variable3+str(interaction.user)+"\n"
        await interaction.response.edit_message(content=f"List:\n1.Apex:\n{bot.event_variable1}\n2.LOL:\n{bot.event_variable2}\n3.PUBG:\n{bot.event_variable3}\nPlease select ", view=self)


#event
@bot.command(name="create_event")  #https://www.youtube.com/watch?v=56XoybDajjA&t=487s
async def event(ctx):
    embed = discord.Embed(
        title="Event",
        description="1:Apex\n2:LOL\n3:PUBG",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)
    await ctx.send("List:\nPlease select ", view=Event())


bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")
