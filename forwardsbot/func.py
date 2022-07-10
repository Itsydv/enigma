"""
HideForwardsBot - Telegram bot for hiding forward tag of original source
Copyright (©) 2020-2022 रोहित यादव <Itsydv@outlook.com>
Github: github.com/Itsydv

HideForwardsBot is free software: you can redistribute it and/or modify it under the terms of the
Apache License (Version 2.0) as published by the Apache Software Foundation.
"""

import logging

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from forwardsbot import constants, bot

# Dictionary to store configuration
buttons_configuration = {}
captions_configuration = {}


def get_config(message, config_type):
    """
    :param message: Message object
    :param config_type: 'buttons' or 'caption'
    :return: True if configuration is enabled, False otherwise
    """

    try:
        if config_type == 'enable_buttons':
            result = buttons_configuration.get(message.chat.id)
            if result == 'off':
                return None
            return message.reply_markup.keyboard
        else:
            result = captions_configuration.get(message.chat.id)
            if result == 'off':
                return None
            return message.html_caption
    except Exception as e:
        logging.error(e)


def load_configuration(cursor):
    """
    :param cursor: cursor object
    Just load configuration from database
    :return: None
    """
    result = cursor.execute("Select id, enable_buttons, enable_caption from users").fetchall()
    for user in result:
        chat_id = user[0]
        button = user[1]
        caption = user[2]
        buttons_configuration[chat_id] = button
        captions_configuration[chat_id] = caption


def joined_channel(member_id):
    """
    :param member_id: user id
    :return: True if user is a member of the channel, False otherwise
    and if user hasn't joined the channel prompt him to join
    """
    try:
        if check_user("@" + constants.bot_owner, member_id):
            return True
        else:
            keyboard = InlineKeyboardMarkup()
            keyboard.add(InlineKeyboardButton('Join', url=f"t.me/{constants.bot_owner}"))
            bot.send_message(member_id, f"To use this special feature of bot you have to join @{constants.bot_owner}\n"
                                        "It will be easier for you to find me in future if I got blocked by telegram.",
                             reply_markup=keyboard)
            return False
    except:
        return True


def check_user(chat_id, member_id):
    """
    :param chat_id: chat id
    :param member_id: user id
    :return: True if user is a member of the chat, False otherwise
    """
    try:
        response = bot.get_chat_member(chat_id, member_id)
        return not (response.status == 'kicked' or response.status == 'left')
    except:
        return False


def edit_report(message, msg_txt):
    """
    :param message: Message object
    :param msg_txt: text of message
    Modify message text in report format
    """
    if msg_txt:
        return f'<b>{forwarder_name(message)} :- </b>' + msg_txt
    return ''


def forwarder_name(message):
    """
    :param message: Message object
    :return: name of forwarder
    """
    username = '@' + str(message.chat.username) if message.chat.username else message.chat.first_name
    sender = f'{username} ' if username else 'User '
    return f'{sender} ({message.chat.id}) '
