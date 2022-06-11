from telebot.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from model.services.themoviedb_service.configuration import IMAGE_BASE_URL, PosterSize


class InlineQueryResultArticleView:
    def __init__(self, controller):
        self.controller = controller

    def show_search_results(self, search_results, inline_query, offset):
        movie_result_articles = []
        star_char = chr(11088)

        for index, result in enumerate(search_results):
            thumb_url = f'{IMAGE_BASE_URL}{PosterSize.W92.value}{result.poster_path}' if result.poster_path else ''
            poster_url = f'{IMAGE_BASE_URL}{PosterSize.ORIGINAL.value}{result.poster_path}' if result.poster_path else ''

            release_year = f"({result.release_year})" if result.release_year else ''
            ratings_part = f'<b>{star_char}</b> {result.vote_average}' if result.vote_average > 0 else 'No ratings'

            inline_query_result_description = (f'{star_char} {result.vote_average}\n'
                                               f'{", ".join(result.genres)}'
                                               if result.vote_average > 0 else f'{", ".join(result.genres)}')

            input_msg = (f'<b>{result.title} {release_year}</b>\n'
                         f'{", ".join(result.genres)}\n'
                         f'{ratings_part}\n'
                         f'{result.overview if result.overview else ""}<a href="{poster_url}">&#8205;</a>')

            # TODO add markup util
            btn_text = 'DETAILS'
            markup = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text=btn_text, url=result.url)
            markup.add(btn)

            movie_article = InlineQueryResultArticle(
                id=result.id,
                title=f'{result.title} {release_year}',
                description=inline_query_result_description,
                reply_markup=markup,
                input_message_content=InputTextMessageContent(
                    message_text=input_msg,
                    parse_mode='HTML',
                    disable_web_page_preview=False
                ),
                thumb_url=thumb_url
            )
            movie_result_articles.append(movie_article)

        self.controller.answer_inline_query(
            inline_query_id=inline_query.id,
            results=movie_result_articles,
            next_offset=offset,
            cache_time=0,
            is_personal=True
        )
