from logging import PlaceHolder
import os, discord, requests
from turtle import title
from discord.ui import Button, View, button, Modal, InputText, Select
from emotiontest import emtransform
import chat, faq
from bs4 import BeautifulSoup

responses= {}
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

@bot.command()  #https://www.youtube.com/watch?v=56XoybDajjA&t=487s
async def hello(ctx):
    select1 = Select( 
        min_values=2,
        max_values=4,
        placeholder= "Choose a game",
        options = [
        discord.SelectOption(
            label="Apex", 
            description="Apex",
            ),
        discord.SelectOption(
            label="Rainbow_six", 
            description="Rainbow Six Seige",
            default= True),
        discord.SelectOption(
            label="pubg", 
            description="PUBG (COMP)",
            ),
        discord.SelectOption(
            label="brawlhalla", 
            description="Brawlhalla",
            ),
        discord.SelectOption(
            label="others", 
            description="Others",
            )

    ],
    row = 2)
    select2 = Select( 
        placeholder= "Choose a game",
        options = [
        discord.SelectOption(
            label="Apex", 
            description="Apex",
            default= True),
        discord.SelectOption(
            label="Rainbow_six", 
            description="Rainbow Six Seige")
    ])
    async def my_callback(interaction):
        select1.disabled = True
        if "others"  in select1.values:
            select1.add_option()
            select1.append_option(discord.SelectOption(
            label="new_game_1", 
            description="New Game_1",
            ))
        await interaction.response.send_message(f"Game chosen: {select1.values}")
    select1.callback = my_callback
    # select.callback = my_callback
    view = View()
    view.add_item(select1)
    view.add_item(select2)
    await ctx.send("Choose a game", view = view)


@bot.event
async def on_message(message):
    print(message)
    #type=<MessageType.application_command: 20>
    if(message.type[1]==20):
        await message.add_reaction('✅')
    if(message.author.name!='CyberU'):
        text=message.content
        ans=emtransform(text)
        # print(ans)
        # ans=chat.outp(ans)
        string = faq.faq(message.content)
        if string != None:
            await message.channel.send(string)
        if 'working hours' in message.content:
            await message.channel.send(file=discord.File('5ee1ae88efa3e739.png'))
        if ans[0]['label'] == 'sadness':
            user = message.author
            embed = discord.Embed(title="Select an option", color=discord.Color.blue())
            embed.add_field(name="👍", value="Agree", inline=True)
            embed.add_field(name="👎", value="Disagree", inline=True)
            # msg = await user.send( "你感覺如何啊？需要幫你轉介去社工嗎？")
            message_to_send = await user.send(embed=embed)
            await message_to_send.add_reaction("👍")
            await message_to_send.add_reaction("👎")
            responses[user.id] = None
            # await msg.add_reaction("👍")
            # await user.respond("Hello!", view=MyView())
            global user_id
            user_id = user.id
        elif message.channel.type == discord.ChannelType.private:
        # check if the message is from the user you are expecting a response from
            if message.author.id == user_id:
                # handle the user's response
                response = message.content
                print(response)
        # await message.channel.send(ans) 

@bot.event
async def on_reaction_add(reaction, user):
    # check if the user's id is in the dictionary
    if user.id in responses:
        if str(reaction) == "👍":
            responses[user.id] = "Agree"
        elif str(reaction) == "👎":
            responses[user.id] = "Disagree"
        # print the user's response
        print(f'{user.name} responded with {responses[user.id]}')
bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")