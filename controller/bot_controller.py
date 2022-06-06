import telebot

from misc import MFT_TOKEN
from model.services.themoviedb_service import movie_db_service
from view.inline_search import inline_movies_results

bot = telebot.TeleBot(token=MFT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'HI')


@bot.inline_handler(lambda query: len(query.query) > 0)
def handle_search_query(inline_query):
    response = movie_db_service.search_movie(inline_query.query)
    if response:
        articles = inline_movies_results(response)
        if articles:
            bot.answer_inline_query(inline_query.id, articles)


@bot.inline_handler(lambda query: len(query.query) == 0)
def handle_empty_query(inline_query):
    # This needed to clear previous results
    bot.answer_inline_query(inline_query.id, [])
