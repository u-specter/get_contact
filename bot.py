import telebot

bot = telebot.TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

@bot.message_handler(commands = ["start"])
def welcome(message):
    bot.send_message(chat_id = message.from_user.id, text=f"Salom {message.from_user.first_name}")

@bot.message_handler(commands= "help")
def help(message):
    bot.send_message(message.chat.id , "Qonday jordem kerak")    

bot.polling()    