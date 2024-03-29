# Youth Discord NLP AI Chatbot 🤖
#### Designed for the St. James Settlement(SJS) Cyber Youth Support Team entitled "6PM"
#### © 2023 Eric Chan, Andy Chan, Jayden Chan, Ken Yeung

## Description:
#### We have collaborated with 6PM, an online support team from a charitable organization, St. James' Settlement. They aim to help hidden youths, who are socially withdrawn from social life, by using available online resources such as online counseling to provide support. Through a meeting with the social workers from 6PM, they have proposed their current situation and problems, which includes the unavailability of online counseling at different times and the inconvenient management of their activities. To tackle the problems that social workers face, we have decided to create a Discord chatbot and a web application. In this paper, a literature review of research on the hidden youths, related technologies required to build the chatbot and an analysis of existing solutions is described first to assist in the brainstorming design of the functions for the chatbot and the web application. Then a system and functional design of the Discord chatbot and the web application will be presented.

## Project Objectives:
#### 1. Bringing informative news 
#### 2. Chatting with hidden youth 
#### 3. Reduce social workers workload 
#### 4. Promoting 6PM 
#### 5.	Evaluation of the system 

## Functions:
#### Discord: 
* Chatting: users can make simple conversations with the chatbot.
* Emotion Detection: analyze the emotion of each message sent by a Discord user.
* FAQ: Users can type text such as ‘contact’, and the Discord bot will return the contact information. If ‘activity’ is entered, the chatbot will return a redirect link to their activities information
* Informative News: Discord bot able to re-post the latest post from Facebook. 
* Apply/Confirm event(s): Allows users to apply/confirm event(s). 

#### Web Application:
* Login: For SJS Internal admins.
* Event Organizing: creat a event will save it into the PostgreSQL database, and send a request to API flask application for posting event, accept or reject the application and send a request to API flask application for sending direct message to user.
* Search Event: Allows the social worker to search the event by event name.
* Create Activity: Allows the social worker to create an activity used on creating event.
* Change Password: Allow the social worker to modify their password
* Logging and Username Filtering: Allow the social worker to view the log and filter the log record with discord username
* Calendar: Shows all event in the calendar
  
#### API:
* Posting event: Able to post events to Discord channel by receiving the event ID from the web application request.
* Event confirmation: Send direct messages to notify users whether their event applications are successful or not.

## Supporting Technologies:
#### Discord Chatbot: pycord, numpy, nltk, torch, transformers, flask, flask_discord_interaction
#### Web Application: PHP, pgsql, Bootstrap, jQuery
#### Database: PostgreSQL
#### Hosting: Docker/Amazone EC2

## Preparation:
* Prepare Discord bot token generate in Discord developer portal https://discord.com/developers/applications
* Prepare FB_ACCESS_TOKEN which is facebook page token generate in Graph API on Meta for Developers https://developers.facebook.com/tools/explorer
* Prepare SJS admin user Id
* Prepare Channel Id

## Installation Steps:
1. Download Docker on offical website - https://docs.docker.com/compose/install/
2. Open the execuation file
3. If you are using Windows OS, please make sure selected "install required Windows components for WSL 2"
4. If you are using Windows OS, please install Linux on Windows with WSL by open a PowerShell and input "wsl --install" after installed.
5. Reboot your PC if required
6. Open a termial or PowerShell and change directory to project folder which contains docker-compose.yaml. "cd /path"
7. Run the command "docker-compose -d", and wait for it
8. All the container will shown as started
9. Open Docker Dashboard, and select "python_app" container.
10. The chatbot will able to use after you can see a log message show "Chatbot is start to run"
