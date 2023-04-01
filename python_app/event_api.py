import discord, psycopg2
from discord.ext import commands
from flask import Flask, redirect, url_for, render_template_string
from flask_discord_interactions import DiscordInteractions
from datetime import datetime
import requests
app = Flask(__name__)

app.config["DISCORD_BOT_TOKEN"] = "OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk"                    # Required to access BOT resources.

discord = DiscordInteractions(app)

@app.route("/create_event/<string:primary_key>")
def create_event(primary_key):
    connection = psycopg2.connect(user="admin",
                                password="admin",
                                host="db",
                                port="5432",
                                database="sjs")
    cursor = connection.cursor()
    cursor.execute(f'SELECT evttitle,atyid, evtlimitmem,evtdesc,evtdate, evtdeadline, evtupdatedate FROM event where evtid = {primary_key}')
    record = cursor.fetchall()
    cursor.execute(f'SELECT atyname FROM activity where atyid = {record[0][1]}')
    activity = cursor.fetchall()
    print(record, activity)
    print("PostgreSQL connection is established.")

    testing = [primary_key, {record[0][6]}]
    headers = {
        "Authorization": f"Bot {app.config['DISCORD_BOT_TOKEN']}",
        "Content-Type": "application/json"
    }

    data = {
        "content": f"**Event: {primary_key}\nEvent last Updated: {record[0][6]}**",


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
        
        'embeds':[
            {
                "description" :f"{record[0][3]}",
                "title" : f"{activity[0][0]}",
                "color": 0x4CAF50,
                "fields": [
                    {
                        "name": "Number of people",
                        "value": f"{record[0][2]}",
                        "inline": False # This determines whether the field is displayed inline or not
                    },
                    {
                        "name": "Date:",
                        "value": f"{record[0][4]}",
                        "inline": True
                    }
                ],
                 "footer": {
                    "text": f"Submission Dateline: {record[0][5]}"
                }
            }
        ]
    }


    response = requests.post("https://discord.com/api/channels/996710862146523136/messages", headers=headers, json=data)

    return response.json()





if __name__ == "__main__":
    print('testing in python')
    app.run(debug=True, port=80, host='0.0.0.0')