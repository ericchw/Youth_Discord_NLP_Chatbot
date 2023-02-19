import os
import discord
import chat
from discord.ui import Button, View, button
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_ID')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# specify the guild IDs in debug_guilds
bot = discord.Bot(debug_guilds=[GUILD], intents=intents)

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


# this decorator makes a slash command
@bot.command(description="Sends the bot's latency.")
async def ping(ctx):  # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")


@bot.command()
async def button(ctx):  # a slash command will be created with the name "ping"
    await ctx.respond("Hello!", view=MyView())

# eric test


@bot.event
async def on_message(message):
    if message.content == "hi":
        await message.channel.send("hello", reference=message)


bot.run(TOKEN)
