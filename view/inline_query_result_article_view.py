from telebot.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from model.services.themoviedb_service.configuration import IMAGE_BASE_URL, PosterSize


class InlineQueryResultArticleView:
    def __init__(self, controller):
        self.controller = controller

    def show_search_results(self, search_results, inline_query, offset):
        movie_result_articles = []
        star_char = chr(11088)
        movie_lage_placeholder = 'https://user-images.githubusercontent.com/106914205/173204169-251272b1-7911-4a76-8766-d2056789ca93.png'
        movie_small_placeholder = 'https://user-images.githubusercontent.com/106914205/173204199-48f4c66a-d3e1-4f7c-ad10-a64351463406.png'

        for index, result in enumerate(search_results):
            thumb_url = f'{IMAGE_BASE_URL}{PosterSize.W92.value}{result.poster_path}' if result.poster_path \
                else movie_small_placeholder
            poster_url = f'{IMAGE_BASE_URL}{PosterSize.ORIGINAL.value}{result.poster_path}' if result.poster_path \
                else movie_lage_placeholder
            release_year = f"({result.release_year})" if result.release_year else ''

            # description
            desc_first_line = f'{star_char} {result.vote_average}\n' if result.vote_average > 0 else 'No ratings\n'
            desc_second_line = f'{", ".join(result.genres)}'
            description = f'{desc_first_line}{desc_second_line}'

            # input_message_text
            msg_first_line = f'<b>{result.title} {release_year}</b>\n'
            msg_second_line = f'{", ".join(result.genres)}\n' if result.genres else ''
            msg_third_line = f'<b>{star_char}</b> {result.vote_average}\n' if result.vote_average > 0 else 'No ratings\n'
            msg_fourth_line = f'{result.overview if result.overview else ""}<a href="{poster_url}">&#8205;</a>'
            input_msg = f'{msg_first_line}{msg_second_line}{msg_third_line}{msg_fourth_line}'

            movie_article = InlineQueryResultArticle(
                id=result.id,
                title=f'{result.title} {release_year}',
                description=description,
                reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='DETAILS', url=result.url)),
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
