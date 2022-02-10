from telebot import *
from main import CBU

bot = TeleBot("5193299930:AAFFb8g1mh09WGM9Y-K3lNu6sXNrxEJUWNs")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("USD" )
markup.add("RUB", "AED", "KZT")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id , "Salom men valyuta kursi haqida malumotlar beraman", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def body(message):
    try:
        if message.text == "RUB":
            cbu = CBU("RUB")
            bot.send_message(message.chat.id , f"1 RUB = {cbu.result['Rate']} SO'M ")
        elif message.text == "USD":
            cbu = CBU("USD")
            bot.send_message(message.chat.id , f"1 USD = {cbu.result['Rate']} SO'M ")
        elif message.text == "AED":
            cbu = CBU("AED")  
            bot.send_message(message.chat.id , f"1 DIRHAM = {cbu.result['Rate']} SO'M ")  
        elif message.text == "KZT":
            cbu = CBU("KZT")  
            bot.send_message(message.chat.id , f"1 TENGE = {cbu.result['Rate']} SO'M ") 
    except:
        bot.send_message(message.chat.id , f"Oxshamadiku {message.chat.first_name}!!")           


bot.polling()    