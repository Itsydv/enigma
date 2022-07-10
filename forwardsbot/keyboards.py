"""
HideForwardsBot - Telegram bot for hiding forward tag of original source
Copyright (©) 2020-2022 रोहित यादव <Itsydv@outlook.com>
Github: github.com/Itsydv

HideForwardsBot is free software: you can redistribute it and/or modify it under the terms of the
Apache License (Version 2.0) as published by the Apache Software Foundation.
"""

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from forwardsbot import constants


def github_source_button():
    """
    Returns a InlineKeyboardButton for source code on github
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Source Code", url=constants.github_repo))
    return keyboard


def update_config(config_type, value):
    """
    Return the update configuration keyboard of captions/button
    """
    if config_type == 'button':
        msg_text = 'Buttons'
    else:
        msg_text = 'Captions'

    keyboard = InlineKeyboardMarkup()
    if value == 'off':
        keyboard.row(InlineKeyboardButton(f'Turn {msg_text} On', callback_data=f'{config_type}-on'))
    else:
        keyboard.row(InlineKeyboardButton(f'Turn {msg_text} Off', callback_data=f'{config_type}-off'))
    return keyboard
