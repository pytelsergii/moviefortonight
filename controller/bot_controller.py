import telebot

from misc import MFT_TOKEN
from model.multi_search_model import MultiSearchModel
from model.services.themoviedb_service.movie_db_service import TheMovieDBService
from view.commands_message_view import CommandsMessageView
from view.multi_search_view import MultiSearchView

bot = telebot.TeleBot(token=MFT_TOKEN, parse_mode=None)
service = TheMovieDBService()
multi_search_model = MultiSearchModel(service)
multi_search_view = MultiSearchView(bot)
commands_message_view = CommandsMessageView(bot)


@bot.message_handler(commands=['start', 'help'])
def handle_welcome_message(message):
    commands_message_view.send_welcome_message(message)


@bot.inline_handler(lambda query: len(query.query) > 0)
def handle_search_query(inline_query):
    offset = int(inline_query.offset) if inline_query.offset else 1
    search_results = multi_search_model.get_multi_search_results(inline_query.query, offset)
    # Stop searching if there is no results
    offset = offset + 1 if len(search_results) > 0 else ''
    multi_search_view.show_multi_search_results(search_results, inline_query, offset)


@bot.inline_handler(lambda query: len(query.query) == 0)
def handle_empty_query(inline_query):
    # This needed to clear previous results
    bot.answer_inline_query(inline_query.id, [])
