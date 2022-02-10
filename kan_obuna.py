from telebot import *
from telebot.types import *

bot = TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton("Umidjon" , url="https://t.me/umidjon_aka"))
markup.add(InlineKeyboardButton("Tekshirish" , callback_data="d"))

def _status(id):
    return bot.get_chat_member(-1001675812693, id).status

@bot.message_handler(commands = ['start'])
def start(message):
    matn = "Assalomu alaykum kanalga obuna boling..."
    bot.send_message(message.chat.id , matn, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query(call):
    status = ["creator" , "adminstartor" , "member"]
    if str(_status(call.message.chat.id)) in status:
        bot.send_message(call.message.chat.id, "Siz kanalga obuna bo'ldingiz")
    else:
        bot.send_message(call.message.chat.id , "Kanalga obuna boling")    

bot.polling()
