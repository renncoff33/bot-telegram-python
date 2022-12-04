# create by EvanD3v
# mau recode?
# import module
from telebot import *
import re
import random

# create by EvanD3v
# api bot
# isi pake token bot masing²
api = 'Token'
bot = TeleBot(api)

# start nya
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "hai selamat datang di bot EvanD3v")

# chatbot nya
sapa = ['hai juga']
@bot.message_handler(content_types=['text'])
def chatbot(message):
	teks = message.text
	if re.findall('halo|hai', teks):
		chatid = message.chat.id
		bot.send_message(chatid, random.choice(sapa))

	else:
		chatid = message.chat.id
		bot.send_message(chatid, 'bot sedang dalam pengembangan')


# finally :v
print("bot sedang berjalan..")
bot.polling()

