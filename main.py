import telebot
from misc import MFT_TOKEN

bot = telebot.TeleBot(token=MFT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


if __name__ == '__main__':
    bot.infinity_polling()
