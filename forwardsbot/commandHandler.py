"""
HideForwardsBot - Telegram bot for hiding forward tag of original source
Copyright (©) 2020-2022 रोहित यादव <Itsydv@outlook.com>
Github: github.com/Itsydv

HideForwardsBot is free software: you can redistribute it and/or modify it under the terms of the
Apache License (Version 2.0) as published by the Apache Software Foundation.
"""

import datetime
import logging

import telebot
from telebot.apihelper import ApiTelegramException
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.util import content_type_media, extract_arguments

import config.config as config
from forwardsbot import bot, constants, commands, cur, func, chat_features, conn


# handle callback query
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(query):
    try:
        bot.answer_callback_query(query.id)
        data = query.data
        if data.startswith('help'):
            help_command(query.message)
        elif data.startswith('policy'):
            privacy_policy(query.message)
        elif data.startswith('report-bug'):
            chat_features.report_bug(query.message)
    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            pass
        else:
            logging.error(e)
    except Exception as e:
        logging.error(e)


@bot.message_handler(chat_types=['private'], commands=['start'])
def start_command(message):
    user_id = extract_arguments(message.text)
    if user_id and user_id in config.ADMINS_LIST_DICT.keys():
        chat_features.reply_to_user(message.chat.id, user_id)
    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.row(
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Source Code', url=constants.github_repo))
        keyboard.row(InlineKeyboardButton('Bot Related Updates', url=f't.me/{constants.bot_owner}'))
        try:
            bot.send_message(
                message.chat.id,
                f"Hi <b>{message.chat.first_name}!</b> Welcome to @{constants.username} developed by "
                f"@{constants.bot_owner}\n\n{commands.HELP_TEXT}\n\n<b>Join our "
                "Channel</b> It will be easier for you to find me in future if I gets down or blocked by telegram.",
                reply_markup=keyboard)
            result = cur.execute(f"select * from users where id = {message.chat.id}").fetchone()
            # if user not registered
            if not result:
                username = '@' + str(
                    message.chat.username) if message.chat.username else \
                    message.chat.first_name if message.chat.first_name else message.chat.id
                cur.execute(
                    "Insert into users (id, username, date) values (?, ?, ?)",
                    (message.chat.id, username, str(datetime.date.today())))
                conn.commit()
        except ApiTelegramException as e:
            if "blocked" in e.result_json['description']:
                pass
            else:
                logging.error(e)
        except Exception as e:
            logging.error(e)


@bot.message_handler(chat_types=['private'], commands=['help'])
def help_command(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton('Report Bugs/Issues', callback_data='report-bug'),
        InlineKeyboardButton('Data & Policy', callback_data='policy')
    )
    keyboard.row(InlineKeyboardButton('Bot Related Updates', url=f't.me/{constants.bot_owner}'))
    try:
        bot.send_message(
            message.chat.id,
            '<b>Help</b> \n\n' +
            commands.HELP_TEXT + commands.AVAILABLE_COMMANDS + '\n\n'
                                                               f'Made with ❤️ by @{constants.bot_owner}',
            reply_markup=keyboard)
    except:
        pass


@bot.message_handler(chat_types=['private'], commands=['policy'])
def privacy_policy(message):
    try:
        keyboard = InlineKeyboardMarkup()
        keyboard.row(InlineKeyboardButton('Report Bugs/Issues', callback_data='report-bug'))
        keyboard.row(InlineKeyboardButton('Join Backup channel', url=f't.me/{constants.bot_owner}'))
        keyboard.row(InlineKeyboardButton('Source Code', url=constants.github_repo))
        bot.send_message(
            message.chat.id,
            '<b>Terms of Service, Data & Privacy</b> \n\n' +
            "We don't collect any <b>personal data</b> from you, we just use information which is necessary. This "
            "includes: \n" +
            f'• Error logs to provide you a better experience and to improve performance \n' +
            f'• Telegram account user id ({message.chat.id}) (for notifications) \n\n' +
            "We don't collect your <b>phone number, emails or any other privacy related credentials</b>\n" +
            "Feel free to contact us using /reportissue command if you have any questions or feedback.",
            reply_markup=keyboard)
    except:
        pass


@bot.message_handler(commands=['id'])
def get_id(message):
    try:
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass
        bot.send_message(message.chat.id, message.chat.id)
    except:
        pass


@bot.message_handler(chat_types=['private'], is_command=False, is_album=False, content_types=content_type_media)
def echo_message(message):
    """
    Echo the message to the chat
    Removes the forward tag of source message if it is a forwarded message
    """
    if func.buttons_configuration.get(message.chat.id) == 'off' or func.captions_configuration.get(
            message.chat.id) == 'off':
        if func.joined_channel(message.chat.id):
            keyboard = func.get_config(message, 'buttons')
            caption = func.get_config(message, 'caption')
        else:
            return
    else:
        keyboard = message.reply_markup
        caption = message.html_caption
    try:
        bot.copy_message(message.chat.id, message.chat.id, message.message_id,
                         reply_markup=keyboard, caption=caption, parse_mode='HTML')
    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            pass
        else:
            logging.error(e)
    except Exception as e:
        logging.error(e)


def handle_cmd(message):
    try:
        if message.text.strip() == '/start':
            start_command(message)
        elif message.text.strip() == '/help':
            help_command(message)
        elif message.text.strip() == '/policy':
            privacy_policy(message)
        else:
            bot.send_message(message.chat.id, 'Previous Operation Cancelled !! Execute Again')
    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            pass
        else:
            logging.error(e)
    except Exception as e:
        logging.error(e)


# Adding Custom Filters
class NotFromBot(telebot.custom_filters.SimpleCustomFilter):
    key = 'not_from_bot'

    @staticmethod
    def check(message: telebot.types.Message, **kwargs):
        return not message.reply_to_message.from_user.is_bot


class IsCommand(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_command'

    @staticmethod
    def check(message: telebot.types.Message, **kwargs):
        text = message.text
        if text is None:
            return False
        return text.startswith('/')


class IsAuthorized(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_authorized'

    @staticmethod
    def check(message: telebot.types.Message, **kwargs):
        return str(message.chat.id) in constants.admins_dict.keys()


bot.add_custom_filter(NotFromBot())
bot.add_custom_filter(IsCommand())
bot.add_custom_filter(IsAuthorized())
bot.add_custom_filter(telebot.custom_filters.IsReplyFilter())
