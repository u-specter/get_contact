from telebot import *

bot = TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

@bot.message_handler(commands= ['start'])
def start(message):
    bot.send_message(message.chat.id , f"Salom {message.from_user.first_name}")

@bot.message_handler(content_types= ['text'])
def matnlar(message):
    matn = message.text
    if matn == "Salom":
        bot.send_message(message.chat.id , f"Salom {message.from_user.first_name}, yaxshimisiz?")
    else:
        bot.send_message(message.chat.id , "Men siznitushunmadim...")    
      

bot.polling()
