# HideForwardsBot 🔎

[![version-0.4](https://img.shields.io/badge/version-0.4-green)](https://github.com/Itsydv/Enigma)
[![Python3](https://img.shields.io/badge/language-Python3-red)](https://www.python.org/downloads/)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-blue.svg)](https://t.me/CharlieBots)
[![GitHub](https://img.shields.io/badge/GitHub-orange.svg)](https://github.com/Itsydv)

[![Hire me on Fiverr](https://img.shields.io/badge/Hire%20me-Fiverr-green?style=for-the-badge&logo=appveyor)](https://www.fiverr.com/share/GXpGAd)
[![Checkout Bot on Telegram](https://img.shields.io/badge/Telegram-@HIdeForwardsBot-blue?style=for-the-badge&logo=appveyor)](https://www.t.me/HideForwardsBot)

If you don't like telegram forwards, before sending a message, send the message to the bot, then forward the message that the bot returns to the user you were chatting with. Just send him File(s), Post(s) or Message(s) which you want to send to someone anonymously without leaking actual source, He will Hide actual Source (Forward Tag of real owner of that content from Post's header).

### How to use it:

- Send any type of messages to the bot be a game, invoice, poll, etc. to get echoed message.

### Available Commands:

<b>[ Private Commands ]</b><br>
- `/start` - Initialize the bot<br>
- `/help` - Bots commands and How It works<br>
- `/policy` - Bots data usage and Privacy Policy<br>
- `/id` - Get Your telegram ID<br>
- `/isolate_sticker` - Isolate any sticker from its original pack<br>
- `/removewebpagepreview` - Use this command to remove webpage preview for a message<br>
- `/removelinks` - This command is used to remove <b>hyperlinks</b> from message.<br>
- `/removecaption` - Use this command to remove caption from a media message<br>
- `/addcaption` - Use this command to add caption to a media message<br>
- `/removebuttons` - Use this command to remove buttons from a message<br>
- `/caption` - Use this message to enable/disable caption for all media messages that will be sent from now onwards<br>
- `/buttons` - Use this message to enable/disable buttons for all messages that will be sent from now onwards<br>
- `/reportbug` - Send a message to the bot Admin

<b>[ Group Commands ]</b><br>
- `/id` - Get the telegram ID of the group<br>
- `/copy` - Copy a message from chat to your Inbox<br>
- `/duplicate` - Duplicate a message and removes original one

### Library Used 🔗
Python wrapper used: [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

Official Documentation: [Telegram Bot API](https://core.telegram.org/bots/api)


### If you want to run and host this bot by yourself:

**Clone and install:** ⚙️

1. Fork/Clone/Download this repo

    `git clone https://github.com/Itsydv/Enigma.git`

2. Navigate to the directory

    `cd Enigma`

3. Create a virtual environment for this project

    `python3 -m venv venv`
   
   Alternatively, you can use pipenv to create a virtual environment for this project.

4. Load the virtual environment
   - On Windows Powershell: `.\venv\Scripts\activate.ps1`
   - On Linux and Git Bash: `source venv/bin/activate`
  
5. Run `pip install -r requirements.txt`

6. Open the `config\config.py` file and edit all the fields like token, host, etc.

7. Run the run.py script in the terminal/shell
    - On Windows Powershell: `python run.py`
    - On Linux and Git Bash: `python3 run.py`

### Special Thanks
Special thanks to community group of pytba on Telegram for helping me to understand how to use the API.

[Join the PyTelegramBotAPI Telegram Chat Group](https://telegram.me/joinchat/Bn4ixj84FIZVkwhk2jag6A)
