import os
from telebot import types

def getReplyKeyboard(text, resize_keyboard=False, one_time_keyboard=False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=resize_keyboard,
                                         one_time_keyboard=one_time_keyboard)
    if type(text) == tuple:
        for i in text:
            keyboard.add(types.KeyboardButton(i))
    else:
        keyboard.add(types.KeyboardButton(text))

    return keyboard


def getKeyboardSummary(text, callback_data=None, url=None):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text, callback_data=callback_data, url=url)
    keyboard.row(button)
    return keyboard