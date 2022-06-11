import telebot

from misc import MFT_TOKEN
from model.movie_search_model import MovieSearchModel
from view.commands_message_view import CommandsMessageView
from view.inline_query_result_article_view import InlineQueryResultArticleView

bot = telebot.TeleBot(token=MFT_TOKEN, parse_mode=None)
search_results_model = MovieSearchModel()
inline_article_view = InlineQueryResultArticleView(bot)
commands_message_view = CommandsMessageView(bot)


@bot.message_handler(commands=['start', 'help'])
def handle_welcome_message(message):
    commands_message_view.send_welcome_message(message)


@bot.inline_handler(lambda query: len(query.query) > 0)
def handle_search_query(inline_query):
    offset = int(inline_query.offset) if inline_query.offset else 1
    search_results = search_results_model.get_search_results(inline_query.query, offset)
    # Stop searching if there is no results
    offset = offset + 1 if len(search_results) > 0 else ''
    inline_article_view.show_search_results(search_results, inline_query, offset)


@bot.inline_handler(lambda query: len(query.query) == 0)
def handle_empty_query(inline_query):
    # This needed to clear previous results
    bot.answer_inline_query(inline_query.id, [])
