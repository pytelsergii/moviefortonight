import os

import telebot
from flask import Flask
from flask import request

import logger
from controller.bot_controller import bot
from misc import HEROKU_APP_URL, MFT_TOKEN

app = Flask(__name__)


@app.route('/' + MFT_TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=HEROKU_APP_URL)
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    logger.setup_logging()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
