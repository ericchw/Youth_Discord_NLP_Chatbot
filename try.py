import os, discord, requests
from turtle import title
from discord.ui import Button, View, button, Modal, InputText, Select
import discord
responses= {}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
event=""
time=""
member=""
bot = discord.Bot(debug_guilds=["995158826347143309"], intents=intents) # specify the guild IDs in debug_guilds

# event handler for when the bot is ready
@bot.event
async def on_ready():
    print('Logged in as', bot.user.name)
    print('------')
    event = bot.get_channel(1079610659647520849)
    await event.send("有個人需要幫手，麻煩請關注")

@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        if interaction.data['custom_id'] == 'yes':
            await interaction.response.send_message('You voted yes!')
        elif interaction.data['custom_id'] == 'no':
            await interaction.response.send_message('You voted no!')



# start the bot
bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")


