from logging import PlaceHolder
import os, discord, requests
from turtle import title
from discord.ui import Button, View, button, Modal, InputText, Select


responses= {}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
event=""
time=""
member=""
bot = discord.Bot(debug_guilds=["995158826347143309"], intents=intents) # specify the guild IDs in debug_guilds
@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")
#event
@bot.command(name="create_event")  #https://www.youtube.com/watch?v=56XoybDajjA&t=487s
async def event(ctx):
    sle_event = Select( 
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
    time = Select( 
        placeholder= "Choose a time",
        options = [
        discord.SelectOption(
            label="morning", 
            description="morning",
            default= True),
        discord.SelectOption(
            label="afternoon",  
            description="afternoon",),
        discord.SelectOption(
            label="night",  
            description="night")
    ])
    join=Button(label="join!", style=discord.ButtonStyle.red)
    view = View()
    view.add_item(sle_event)
    view.add_item(time)
    view.add_item(join)

    message=join.interaction.response.send_message(f"New poll:{sle_event.values[0]} \n✅ = Yes**\n**❎ = No**")
    await message.add_reaction('❎')
    await message.add_reaction('✅')
    await ctx.send("Choose a game", view = view)

    bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")