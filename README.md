# Preparation:
- Discord bot token generate in Discord developer portal https://discord.com/developers/applications
- FB_ACCESS_TOKEN which is facebook page token generate in Graph API on Meta for Developers https://developers.facebook.com/tools/explorer
- SJS admin user Id
- Channel Id

# Installation step
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
