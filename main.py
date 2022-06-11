import os

from flask import Flask

import logger
from controller.bot_controller import bot
from misc import HEROKU_APP_URL

app = Flask(__name__)


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=HEROKU_APP_URL)
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    logger.setup_logging()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
