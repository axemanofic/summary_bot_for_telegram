#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import config
import telebot
from telebot import types

bot = telebot.TeleBot(token=config.TOKEN)


def getReplyKeyboard(text):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text))
    return keyboard


def getInlineKeyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('О себе', callback_data='self')
    button2 = types.InlineKeyboardButton('Скиллы', callback_data='skills')
    button3 = types.InlineKeyboardButton('Образование',
                                         callback_data='certificates')
    keyboard.row(button1, button2)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'self':
        bot.edit_message_text('о себе', chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=getInlineKeyboard())
    elif call.data == 'skills':
        bot.edit_message_text('скиллы', chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=getInlineKeyboard())
    elif call.data == 'certificates':
        bot.edit_message_text('сертификаты', chat_id=call.message.chat.id,
                              message_id=call.message.id, reply_markup=getInlineKeyboard())


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет 😊',
                     reply_markup=getReplyKeyboard('Просмотреть резюме 📚'))


@bot.message_handler(content_types=['text'])
def text_handler(message):
    print(message.text, message.from_user.id)

    if message.text == 'Просмотреть резюме 📚':
        bot.send_message(message.chat.id, 'Выбирай',
                         reply_markup=getInlineKeyboard())
    elif (message.text == 'admin') and (message.chat.id == config.MY_ID):
        bot.send_message(message.chat.id,
                         'Добро пожаловать {}'.format(message.chat.username))


def main_loop():
    bot.polling(none_stop=True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        sys.exit(0)
