"""
HideForwardsBot - Telegram bot for hiding forward tag of original source
Copyright (©) 2020-2022 रोहित यादव <Itsydv@outlook.com>
Github: github.com/Itsydv

HideForwardsBot is free software: you can redistribute it and/or modify it under the terms of the
Apache License (Version 2.0) as published by the Apache Software Foundation.
"""

import logging
import os

from telebot.apihelper import ApiTelegramException
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.util import extract_arguments

from forwardsbot import bot, cur, conn, func, keyboards, constants, commandHandler


@bot.message_handler(chat_types=['private'], is_reply=True, commands=['removewebpagepreview'])
def disable_webpage_preview(message):
    try:
        if func.joined_channel(message.chat.id):
            replied_msg = message.reply_to_message
            keyboard = InlineKeyboardMarkup(
                keyboard=message.reply_markup.keyboard if message.reply_markup else None)
            if replied_msg.content_type == 'text':
                bot.send_message(message.chat.id, replied_msg.html_text, reply_markup=keyboard,
                                 disable_web_page_preview=True)
            else:
                bot.send_message(message.chat.id, "No webpage preview to remove.")
    except:
        pass


@bot.message_handler(chat_types=['private'], is_reply=False, commands=['removewebpagepreview'])
def disable_webpage_preview_info(message):
    try:
        bot.send_message(message.chat.id,
                         'This command is used to remove webpage preview from an message.\n\n' +
                         ' Reply with this command to the message where you want to disable webpage preview.' +
                         ' Be sure to reply to the message the bot already echoed.')
    except:
        pass


@bot.message_handler(chat_types=['private'], is_reply=True, commands=['addcaption'])
def add_caption(message):
    try:
        if func.joined_channel(message.chat.id):
            replied_msg = message.reply_to_message
            if replied_msg.content_type == 'text':
                bot.send_message(replied_msg.chat.id, "Text messages don't have Captions 😏")
            elif len(message.text.split()) < 2:
                bot.send_message(message.chat.id,
                                 "Please provide caption to add\n\n" +
                                 "<b>e.g., </b><code>/addcaption [caption Here]</code> (brackets not included)"
                                 )
            else:
                new_caption = extract_arguments(message.html_text)
                bot.copy_message(replied_msg.chat.id, replied_msg.chat.id, replied_msg.message_id, caption=new_caption,
                                 parse_mode='HTML')

    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            pass
        else:
            logging.error(e)
    except Exception as e:
        logging.error(e)


@bot.message_handler(chat_types=['private'], is_reply=False, commands=['addcaption'])
def add_caption_info(message):
    try:
        if len(message.text.split()) > 1:
            bot.reply_to(message,
                         'Reply with this command and the caption after it to the message where you want to add the '
                         'caption.')
        else:
            bot.send_message(message.chat.id,
                             "<b>This command allow you to add a caption to a message." +
                             "Reply with this command and the caption after it to the message where you want to add "
                             "the caption.</b>\n\n" +
                             "<b>e.g., </b><code>/addcaption [caption Here]</code>\n\n" +
                             "<i>If the message already has a caption this command will overwrite the current caption "
                             "with the new one." +
                             " If the message doesn't support a caption, it simply won't add it.</i>\n\n" +
                             "<code>Note: If the message is sent by you, you can just edit it to add the caption." +
                             "This command is intended in case for example you are forwarding from a channel a big "
                             "file you don't want to download and upload again.</code>")
    except:
        pass


@bot.message_handler(chat_types=['private'], is_reply=True, commands=['removecaption'])
def remove_caption(message):
    try:
        if func.joined_channel(message.chat.id):
            replied_msg = message.reply_to_message
            if replied_msg.content_type == 'text':
                bot.send_message(replied_msg.chat.id, "Text messages don't have Captions 😏")
                return
            bot.copy_message(replied_msg.chat.id, message.chat.id, replied_msg.message_id, caption="",
                             parse_mode='HTML')
    except:
        return


@bot.message_handler(chat_types=['private'], is_reply=False, commands=['removecaption'])
def remove_caption_info(message):
    try:
        bot.send_message(message.chat.id,
                         'This command is used to remove caption from an media.' +
                         ' Reply with this command to the message where you want to remove the caption.' +
                         ' Be sure the message has a caption.'
                         )
    except:
        pass


@bot.message_handler(chat_types=['private'], is_reply=True, commands=['removebuttons'])
def remove_buttons(message):
    try:
        if func.joined_channel(message.chat.id):
            replied_msg = message.reply_to_message
            if replied_msg.reply_markup.keyboard is None:
                bot.send_message(message.chat.id, "Message doesn't have buttons")
                return
            bot.copy_message(replied_msg.chat.id, replied_msg.chat.id, replied_msg.message_id, reply_markup=None,
                             parse_mode='HTML')

    except:
        return


@bot.message_handler(chat_types=['private'], is_reply=False, commands=['removebuttons'])
def remove_buttons_info(message):
    try:
        bot.send_message(message.chat.id,
                         'This command is used to remove buttons from a message.' +
                         ' Reply with this command to the message where you want to remove the buttons.' +
                         ' Be sure the message has buttons.'
                         )
    except:
        pass


@bot.message_handler(chat_types=['private'], is_reply=True, commands=['removelinks'])
def remove_link(message):
    try:
        if func.joined_channel(message.chat.id):
            replied_msg = message.reply_to_message
            if replied_msg.content_type == 'text':
                bot.send_message(replied_msg.chat.id, replied_msg.text)
                return
            bot.copy_message(replied_msg.chat.id, replied_msg.chat.id, replied_msg.message_id,
                             caption=replied_msg.caption, parse_mode='HTML')

    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            pass
        else:
            logging.error(e)
    except:
        bot.reply_to(message, "Make sure the message has a hyperlink !!")


@bot.message_handler(chat_types=['private'], is_reply=False, commands=['removelinks'])
def remove_link_info(message):
    try:
        bot.send_message(message.chat.id,
                         'This command is used to remove <b>hyperlinks</b> only from message.' +
                         ' Reply with this command to the message where you want to remove the hyperlink(s).' +
                         ' Be sure the message has a hyperlink.'
                         )
    except:
        pass


@bot.message_handler(chat_types=['private'], commands=['caption', 'buttons'])
def disable_config(message):
    try:
        if func.joined_channel(message.chat.id):
            config_type = message.text.split()[0][1:].split('@')[0]
            operation = f"enable_{config_type}"
            result = cur.execute(f"select {operation} from users where id = {message.chat.id}").fetchone()
            keyboard = keyboards.update_config(message.text.split()[0][1:].split('@')[0], result[0])
            if config_type == 'caption':
                bot.send_message(message.chat.id, 'This option is used to Enable/disable the Captions for '
                                                  'Media File(s).',
                                 reply_markup=keyboard)
            elif config_type == 'buttons':
                bot.send_message(message.chat.id, f'This option is used to Enable/disable the Buttons for all messages',
                                 reply_markup=keyboard)
    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            pass
        else:
            logging.error(e)
    except Exception as e:
        logging.error(e)


@bot.callback_query_handler(func=lambda call: ('caption' in call.data or 'buttons' in call.data))
def process_config(call):
    message = call.message
    if func.joined_channel(message.chat.id):
        config_type, value = call.data.split('-')
        try:
            operation = f"enable_{config_type}"
            cur.execute(f"update users set {operation} = '{value}' where id = {message.chat.id}")
            conn.commit()
            if config_type == 'caption':
                func.captions_configuration[message.chat.id] = value
            elif config_type == 'buttons':
                func.buttons_configuration[message.chat.id] = value
            bot.answer_callback_query(call.id,
                                      text=f'Done !! {config_type.capitalize()} is now turned {value.upper()}')
            keyboard = keyboards.update_config(config_type, value)
            bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=keyboard)
        except ApiTelegramException as e:
            if "blocked" in e.result_json['description']:
                pass
            elif "not modified" in e.result_json['description']:
                pass
            else:
                logging.error(e)
        except Exception as e:
            logging.error(e)


@bot.message_handler(chat_types=['private'], is_reply=True, commands=['isolate_sticker'])
def isolate_sticker(message):
    try:
        replied_msg = message.reply_to_message
        if func.joined_channel(message.chat.id) and replied_msg.content_type == 'sticker':
            bot.delete_message(message.chat.id, message.message_id)
            msg = bot.send_message(message.chat.id, 'Please wait..')
            sticker = bot.get_file(replied_msg.sticker.file_id)
            msg = bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                        text='Downloading Sticker..')
            downloaded_file = bot.download_file(sticker.file_path)
            msg = bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                        text='Isolating Sticker..')
            with open(f'{replied_msg.sticker.file_unique_id}.tgs', 'wb') as new_file:
                new_file.write(downloaded_file)
            with open(f'{replied_msg.sticker.file_unique_id}.tgs', 'rb') as new_file:
                bot.send_sticker(message.chat.id, new_file)
                bot.delete_message(message.chat.id, msg.message_id)
            os.remove(f'{replied_msg.sticker.file_unique_id}.tgs')
        elif replied_msg.content_type != 'sticker':
            bot.send_message(message.chat.id, 'Please reply to a sticker to isolate it.')
    except ApiTelegramException as e:
        if "blocked" in e.result_json['description']:
            pass
        else:
            logging.error(e)
    except Exception as e:
        logging.error(e)


@bot.message_handler(chat_types=['private'], is_reply=False, commands=['isolate_sticker'])
def isolate_sticker_info(message):
    try:
        bot.send_message(message.chat.id,
                         'This command is used to isolate any sticker from its sticker pack.' +
                         ' Reply with this command to the sticker which you want to isolate from sticker pack.'
                         )
    except:
        pass


@bot.message_handler(chat_types=['private'], commands=['reportissue', 'reportbug'])
def report_bug(message):
    try:
        msg = bot.send_message(message.chat.id,
                               'Now write a message to send to the bot admin.\n\nYou can also attach screenshots or '
                               'log file but all in single message or type /cancel to cancel the operation')
        bot.register_next_step_handler(msg, process_report)
    except:
        pass


def process_report(message):
    try:
        if message.text:
            if message.text == '/cancel':
                bot.send_message(message.chat.id, 'Operation Cancelled')
                return
            elif message.text[0] == '/':
                commandHandler.handle_cmd(message)
                return
        send_to = constants.log_grp
        keyboard = InlineKeyboardMarkup()
        keyboard.add(
            InlineKeyboardButton('Reply', url='https://t.me/'
                                              f'{constants.username}?start={message.from_user.id}'))
        if message.content_type == 'text':
            text = func.edit_report(message, message.html_text)
            bot.send_message(send_to, text, reply_markup=keyboard)
        else:
            caption = func.edit_report(message, message.html_caption)
            bot.copy_message(send_to, message.chat.id, message.message_id, caption=caption, reply_markup=keyboard,
                             parse_mode='HTML')
        bot.reply_to(message, 'Your Message is Sent to Admin 👍')
    except Exception as e:
        logging.error(e)


@bot.message_handler(chat_types=['private'], is_authorized=True, commands=['message_to'])
def admins_message(message):
    """
    Admin Command
    Sending message to specific user
    """
    try:
        if len(message.text.split()) > 1:
            send_to = message.text.split()[1].strip()
            reply_to_user(message.chat.id, send_to)
    except Exception as e:
        bot.send_message(constants.log_grp, f'Exception in admins_message Function :- {e}')


def reply_to_user(chat_id, send_to):
    msg = bot.send_message(chat_id, '<b>Ok now send ur message !!</b>')
    bot.register_next_step_handler(msg, process_admin_message, send_to)


def process_admin_message(message, send_to):
    try:
        if message.content_type == 'text':
            text = f'<b>Message from Admin :-</b> {message.html_text}' if message.html_text else message.text
            bot.send_message(send_to, text, reply_markup=message.reply_markup)
        else:
            caption = f'<b>Message from Admin :-</b> ' \
                      f'{message.html_caption}' if message.html_caption else message.caption
            bot.copy_message(send_to, message.chat.id, message.message_id, caption=caption, parse_mode='HTML')
        bot.send_message(message.chat.id, 'Message Sent 👍')
    except ApiTelegramException as e:
        error = str(e.result_json['description'])
        bot.send_message(message.chat.id, error)


@bot.message_handler(chat_types=['private'], commands=['cancel'])
def delete_operation(message):
    try:
        bot.clear_step_handler(message)
        bot.reply_to(message, "<b>No operation to cancel</b>")
    except:
        pass
