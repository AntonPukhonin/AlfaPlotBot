# coding: utf-8
import time
import telebot
from telebot import types
import config
import os

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['info', 'help'])
def command_help(message):
    bot.send_message(message.chat.id, "Для начала работы с ботом, введите /start")

@bot.message_handler(commands=['start'])
def handle_start(message):
        markup = types.ReplyKeyboardMarkup()
        markup.row('Траты')
        markup.row('Курсы', 'Пифы')
        msg = bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
        bot.register_next_step_handler(msg, on_section_click)

def on_section_click(message):
        if message.text == u'Курсы':
                markup = types.ReplyKeyboardMarkup()
                markup.row('Назад')
                markup.row('USD/RUB', 'EUR/RUB')
                msg = bot.send_message(message.chat.id, "Выберите актив:", reply_markup=markup)
                bot.register_next_step_handler(msg, on_currency_click)
        elif message.text == u'Пифы':
                msg = bot.send_message(message.chat.id, "Пока не готово(")
                bot.register_next_step_handler(msg, on_section_click)
        elif message.text == u'Траты':
                msg = bot.send_message(message.chat.id, "Пока не готово(")
                bot.register_next_step_handler(msg, on_section_click)

def on_currency_click(message):
        if message.text == u'Назад':
            handle_start(message)
        elif message.text == u'USD/RUB':
            msg = bot.send_photo(message.chat.id, open('kitten.jpg', 'rb'))
            bot.register_next_step_handler(msg, on_currency_click)
        elif message.text == u'EUR/RUB':
            msg = bot.send_photo(message.chat.id, open('rooster.jpg', 'rb'))
            bot.register_next_step_handler(msg, on_currency_click)

@bot.message_handler(func=lambda message: True, content_types=['location'])
def listener_location(message):
    bot.send_message(message.chat.id, "I's location")

@bot.message_handler(func=lambda message: message.text == u'Философия')
def go_philosophy(message):
    bot.send_message(message.chat.id, 'В чём смысл жизни? Что я здесь делаю?')

bot.polling()

if __name__ == '__main__':
        os.environ['http_proxy'] = 'http://datahub-20:8888'
        os.environ['https_proxy'] = 'http://datahub-20:8888'
        bot.polling(none_stop=True)
        os.environ['http_proxy'] = 'http://localhost:3128/'
        os.environ['https_proxy'] = 'http://localhost:3128/'
