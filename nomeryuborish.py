from distutils import command
from telebot import *

bot = TeleBot("")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(types.KeyboardButton("raqamni jonatish", request_contact=True))

@bot.message_handler(commands = ['start'])
def start(message):
    msg = bot.send_message(message.chat.id , "Assalomu alaykum",  reply_markup=markup)
    bot.register_next_step_handler(msg , get_number)

def get_number(message):
    if message.contact is None:
        msg = bot.send_message(message.chat.id, "Iltimos, tugmani bosing", reply_markup=markup)
        bot.register_next_step_handler(msg, get_number)
    else:
        bot.send_message(message.chat.id , f"Raqamni qabul qildim - {message.contact.phone_number}")    


bot.polling()
