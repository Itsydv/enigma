"""
HideForwardsBot - Telegram bot for hiding forward tag of original source
Copyright (©) 2020-2022 रोहित यादव <Itsydv@outlook.com>
Github: github.com/Itsydv

HideForwardsBot is free software: you can redistribute it and/or modify it under the terms of the
Apache License (Version 2.0) as published by the Apache Software Foundation.
"""


class Constants:
    """
    Constants class for hideforwardsbot.
    """

    def __init__(self, token, host_name):
        self._name = None
        self._username = None
        self._admins_dict: dict = {}
        self.__version = "0.4.1"
        self.__author = "Itsydv"  # GitHub Username
        self.__email = "itsydv@outlook.com"
        self.__github_repo = "Enigma"
        self.bot_owner = 'CharlieBots'
        self.token: str = token
        self.host_name = host_name
        self.db_file = 'data/database.db'
        self.log_grp = '-1001389138549'
        self.log_file = 'data/botlogs.log'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def admins_dict(self):
        return self._admins_dict

    @admins_dict.setter
    def admins_dict(self, admins_dict):
        self._admins_dict = admins_dict

    @property
    def webhook_url(self):
        return f'https://{self.host_name}.pythonanywhere.com/{self.token}'

    @property
    def github_repo(self):
        return rf'https://github.com/{self.__author}/{self.__github_repo}'


class Commands:
    """
    Commands class for hideforwardsbot.
    """

    HELP_TEXT = "Just send me File(s), Post(s) or Message(s) which you want to send to someone anonymously without " \
                "leaking actual source, I'll Hide actual Source (Forward Tag of real owner of that content from " \
                "Post's header)."

    AVAILABLE_COMMANDS = """<b>Available commands :</b>

<b>[ Private Commands ]</b>
/start - Initialize the bot
/help - Bots commands and How It works
/policy - Bots data usage and Privacy Policy
/id - Get Your telegram ID
/isolate_sticker - Isolate any sticker from its original pack
/removewebpagepreview - Use this command to remove webpage preview for an message
/removelinks - This command is used to remove <b>hyperlinks</b> from message.
/removecaption - Use this command to remove caption from an media message
/addcaption - Use this command to add caption to an media message
/removebuttons - Use this command to remove buttons from an message
/caption - Use this message to enable/disable caption for all media messages that will be sent from now onwards
/buttons - Use this message to enable/disable buttons for all messages that will be sent from now onwards
/reportbug - Send a message to the bot Admin

<b>[ Group Commands ]</b>
/id - Get the telegram ID of the group
/copy - Copy a message from chat to your Inbox
/duplicate - Duplicate a message and removes original one

Note: You can also copy non-forwarded/protective content messages from group to your Inbox if Bot is added in the 
group and that message isn't send by any other bot. """
