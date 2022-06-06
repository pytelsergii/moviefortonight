from telebot.types import InlineQueryResultArticle, InputTextMessageContent


def inline_movies_results(movie_response):
    movie_result_articles = []
    new_ln = '\n'
    star_char = chr(11088)
    for index, result in enumerate(movie_response.results):
        release_year = f"({result.release_date.split('-')[0]})" if result.release_date else ''
        movie_article = InlineQueryResultArticle(
            id=index,
            title=f'{result.title} {release_year}',
            description=f'{star_char} {result.vote_average}{new_ln}{", ".join(result.genres)}',
            input_message_content=InputTextMessageContent(result.title),
            thumb_url=result.poster_path if result.poster_path else ''
        )
        movie_result_articles.append(movie_article)

    return movie_result_articles
