from telebot import *
from tarjimoon import tarjimon

bot = TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

@bot.message_handler(commands= ['start'])
def start(msg):
    bot.send_message(msg.chat.id , "Salom men tarjimon botman")

@bot.message_handler(content_types = ['text'])
def tarjima(matn):
    bot.send_message(matn.chat.id , f"{tarjimon(matn.text)}")

bot.polling() 