import requests
import json
import discord
from io import BytesIO
from PIL import Image
from datetime import datetime, timezone, timedelta
import asyncio

timezone_offset = timedelta(hours=8)
# Define the Facebook page and Discord channel IDs
FB_PAGE_ID = "117562637973323"
DISCORD_CHANNEL_ID = "1097177783970578473"

# Define the Facebook Graph API endpoint and access token
FB_ENDPOINT = f"https://graph.facebook.com/{FB_PAGE_ID}/feed"
FB_ACCESS_TOKEN = "EAACDMpcEwCIBAFjYT25GGIl7j0KV4ZCdY7WBiIQJ3b08WK6mYZBzkufCoBFk455vdnGImUsxHkfvmUXZBrGWkFbo0gY9j4gRFWr7rIB3fLK1cAbE4Ox9CpTCjlaYUZB0EJpqq6iex2ZAVukYKZCfX6ioCaFCqzpDZCIaJkHiv3l6YKp2FR7awDmaVN1ost5ZBHDuSpqonbJXBf7EAZBTXmszW"#"<insert Facebook access token here>"

# Initialize the PyCord client and log in
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot(intents=intents)
bot_token = "OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk"

# Initialize the last post time to None
last_post_time = None

# Define a function to send the Facebook post to the Discord channel
async def send_facebook_post():
    global last_post_time
    while True:
        # Make a GET request to the Facebook Graph API to retrieve the latest post
        params = {
            "access_token": FB_ACCESS_TOKEN,
            "fields": "message,created_time,attachments",
            "limit": 1
        }
        response = requests.get(FB_ENDPOINT, params=params)
        # Check if the response is valid
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.reason}")
            return

        data = json.loads(response.text)

        # Extract the message and created_time fields from the Facebook post
        message = data["data"][0]["message"]
        created_time = data["data"][0]["created_time"]
        created_time_datetime = datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S+0000") + timezone_offset
        formatted_created_time = created_time_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Check if the post is new
        if last_post_time is None or created_time_datetime > last_post_time:
            print("last_post_time is None or created_time_datetime > last_post_time")
            # Extract the attachment information from the Facebook post
            attachments = data["data"][0]["attachments"]["data"] if "attachments" in data["data"][0] else []

            channel = await bot.fetch_channel(DISCORD_CHANNEL_ID)

            # Create the message content with the post text and timestamp
            facebookLinkId = data['data'][0]['id']
            content = f"Latest Facebook post ({formatted_created_time}):\n{message}\nhttps://www.facebook.com/{facebookLinkId}"

            # Check if the post has any attachments (i.e., photos or videos)
            if len(attachments) > 0:
                # Extract the URL of the first attachment
                attachment_url = attachments[0]["media"]["image"]["src"]

                # Download the attachment and create a PIL Image object
                response = requests.get(attachment_url)
                image = Image.open(BytesIO(response.content))

                # Save the image to a BytesIO object and attach it to the Discord message
                image_bytes = BytesIO()
                image.save(image_bytes, format=image.format)
                image_bytes.seek(0)
                file = discord.File(fp=image_bytes, filename="attachment.png")
                await channel.send(file=file, content=content)
            else:
                # If there are no attachments, just send the message text
                await channel.send(content)

            # Update the last post time
            last_post_time = created_time_datetime
        else:
            print("last post posted already")
        await asyncio.sleep(10)

# Define the on_ready event handler to send the Facebook post when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    await send_facebook_post()

# Start the bot
bot.run(bot_token)