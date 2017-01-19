#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config
import telebot

import subprocess

bot = telebot.TeleBot(config.token)
  
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    
subprocess.call('uname -a', shell=True)

if __name__ == '__main__':
     bot.polling(none_stop=True)
