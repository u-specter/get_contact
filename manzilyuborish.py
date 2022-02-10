from distutils import command
from telebot import *
from geopy import Nominatim

bot = TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(types.KeyboardButton("manzil jonatish", request_location=True))

@bot.message_handler(commands = ['start'])
def start(message):
    msg = bot.send_message(message.chat.id , "Assalomu alaykum",  reply_markup=markup)
    bot.register_next_step_handler(msg , get_location)
    
def get_location(message):
    if message.location is None:
        msg = bot.send_message(message.chat.id, "Iltimos, tugmani bosing", reply_markup=markup)
        bot.register_next_step_handler(msg, get_location)
    else:
        geo = Nominatim(user_agent="geoapiExercises")    
        location = geo.geocode(str(message.location.latitude)+","+str(message.location.longitude))
        bot.send_message(message.chat.id, f"Sizning manzilingiz - {location}")

bot.polling()
