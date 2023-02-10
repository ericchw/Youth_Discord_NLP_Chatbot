import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = discord.Bot(debug_guilds=["995158826347143309"], intents=intents) 
#event
@bot.command(name="create_event")  #https://www.youtube.com/watch?v=56XoybDajjA&t=487s
async def event(ctx):
    embed = discord.Embed(
        title="Event",
        description="1:Apex\n2:LOL\n3:PUBG",
        color=discord.Color.red()
    )

    message = await ctx.send(embed=embed)

    await message.add_reaction("✅")
    await message.add_reaction("❌")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["✅", "❌"]

    try:
        reaction, user = await bot.wait_for("reaction_add", check=check, timeout=60.0)
    except :
        await message.clear_reactions()
    else:
        if str(reaction.emoji) == "✅":
            await ctx.send("The ✅ button was pressed.")
        elif str(reaction.emoji) == "❌":
            await ctx.send("The ❌ button was pressed.")

bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")