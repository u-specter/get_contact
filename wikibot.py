from telebot import *
import wikipedia
from telegraph import Telegraph

wikipedia.set_lang("uz")

telegraph = Telegraph()
telegraph.create_account(short_name='WikiBot')

def url(title):
    info = wikipedia.summary("title")
    responce = telegraph.create_page(f'{title}',html_content=f'<p>{info}</p>')
    return responce["url"]


bot = TeleBot("1735077707:AAFGH_HAqDz7wD6lwA1r9OHHJK-X9lqJFsY")

@bot.message_handler(commands= ['start'])
def start(message):
    text = f"Assalomu alaykum {message.from_user.first_name}, men wikipediadan malumot topib beraman va menga soz yuboring"
    bot.send_message(message.chat.id , text)

@bot.message_handler(content_types= 'text')
def wiki(message):
    try:
        bot.send_message(message.chat.id , url(message.text))
    except:
        bot.send_message(message.chat.id , "Afsus oxshamadi(")
bot.polling()    