#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config
import telebot

import subprocess

from subprocess import Popen, PIPE

bot = telebot.TeleBot(config.token)
  
#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
#    bot.send_message(message.chat.id, message.text)

cmd = 'ping google.com -c 3'
PIPE = subprocess.PIPE

p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()

#p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
#while True:
 #   s = p.stdout.readline()
  #  if not s: break
   # print(s), 
print(p)
    
cmd = 'uname -a'
subprocess.Popen(cmd, shell = True)
    
    
cmd = 'uname -a'
PIPE = subprocess.PIPE
p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
        stderr=subprocess.STDOUT, close_fds=True, cwd='/home/')
print(p.stdout.read())

@bot.message_handler(content_types=["text"])

def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, p)

if __name__ == '__main__':
     bot.polling(none_stop=True)

    
