from typing import List, Union

from telebot import TeleBot
from telebot.types import InlineQuery

from model.movie import Movie
from model.person import Person
from model.services.themoviedb_service.media_type import MediaType
from model.tv_show import TVShow
from view.inline_query_result_view_base import BaseInlineQueryResultView

from view.movie_result_article import MovieResultArticle
from view.person_result_article import PersonResultArticle
from view.tv_show_result_article import TVShowResultArticle


class MultiSearchView(BaseInlineQueryResultView):

    def __init__(self, controller: TeleBot):
        super().__init__(controller)

    def show_multi_search_results(self, search_results: List[Union[Movie, TVShow, Person]], inline_query: InlineQuery,
                                  offset: int) -> None:
        result_articles = []

        for result in search_results:
            media_type = result.media_type

            if media_type == MediaType.MOVIE:
                result_articles.append(MovieResultArticle(result))

            elif media_type == MediaType.TV_SHOW:
                result_articles.append(TVShowResultArticle(result))

            elif media_type == MediaType.PERSON:
                result_articles.append(PersonResultArticle(result))

        self._controller.answer_inline_query(
            inline_query_id=inline_query.id,
            results=result_articles,
            next_offset=offset,
            cache_time=0
        )
