from logging import PlaceHolder
import os, discord, time, re
from turtle import title
from discord.ui import Button, View, button, Modal, InputText, Select
from discord.ext import commands
from emotiontest import emtransform
import chinese
import langid
import chat
from db import connectDB, initiate
from datetime import datetime, timezone, timedelta
import random

responses= {}
polling = [[1,[]],[2,[]],[3,[]],[4,[]],[5,[]],[6,[]],[7,[]],[8,[]],[9,[]],[10,[]]]
dateline = False
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
cevent = []
member=""
bot = discord.Bot(debug_guilds=["995158826347143309"], intents=discord.Intents.all()) # specify the guild IDs in debug_guilds
# bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
channel_id = 1060512412299710504

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
        
#event
bot.event_variable1 = ""
bot.event_variable2 = ""
bot.event_variable3 = ""
bot.event_name=[]

class Event(View):
    @button(label="League of Legends", style=discord.ButtonStyle.blurple)
    async def callback1(self, button, interaction):
        for i in polling[1][1]:
            bot.event_variable1=bot.event_variable1+i
        if bot.event_variable1.find(str(interaction.user))<0:
            if dateline == False:
                polling[1][1].append(interaction.user.name)
                flat_list = [item for sublist in polling for item in sublist]
                str_list = [str(item) for item in flat_list]
                temp_list = [item.strip("[]") if "[" in item else item for item in str_list]
                my_string = ",".join(temp_list)
                my_string = my_string.replace("'", "")
                bot.event_name=polling
                event_det_id = connectDB(f"SELECT edtlhdrid from event_detail WHERE edtlhdrid = {cevent[0][0]}", "r")
                if len(event_det_id[1]) == 0:
                    connectDB(f"INSERT INTO event_detail VALUES (DEFAULT, '{cevent[0][0]}', '{my_string}')", "i") 
                else:
                    connectDB(f"UPDATE event_detail SET edtlvotedtl = '{my_string}'  WHERE edtlhdrid = {cevent[0][0]}", "u")
            bot.event_variable1=bot.event_variable1+str(interaction.user)+"\n"
        await interaction.response.edit_message(content=f"List:\n1.{bot.event_name[1][0]}:\n{polling[1][1]}\n2.{bot.event_name[2][0]}:\n{polling[2][1]}\n3.{bot.event_name[3][0]}:\n{polling[3][1]}\nPlease select", view=self)
    @button(label="Apex Leagues", style=discord.ButtonStyle.green)
    async def callback2(self, button, interaction):
        for i in polling[2][1]:
            bot.event_variable2=bot.event_variable2+i
        if bot.event_variable2.find(str(interaction.user))<0:
            if dateline == False:
                polling[2][1].append(interaction.user.name)
                flat_list = [item for sublist in polling for item in sublist]
                str_list = [str(item) for item in flat_list]
                temp_list = [item.strip("[]") if "[" in item else item for item in str_list]
                my_string = ",".join(temp_list)
                my_string = my_string.replace("'", "")
                bot.event_name=polling
                event_det_id = connectDB(f"SELECT edtlhdrid from event_detail WHERE edtlhdrid = {cevent[0][0]}", "r")
                if len(event_det_id[1]) == 0:
                    connectDB(f"INSERT INTO event_detail VALUES (DEFAULT, '{cevent[0][0]}', '{my_string}')", "i") 
                else:
                    connectDB(f"UPDATE event_detail SET edtlvotedtl = '{my_string}'  WHERE edtlhdrid = {cevent[0][0]}", "u")
            bot.event_variable2=bot.event_variable2+str(interaction.user)+"\n"
        await interaction.response.edit_message(content=f"List:\n1.{bot.event_name[1][0]}:\n{polling[1][1]}\n2.{bot.event_name[2][0]}:\n{polling[2][1]}\n3.{bot.event_name[3][0]}:\n{polling[3][1]}\nPlease select", view=self)
    @button(label="Fall Guys", style=discord.ButtonStyle.red)
    async def callback3(self, button, interaction):
        for i in polling[3][1]:
            bot.event_variable3=bot.event_variable3+i
        if bot.event_variable3.find(str(interaction.user))<0:
            if dateline == False:
                polling[3][1].append(interaction.user.name)
                flat_list = [item for sublist in polling for item in sublist]
                str_list = [str(item) for item in flat_list]
                temp_list = [item.strip("[]") if "[" in item else item for item in str_list]
                my_string = ",".join(temp_list)
                my_string = my_string.replace("'", "")
                bot.event_name=polling
                #print(polling[1][1])
                event_det_id = connectDB(f"SELECT edtlhdrid from event_detail WHERE edtlhdrid = {cevent[0][0]}", "r")
                if len(event_det_id[1]) == 0:
                    connectDB(f"INSERT INTO event_detail VALUES (DEFAULT, '{cevent[0][0]}', '{my_string}')", "i") 
                else:
                    connectDB(f"UPDATE event_detail SET edtlvotedtl = '{my_string}'  WHERE edtlhdrid = {cevent[0][0]}", "u")
            bot.event_variable3=bot.event_variable3+str(interaction.user)+"\n"
        await interaction.response.edit_message(content=f"List:\n1.{bot.event_name[1][0]}:\n{polling[1][1]}\n2.{bot.event_name[2][0]}:\n{polling[2][1]}\n3.{bot.event_name[3][0]}:\n{polling[3][1]}\nPlease select", view=self)
@bot.command(name="create_event")  #https://www.youtube.com/watch?v=56XoybDajjA&t=487s
async def event(ctx):
    embed = discord.Embed(
        title="Event",
        description="1:Apex\n2:LOL\n3:PUBG",
        color=discord.Color.red()
    )
    # print(event)
    await ctx.send(embed=embed)
    # bot.loop.create_task(my_function(ctx))
    # connectDB(f"INSERT INTO event_header VALUES (DEFAULT, '{embed.title}', '{'voting'}', '{embed.description}', '{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}', '{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}')", "u")
    await ctx.send(f"List:\n1.Apex:\n{bot.event_variable1}\n2.LOL:\n{bot.event_variable2}\n3.PUBG:\n{bot.event_variable3}\nPlease select", view=Event())



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    # initiate()
        

    
        
    

    
@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")


@bot.command()
async def button2(ctx): # a slash command will be created with the name "ping"
    await ctx.respond("Hello!", view=MyView())
#check eng
def is_english(text):
    lang, _ = langid.classify(text)
    return lang == 'en'

@bot.event
async def on_message(message):
    print(message)
    if(message.author.name!='CyberU'):
        text=message.content
        emotion=emtransform(text)
        text = text.replace("'", "''")
            #SQL: insert data (user input message and NLP label but not value -> emotion[0]['label'])
        print(datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
        connectDB(f"INSERT INTO chatlog VALUES (DEFAULT, '{message.author.name}', '{message.author.id}', '{text}', '{emotion['label']}', '{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}')", "u")
        # print(ans)
        print(text)
        if is_english(text):
            ans=chat.outp(text)
        else:
            ans=chinese.get_response(text)

        
        # print(ans)
        if ans:
            # ans can be SQL statement for FAQ or string in intents.json, if string will output, if SQL statement will connect datebase to get data and return.
            # print(type(ans))
            if type(ans) == str:
                if(message.channel.name=='faq'):
                    await message.channel.send(ans)
                    connectDB(f"INSERT INTO chatlog VALUES (DEFAULT, '{'bot'}', '{'bot'}', '{ans}', '{'bot'}', '{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}')", "u")
            else:
                # print(ans.keys())
                for key in ans.keys():
                    if key == 'sql':
                        # print(key)
                        val1 = connectDB(ans['sql'], "r")
                        res = []
                        temp = []
                        # print(val1[1])
                        for value in val1[1]:
                            for x in value:
                                #print(value)
                                temp.append(x)
                        for key in val1[0]:
                            # print(key)
                            for value in temp:
                                string = key.replace("name","名稱").replace("phonenumber","電話").replace("whatsapp","Whatsapp").replace("website","網站").replace("instagram","Instagram").replace("discord","Discord").replace("servicehours","服務時間") + ": " + value
                                res.append(string)
                                temp.remove(value)
                                break
                        # print(res)
                        res = "\n".join(res)
                        await message.channel.send(res)
                        connectDB(f"INSERT INTO chatlog VALUES (DEFAULT, '{'bot'}', '{'bot'}', '{res}', '{'query'}', '{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}')", "u")
                    # if key == 'serviceHours':
                    #     await message.channel.send(file=discord.File(ans))
        else:
            if emotion['label']== 'anger':
                string = "大家冷靜d"
                image = random.choice(['https://tenor.com/zh-HK/view/生氣-暴怒-愛生氣-no-跳舞-gif-14378133', 'https://tenor.com/zh-HK/view/angry-annoyed-dont-be-angry-calm-down-relax-gif-11818781'])
                await message.channel.send(string)
                await message.channel.send(image)
                # SQL: save message to database "大家冷靜d"
                connectDB(f"INSERT INTO chatlog VALUES (DEFAULT, '{'bot'}', '{'bot'}', '{string}', '{'solve'}', '{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}')", "u")
        # string = faq.faq(message.content)
        # if string != None:
        #     await message.channel.send(string)
        if 'working hours' in message.content:
            await message.channel.send(file=discord.File('5ee1ae88efa3e739.png'))
        if emotion['label'] == 'sadness':
            user = message.author
            embed = discord.Embed(title="你感覺如何啊？需要幫你轉介去社工嗎？", color=discord.Color.blue())
            # await bot.get_channel(int(channel_id)).send(embed=embed_announce)
            embed.add_field(name="👍", value="需要（你可回答'yes')", inline=True)
            embed.add_field(name="👎", value="不需要", inline=True)
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
                # if str(reaction) == "👍":
                #     responses[user.id] = "Agree"
                # elif str(reaction) == "👎":
                #     responses[user.id] = "Disagree"
                
                response = message.content
                # SQL: save message to database "需要/不需要"  (ANOTHER TABLE 1?)
                if response == 'yes':
                    sjsAdmin = bot.get_user(909806470416191518)
                    await sjsAdmin.send(f"{user.mention}於{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}同意尋求幫助，麻煩請關注")
                    # await user.send("你的")
                # print(type(response))
        
        
        # await message.channel.send(ans) 

@bot.event
async def on_reaction_add(reaction, user):
    # check if the user's id is in the dictionary
    # bug found to fix: DM and public like message also will redirect to socail worker
    message = reaction.message
    #TODO: here check reaction
    #1. IF CHECK discord channel, and check emoji is 'up' or 'down'
    if user.bot:
        return
    if reaction.message.channel.id == 1060512412299710504:
        # if reaction.emoji == "1️⃣":
        #     # Do something with the user's reaction
        #     if dateline == False:
        #         polling[0][1].append(user.name)
        #         flat_list = [item for sublist in polling for item in sublist]
        #         str_list = [str(item) for item in flat_list]
        #         temp_list = [item.strip("[]") if "[" in item else item for item in str_list]
        #         my_string = ",".join(temp_list)
        #         my_string = my_string.replace("'", "")

        #         # print(my_string)
        #         # edtlhdridInDB = connectDB(f"SELECT edtlhdrid from event_detail WHERE edtlhdrid = {cevent[0][0]}", "r")
        #         # if edtlhdridInDB == id:
        #         #     connectDB(f"UPDATE event_detail SET edtlvotedtl = {my_string}  WHERE edtlhdrid = {cevent[0][0]}", "u")
        #         # else:
        #         #     id = connectDB(f"INSERT INTO event_detail VALUES (DEFAULT, '{cevent[0][0]}', '{my_string}')", "i")
                
        #         event_det_id = connectDB(f"SELECT edtlhdrid from event_detail WHERE edtlhdrid = {cevent[0][0]}", "r")
        #         # connectDB(f"UPDATE event_detail SET edtlvotedtl = {my_string}  WHERE edtlhdrid = {cevent[0][0]}", "u")
        #         print(event_det_id)
        #         if len(event_det_id[1]) == 0:
        #             connectDB(f"INSERT INTO event_detail VALUES (DEFAULT, '{cevent[0][0]}', '{my_string}')", "i") 
        #         else:
        #             connectDB(f"UPDATE event_detail SET edtlvotedtl = {my_string}  WHERE edtlhdrid = {cevent[0][0]}", "u")
        #     print(f"{user.name} reacted with {reaction.emoji}")
        print(f"Outisde: {user.name} reacted with responses")
    if isinstance(message.channel, discord.DMChannel):
        if user.id in responses:
            if reaction.emoji == "👍":
                responses[user.id] = "Agree"
                # await user.send("Hello! This is a private message.")
                # send need help to social worker
                # sjsAdmin = bot.get_user(792305150429233152)
                sjsAdmin = bot.get_user(909806470416191518)
                # await sjsAdmin.send("有個人需要幫手，麻煩請關注")
                await sjsAdmin.send(f"{user.mention}於{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}同意尋求幫助，麻煩請關注")
                # await user.send("你的")
                connectDB(f"INSERT INTO helplog VALUES (DEFAULT, '{user.name}', '{user.id}', '{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}')", "u")
            elif str(reaction) == "👎":
                responses[user.id] = "Disagree"
            # print the user's response
            print(f'{user.name} responded with {responses[user.id]}')

@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        if interaction.data['custom_id'] == 'join':
            # Retrieve the message object
            channel = await bot.fetch_channel(interaction.channel_id)
            message = await channel.fetch_message(interaction.message.id)
            
            # Get the message content
            message_content = message.content
            eventid, latest_update = message_content.split("\n")[0][8:], message_content.split("\n")[1][16:-2]
            # print(eventid, latest_update)
            # eventid = message.content.split(maxsplit=1)[1]
            # print(f"event id is {eventid}")
            eventid = re.search(r'\d+', eventid).group()
            print(f"event info: {eventid}, {latest_update}")
            # latest_update = re.search(r'\d+', latest_update).group()
            update_checking = connectDB(f"select exists(select 1 from event where evtupdatedate='{latest_update}' and evtid = {eventid})", "r")
            # print(update_checking[1][0][0])
            checking = connectDB(f"select exists(select 1 from polling where polldcusername='{interaction.user}' and evtid = {eventid})", "r")
            timecheck = connectDB(f"select evtdate, evtlimitmem from event where evtid = {eventid}", "r")
            # print(datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S"))
            print(f'database: {timecheck[1]}')
            print(f'database: {timecheck[1][0][0]}, type: {type(timecheck[1][0][0])}')
            count = connectDB(f'SELECT COUNT ( DISTINCT POLLDCUsername ) AS "Number of pollers" FROM polling where evtid = {eventid}', "r")
            print(count[1][0][0])
            if(update_checking):
                if checking[1][0][0] == False and timecheck[1][0][0] > datetime.now(timecheck[1][0][0].tzinfo) and count[1][0][0] <= timecheck[1][0][1] and timecheck[1][0][1] != 0:
                    current_time = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
                    connectDB(f"INSERT INTO polling VALUES (DEFAULT, {eventid}, '{interaction.user.id}', '{interaction.user}','{current_time}' )", "i") 
                    await interaction.response.send_message(f'{interaction.user}, you have successfully joined the event')
                elif checking[1][0][0] == True:
                    await interaction.response.send_message(f'{interaction.user}, you are not allowed to join the same event more than twice')
                elif count[1][0][0] >= timecheck[1][0][1]:
                    await interaction.response.send_message(f'{interaction.user}, member is full')
                else:
                    await interaction.response.send_message(f'{interaction.user}, the event is overdue')    
            else:
                await interaction.response.send_message(f'{interaction.user}, this is not the latest event')    

            
#run bot by token
bot.run("OTk0ODk4OTcwMDg4MzA4NzQ2.GaEk2B.X7x5yEF1CZjHqtRM0YsMsCcSY6Qcn892V_z5Kk")