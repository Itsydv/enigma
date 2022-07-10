"""
HideForwardsBot - Telegram bot for hiding forward tag of original source
Copyright (©) 2020-2022 रोहित यादव <Itsydv@outlook.com>
Github: github.com/Itsydv

HideForwardsBot is free software: you can redistribute it and/or modify it under the terms of the
Apache License (Version 2.0) as published by the Apache Software Foundation.
"""

import logging

from telebot.apihelper import ApiTelegramException

from forwardsbot import bot


@bot.message_handler(chat_types=['group', 'supergroup'], is_reply=True, not_from_bot=True,
                     commands=['copy', 'duplicate'])
def copy_message(message):
    try:
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass
        replied_msg = message.reply_to_message
        if message.text.split()[0][1:].split('@')[0] == 'copy':
            send_to = message.from_user.id
        else:
            send_to = message.chat.id
        bot.copy_message(send_to, message.chat.id, replied_msg.message_id, parse_mode='HTML')
        if message.text.split()[0][1:].split('@')[0] == 'duplicate':
            try:
                bot.delete_message(message.chat.id, replied_msg.message_id)
            except:
                pass
    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            bot.send_message(message.chat.id, 'Please unblock me first or use /start to start me then try again.')
        else:
            logging.error(e)
    except Exception as e:
        logging.error(e)


@bot.message_handler(chat_types=['group', 'supergroup'], is_reply=True, not_from_bot=False,
                     commands=['copy', 'duplicate'])
def cant_copy_message(message):
    try:
        bot.send_message(message.chat.id, f"You can't {message.text.split()[0][1:].split('@')[0]} "
                                          "messages from other bots.")
    except:
        pass


@bot.message_handler(chat_types=['group', 'supergroup'], is_reply=False, commands=['copy', 'duplicate'])
def copy_message_info(message):
    try:
        if message.text.split()[0][1:].split('@')[0] == 'copy':
            text = "Use this command to copy a message from this chat to your Inbox."
        else:
            text = "Use this command to duplicate any message of this chat and illustrate that if it was sent by me."
        bot.send_message(message.chat.id, text)
    except:
        pass
