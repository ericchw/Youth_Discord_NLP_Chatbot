from logging import PlaceHolder
import os, discord
from turtle import title
from discord.ui import Button, View, button, Modal, InputText
import emotion
import chat

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
event=""
time=""
member=""
bot = discord.Bot(debug_guilds=["995158826347143309"], intents=intents) # specify the guild IDs in debug_guilds

# since global slash commands can take up to an hour to register,
# we need to limit the guilds for testing purposes

class MyView(View):
    @button(label="Button 1", style=discord.ButtonStyle.blurple, emoji="😊")
    async def callback1(self, button, interaction):
        await interaction.response.edit_message(content=f"Hi from Button 1", view=self)
        await interaction.followup.send(f"This is a followup message from Button 1.")

    @button(label="Button 2", style=discord.ButtonStyle.green, emoji="😊")
    async def callback2(self, button, interaction):
        await interaction.response.send_message(f"Hi from Button 2")
        await interaction.followup.send(f"This is a followup message from Button 2.")

    @button(label="Button 3", style=discord.ButtonStyle.red, emoji="😊")
    async def callback3(self, button, interaction):
        await interaction.response.send_message(f"Hi from Button 3")
        await interaction.followup.send(f"This is a followup message from Button 3.")

class EventModel(Modal):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.add_item(InputText(
            label="Event type:",
            placeholder="Event_type"
            ))
        self.add_item(InputText(
            label="Date & time:",
            placeholder="d&t"
            ))
        self.add_item(InputText(
            label="Minium members:",
            placeholder="members"
            ))
    async def callback(self,interaction:discord.InputText):
        embed=discord.Embed(title="User Details",color=discord.Colour.brand_red())
        embed.add_field(name="Event_type",value=self.children[0].value,inline=False)
        embed.add_field(name="d&t",value=self.children[1].value,inline=False)
        embed.add_field(name="members",value=self.children[2].value,inline=False)
        m=await interaction.response.send_message(embed=embed)
        
        





@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")


@bot.command()
async def button2(ctx): # a slash command will be created with the name "ping"
    await ctx.respond("Hello!", view=MyView())
#event
@bot.command(name="create_event")
async def event(ctx):
    modal=EventModel(title="Create a Event")
    await ctx.send_modal(modal)
    






#polling
@bot.command()
async def poll(ctx, *, question):
    #limit of polling
    await ctx.channel.purge(limit=2)
    message = await ctx.send(f"New poll: \n✅ = Yes**\n**❎ = No**")
    await message.add_reaction('❎')
    await message.add_reaction('✅')


@bot.event
async def on_message(message):
    print(message)
    #type=<MessageType.application_command: 20>
    if(message.type[1]==20):
        await message.add_reaction('✅')
    if(message.author.name!='CyberU'):
        ans=chat.outp(message.content)
        await message.channel.send(ans) 

bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")