from telebot import *

bot = TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

@bot.message_handler(commands= ['start'])
def start(message):
    a = bot.send_message(message.chat.id , "Blue - so'zini tarjimasi:")
    bot.register_next_step_handler(a , steep1)

def steep1(msg):
    if msg.text == "Ko'k":
        bot.send_message(msg.chat.id, "Tog'ri")
        a = bot.send_message(msg.chat.id , "Red - so'zini manosi?")
        bot.register_next_step_handler(a , steep2)
    else:
        a = bot.send_message(msg.chat.id , "Notog'ri")    
        bot.register_next_step_handler(a , start)

def steep2(msg):
    if msg.text == "qizil":
        bot.send_message(msg.chat.id, "Tog'ri")
      
    else:
        a = bot.send_message(msg.chat.id , "Notog'ri")    
        bot.register_next_step_handler(a , steep1)


bot.polling()