# -*- coding: utf-8 -*-
import time
import telebot
from telebot import types
import config
import os
import psycopg2

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
        markup = types.ReplyKeyboardMarkup()
        markup.row('Траты')
        markup.row('Курсы', 'Пифы')
        msg = bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
        bot.register_next_step_handler(msg, on_section_click)

def on_section_click(message):
        if message.text == 'Курсы':
                markup = types.ReplyKeyboardMarkup()
                markup.row('Назад')
                markup.row('USD/RUB', 'EUR/RUB')
                msg = bot.send_message(message.chat.id, "Выберите актив:", reply_markup=markup)
                bot.register_next_step_handler(msg, on_currency_click)

def on_currency_click(message):
        if message.text == 'Назад':
                handle_start(message)


if __name__ == '__main__':
        os.environ['http_proxy'] = 'http://datahub-20:8888'
        os.environ['https_proxy'] = 'http://datahub-20:8888'
        bot.polling(none_stop=True)
        os.environ['http_proxy'] = 'http://localhost:3128/'
        os.environ['https_proxy'] = 'http://localhost:3128/'

