import discord, psycopg2, json
from discord.ext import commands
from flask import Flask, redirect, url_for, render_template_string
from flask_discord_interactions import DiscordInteractions
from datetime import datetime
import requests
import logging
import sys
import time


# create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a console handler
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

# create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(handler)

app = Flask(__name__)

app.config["DISCORD_BOT_TOKEN"] = "OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk"                    # Required to access BOT resources.

discord = DiscordInteractions(app)

@app.route("/create_event/<string:primary_key>")
def create_event(primary_key):
    start_time = time.time()
    connection = psycopg2.connect(
        host="db",
        port="5432",
        database="sjs",
        user="admin",
        password="admin",
    )
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
        "content": f"**Event last Updated: {record[0][6]}**",
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "label": "Apply",
                        "style": 4,
                        "custom_id": f"{primary_key}|join"
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
    response = requests.post("https://discord.com/api/channels/1079031912682766406/messages", headers=headers, json=data)
    end_time = time.time()
    execution_time = end_time - start_time
    logger.debug(f"Execution time: {execution_time} seconds")

    return response.json()

@app.route("/send_message/<string:event_id>")
def send_private_message(event_id):
    # Define the API endpoint and headers
    connection = psycopg2.connect(
        host="db",
        port="5432",
        database="sjs",
        user="admin",
        password="admin",
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT polldcid, polldcusername, pollstatus FROM polling where pollstatus = 'Accepted' or pollstatus = 'Rejected' and evtid = {event_id}")
    record = cursor.fetchall()
    cursor.execute(f'SELECT * FROM event where evtid = {event_id}')
    activity = cursor.fetchall()
    
    print(f'record is :{record[0]}')
    print(f'activity name is: {activity}')
    for x in record:
        print (x)
        string = ''
        if x[2] == 'Rejected':
            string = f"{x[1]}, we are apologize that we are unable to accept your application for {activity[0][2]}. Hope you can join for our future events."
            url = "https://discord.com/api/users/@me/channels"
            headers = {
                "Authorization": f"Bot {app.config['DISCORD_BOT_TOKEN']}",
                "Content-Type": "application/json"
            }

            # Define the data to be sent in the API request
            data = {
                "recipient_id": x[0],
                "content": "temp",
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
                "content": f"{string}",
            }

            # Send the API request to send the message to the user
            response = requests.post(url, headers=headers, data=json.dumps(data))
        else:
            string = f"{x[1]}, you have successfully joined {activity[0][2]}"
            url = "https://discord.com/api/users/@me/channels"
            headers = {
                "Authorization": f"Bot {app.config['DISCORD_BOT_TOKEN']}",
                "Content-Type": "application/json"
            }

            # Define the data to be sent in the API request
            data = {
                "recipient_id": x[0],
                "content": "temp",
                "components": [
                    {
                        "type": 1,
                        "components": [
                            {
                                "type": 2,
                                "label": "Confirm",
                                "style": 4,
                                "custom_id": f"{activity[0][0]}|event_confirmation",
                            }
                        ]
                    }
                ],
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
                "content": f"{string}",
                "components": [
                    {
                        "type": 1,
                        "components": [
                            {
                                "type": 2,
                                "label": "Confirm",
                                "style": 4,
                                "custom_id": f"{activity[0][0]}|event_confirmation",
                            }
                        ]
                    }
                ],
            }

            # Send the API request to send the message to the user
            response = requests.post(url, headers=headers, data=json.dumps(data))
            

        
    return response.json()
    

if __name__ == "__main__":
    print('testing in python')
    app.run(debug=True, port=80, host='0.0.0.0')