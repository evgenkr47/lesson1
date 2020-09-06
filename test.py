import telebot
from telebot import types
bot = telebot.TeleBot("1303754511:AAGuU54t24WpqkOm4GArg69K2eWYhQCIxdg")

@bot.message_handler(commands=['start', 'help'])
def main(message):
	keyboard = types.InlineKeyboardMarkup()
	url_btn = types.InlineKeyboardButton(text="Ну смотри, не стесняйся", url="https://www.instagram.com/evgen_fitguide/")
	keyboard.add(url_btn)
	bot.send_message(message.chat.id, "Хочешь посмотреть на обладателя ПЕНИСА 15 см?", reply_markup=keyboard)


bot.polling(none_stop=True)