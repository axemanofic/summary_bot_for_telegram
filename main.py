#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import time
import config
import telebot
from telebot import types

bot = telebot.TeleBot(token=config.TOKEN)


def getReplyKeyboard(text):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=2)
    keyboard.add(types.KeyboardButton(text))
    types.KeyboardButton
    return keyboard


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет 😊",
        reply_markup=getReplyKeyboard("Просмотреть резюме 😉"))


@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, message.text)


def main_loop():
    bot.polling(none_stop=True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        sys.exit(0)
