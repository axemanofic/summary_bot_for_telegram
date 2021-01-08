#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import config
import telebot
from telebot import types

bot = telebot.TeleBot(token=config.TOKEN)


def getReplyKeyboard(text, resize_keyboard=False, one_time_keyboard=False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=resize_keyboard,
                                         one_time_keyboard=one_time_keyboard)
    if type(text) == tuple:
        for i in text:
            keyboard.add(types.KeyboardButton(i))

    else:
        keyboard.add(types.KeyboardButton(text))

    return keyboard


def getInlineKeyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('О себе', callback_data='self')
    button2 = types.InlineKeyboardButton('Скиллы', callback_data='skills')
    button3 = types.InlineKeyboardButton('Образование',
                                         callback_data='education')
    keyboard.row(button1, button2)
    keyboard.row(button3)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'self':
        bot.edit_message_text('о себе', chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=getInlineKeyboard())
    elif call.data == 'skills':
        bot.edit_message_text('скиллы', chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=getInlineKeyboard())
    elif call.data == 'education':
        bot.edit_message_text('сертификаты', chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=getInlineKeyboard())


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет 😊',
                     reply_markup=getReplyKeyboard(config.USER_BUTTON_TEXT,
                                                   resize_keyboard=True, one_time_keyboard=True))


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == config.USER_BUTTON_TEXT:
        bot.send_message(message.chat.id, 'Выбирай',
                         reply_markup=getInlineKeyboard())
    elif (message.text == 'admin') and (message.chat.id == config.MY_ID):
        bot.send_message(message.chat.id,
                         'Добро пожаловать {}'.format(message.chat.username),
                         reply_markup=getReplyKeyboard(config.ADMIN_BUTTON_TEXT, resize_keyboard=True))


def main_loop():
    bot.polling(none_stop=True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        sys.exit(0)
