"""
HideForwardsBot - Telegram bot for hiding forward tag of original source
Copyright (©) 2020-2022 रोहित यादव <Itsydv@outlook.com>
Github: github.com/Itsydv

HideForwardsBot is free software: you can redistribute it and/or modify it under the terms of the
Apache License (Version 2.0) as published by the Apache Software Foundation.
"""

# built-in modules
import sqlite3
import logging

# need to install these modules
from telebot import TeleBot
from telebot.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats, Update
from flask import Flask, request

# files
from forwardsbot.util import Constants, Commands
from config import config


def initialize_bot(webhook=False):
    """
    Initialize bot instance and set webhook
    :return: TeleBot instance
    """
    bot_instance: TeleBot = TeleBot(constants.token, threaded=False, parse_mode='HTML', skip_pending=True)
    if webhook:
        bot_instance.remove_webhook()
        bot_instance.set_webhook(url=constants.webhook_url, drop_pending_updates=True)
    return bot_instance


def set_bot_credentials(bot_instance: TeleBot):
    """
    :param bot_instance: TeleBot instance
    setting bot credentials like username, first name, last name, commands, etc.
    """
    bot_info = bot_instance.get_me()
    constants.name = bot_info.first_name
    constants.username = bot_info.username
    constants.admins_dict = config.ADMINS_LIST_DICT

    # deleting all previous commands
    bot_instance.delete_my_commands()

    # set bot commands for all private chats
    bot_instance.set_my_commands(
        commands=[
            BotCommand("start", "Initialize Bot"),
            BotCommand("help", "Ask for Help"),
            BotCommand("policy", "Bots data usage and Privacy Policy "),
            BotCommand("id", "Get Your telegram ID"),
            BotCommand("isolate_sticker", "Isolate any sticker from its original pack"),
            BotCommand("removewebpagepreview", "Remove webpage preview for an message"),
            BotCommand("removelinks", "Remove hyperlinks from message"),
            BotCommand("addcaption", "Add caption to an media message"),
            BotCommand("removecaption", "Remove caption from an media message"),
            BotCommand("removebuttons", "Remove buttons from an message "),
            BotCommand("caption", "Enable/disable caption for all media messages"),
            BotCommand("buttons", "Enable/disable buttons for all messages"),
            BotCommand("reportbug", "Report an Issue or send message to Admin"),
            BotCommand("cancel", "Cancel the current Operation")
        ],
        scope=BotCommandScopeAllPrivateChats()
    )

    # add commands for all group chats
    bot_instance.set_my_commands(
        commands=[
            BotCommand("id", "Get the telegram ID of the group"),
            BotCommand("copy", "Copy a message from chat to your Inbox."),
            BotCommand("duplicate", "Duplicate a message and removes original one.")
        ],
        scope=BotCommandScopeAllGroupChats()
    )


constants = Constants(config.BOT_TOKEN, config.HOST_NAME)  # get token from @BotFather
commands = Commands()
bot = initialize_bot(webhook=False)
set_bot_credentials(bot)
conn = sqlite3.connect(constants.db_file, check_same_thread=False)
cur = conn.cursor()

# setup logging
logging.basicConfig(level=logging.ERROR, filename=constants.log_file, filemode='a',
                    format='%(asctime)s : %(levelname)s - '
                           '%(funcName)s (%(filename)s) Function - %(message)s')

# require to connect files with each other
from forwardsbot import func, chat_features, group_features, commandHandler
func.load_configuration(cur)

# For running without polling method
app = Flask(__name__)


@app.route('/' + config.BOT_TOKEN, methods=['POST'])
def set_webhook():
    """
    Setting webhook for bot
    """
    update = Update.de_json(
        request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


@app.route('/')
def home():
    """
    Home page of the web server
    """
    return '<h1>Bot is running...</h1>'
