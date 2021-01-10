#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import config
import manage_db
import telebot
from global_var import TEMPLATE_TEXT
from functions import getKeyboardSummary, getReplyKeyboard

bot = telebot.TeleBot(token=config.TOKEN)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'skills':
        bot.edit_message_text(TEMPLATE_TEXT['skills'], chat_id=call.message.chat.id, message_id=call.message.id,
                              reply_markup=getKeyboardSummary('Образование', callback_data='education'))
    elif call.data == 'education':
        bot.edit_message_text(TEMPLATE_TEXT['education'], chat_id=call.message.chat.id, message_id=call.message.id,
                              disable_web_page_preview=True, parse_mode='html', reply_markup=
                              getKeyboardSummary('Написать мне', url='https://t.me/axemanofic'))


@bot.message_handler(commands=['start'])
def welcome(message):
    manage_db.insert_data((message.chat.id, message.chat.first_name))
    bot.send_message(message.chat.id, TEMPLATE_TEXT['welcome'],
                     reply_markup=getReplyKeyboard(TEMPLATE_TEXT['user_button'],
                                                   resize_keyboard=True, one_time_keyboard=True), parse_mode='html')

@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.chat.id, TEMPLATE_TEXT['help'],
                     reply_markup=getReplyKeyboard(TEMPLATE_TEXT['user_button'],
                                                   resize_keyboard=True, one_time_keyboard=True))


@bot.message_handler(content_types=['text'])
def text_handler(message):
    print(message)
    if message.text == TEMPLATE_TEXT['user_button']:
        bot.send_message(message.chat.id, TEMPLATE_TEXT['about_myself'], disable_web_page_preview=True,
                         reply_markup=getKeyboardSummary('Навыки', callback_data='skills'))

    elif (message.text == 'admin') and (message.chat.id in config.MY_ID):
        bot.send_message(message.chat.id, 'Добро пожаловать, {}'.format(message.chat.first_name),
                         reply_markup=getReplyKeyboard(TEMPLATE_TEXT['admin_button'], resize_keyboard=True))

    elif (message.text == TEMPLATE_TEXT['admin_button']) and (message.chat.id in config.MY_ID):
        num_users = manage_db.count_data()


def main_loop():
    bot.polling(none_stop=True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        sys.exit(0)
