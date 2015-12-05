# coding: utf-8
import time
import telebot
from telebot import types
import config
import os
import sys

path = os.getcwd() + "/rawdata"
sys.path.insert(0, path)

path = os.getcwd() + "/graphics"
sys.path.insert(0, path)

import asset
from datetime import datetime, date, timedelta
import currency

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['info', 'help'])
def command_help(message):
    bot.send_message(message.chat.id, "Для начала работы с ботом, введите /start")

@bot.message_handler(commands=['start'])
def handle_start(message):
        markup = types.ReplyKeyboardMarkup(selective=False)
        markup.row('Траты')
        markup.row('Курсы')
        msg = bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
        bot.register_next_step_handler(msg, on_section_click)

def on_section_click(message):
	asset_list = asset.get_assets_names()
	print asset_list

        if message.text == u'Курсы':
                markup = types.ReplyKeyboardMarkup(selective=False)
                markup.row('Назад')
                markup.row('USD/RUB за неделю', 'EUR/RUB за неделю')
                markup.row('USD/RUB за год', 'EUR/RUB за год')
                msg = bot.send_message(message.chat.id, "Выберите актив:", reply_markup=markup)
                bot.register_next_step_handler(msg, on_currency_click)
        elif message.text == u'Траты':
                msg = bot.send_photo(message.chat.id, open('temp.jpg', 'rb'))
                bot.register_next_step_handler(msg, on_section_click)

def on_currency_click(message):
        if message.text == u'Назад':
            handle_start(message)
        elif message.text == u'USD/RUB за неделю':
            createAndShowChart(message, 1, True, "USD/RUB")
        elif message.text == u'EUR/RUB за неделю':
            createAndShowChart(message, 2, True, "EUR/RUB")
        elif message.text == u'USD/RUB за год':
            createAndShowChart(message, 1, False, "USD/RUB")
        elif message.text == u'EUR/RUB за год':
            createAndShowChart(message, 2, False, "EUR/RUB")

def createAndShowChart(message, index, isWeek, title):
    res = asset.get_asset_quotes(index)
    days = sorted(res.keys())
    ticks = []
    for item in days:
        ticks.append(res.get(item).get('AdjClose'))

    if isWeek == True:
        currency.createChartWeek(title, days, ticks)
    elif index == 1:#HardCode
        currency.createChartWeek(title, days, ticks, TRUE)
    else:
        currency.createChart(title, days, ticks)

    msg = bot.send_photo(message.chat.id, open('filename.png', 'rb'))
    bot.register_next_step_handler(msg, on_currency_click)


@bot.message_handler(func=lambda message: True, content_types=['location'])
def listener_location(message):
    bot.send_message(message.chat.id, "I's location")

if __name__ == '__main__':
        os.environ['http_proxy'] = 'http://datahub-20:8888'
        os.environ['https_proxy'] = 'http://datahub-20:8888'
        bot.polling(none_stop=True)
        os.environ['http_proxy'] = 'http://localhost:3128/'
        os.environ['https_proxy'] = 'http://localhost:3128/'
