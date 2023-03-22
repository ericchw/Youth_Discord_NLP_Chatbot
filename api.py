import os, discord, requests
from turtle import title
from discord.ui import Button, View, button, Modal, InputText, Select
import discord
responses= {}
intents = discord.Intents.default()
from flask import Flask
app = Flask(__name__)
bot = discord.Bot(debug_guilds=["995158826347143309"], intents=intents)

# Define a route for the bot to send a "hi" message
@app.route('/hi')
def say_hi():
    #channel = bot.get_channel(996710862146523136)  # Replace with your Discord channel ID
    #channel.send('Hi!')
    return 'Hi sent!'

# Run the Flask app and start the Discord bot
if __name__ == '__main__':
    #bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")
    app.run()