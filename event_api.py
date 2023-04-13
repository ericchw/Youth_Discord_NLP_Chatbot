import discord
from discord.ext import commands
from flask import Flask, redirect, url_for, render_template_string
from flask_discord_interactions import DiscordInteractions
import requests
import json
app = Flask(__name__)

app.config["DISCORD_BOT_TOKEN"] = "OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk"                    # Required to access BOT resources.


@app.route("/create_event/<string:primary_key>")
def create_event(primary_key):
    headers = {
        "Authorization": f"Bot {app.config['DISCORD_BOT_TOKEN']}",
        "Content-Type": "application/json"
    }

    data = {
        "content": f"**No: {primary_key}**",
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "Join",
                        "style": 4,
                        "custom_id": "join"
                    }
                ]
            }
        ],
        "embeds": [
            {
                "title": "Example Embed",
                "description": "This is an example embed.",
                "color": 16711680
            }
        ]
    }

    response = requests.post("https://discord.com/api/channels/996710862146523136/messages", headers=headers, json=data)
    return response.json()


@app.route("/send_message/<string:recipient_id>/<string:content>")
def send_private_message(recipient_id,content):
    # Define the API endpoint and headers
    url = "https://discord.com/api/users/@me/channels"
    headers = {
        "Authorization": f"Bot {app.config['DISCORD_BOT_TOKEN']}",
        "Content-Type": "application/json"
    }

    # Define the data to be sent in the API request
    data = {
        "recipient_id": recipient_id,
        "content": content
    }

    # Send the API request to create a DM channel with the user
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Parse the response JSON and extract the channel ID
    response_json = response.json()
    channel_id = response_json["id"]

    # Define the API endpoint for sending a message and update the headers
    url = f"https://discord.com/api/channels/{channel_id}/messages"
    headers["Content-Type"] = "application/json"

    # Define the data to be sent in the API request
    data = {
        "content": content
    }

    # Send the API request to send the message to the user
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)