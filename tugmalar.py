from telebot import *

bot = TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

# tugmalar = types.ReplyKeyboardMarkup(resize_keyboard=True)

# tugma1 = types.KeyboardButton("Hi")
# tugma2 = types.KeyboardButton("Hello")

tugmalar = types.InlineKeyboardMarkup(row_width=2)

tugma1 = types.InlineKeyboardButton("Salom" , callback_data="S")
tugma2 = types.InlineKeyboardButton("Hello" , callback_data="H")

# tugmalar.add(tugma1)
# tugmalar.add(tugma2)

tugmalar.add(tugma1 , tugma2)

@bot.message_handler(commands = ['start'])
def start(msg):
    bot.send_message(msg.chat.id , "Salom" , reply_markup= tugmalar)

# @bot.message_handler(content_types= ['text'])
# def body(msg):
#     if msg.text == "Hi":
#         bot.send_message(msg.chat.id, "Hello")
#     elif msg.text == "Hello":
#         bot.send_message(msg.chat.id,  "Hi")

@bot.callback_query_handler(func=lambda call:True)
def query(call):
    if call.data == "S":
        bot.send_message(call.message.chat.id, "Hello")
    elif call.data == "H":
        bot.send_message(call.message.chat.id , "Salom")


bot.polling()    