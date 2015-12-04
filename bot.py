# -*- coding: utf-8 -*-

import config
import telebot
import time
import os

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            bot.send_message(m.chat.id, m.text)

if __name__ == '__main__':
     os.environ['http_proxy'] = 'http://datahub-20:8888'
     os.environ['https_proxy'] = 'http://datahub-20:8888'
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)
     os.environ['http_proxy'] = 'http://localhost:3128/'
     os.environ['https_proxy'] = 'http://localhost:3128/'
