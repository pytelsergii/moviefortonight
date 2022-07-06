from datetime import datetime

from telebot.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from model.movie import Movie


class MovieResultArticle(InlineQueryResultArticle):
    MOVIE_TITLE = 'Movie'
    THUMB_PLACEHOLDER = 'https://user-images.githubusercontent.com/106914205/177016124-241beb1f-1167-4163-bd4c-3e7afa6627c3.jpg'
    POSTER_PLACEHOLDER = 'https://user-images.githubusercontent.com/106914205/177016114-94fd391f-b7c8-4427-86bc-b5f50717ed8d.jpg'
    STAR_CHAR = chr(11088)

    def __init__(self, movie):
        super().__init__(movie.id, title='', input_message_content=InputTextMessageContent(''))
        self._movie: Movie = movie
        self.title: str = self._title()
        self.description: str = self._description()
        self.reply_markup: InlineKeyboardMarkup = self._reply_markup()
        self.input_message_content: InputTextMessageContent = self._input_message_content()
        self.thumb_url: str = self._thumb_url()

    def _title(self):
        release_year = f'({datetime.strptime(self._movie.release_date, "%Y-%m-%d").year})' if self._movie.release_date else ''
        return f'{self._movie.title} {release_year}' if release_year else f'{self._movie.title}'

    def _description(self):
        if self._movie.vote_average and self._movie.vote_average > 0:
            desc_first_line = f'{self.STAR_CHAR} {self._movie.vote_average}  {self.MOVIE_TITLE}\n'
        else:
            desc_first_line = f'No ratings  {self.MOVIE_TITLE}\n'

        desc_second_line = f'{", ".join(self._movie.genres)}' if self._movie.genres else ''
        description = f'{desc_first_line}{desc_second_line}'
        return description

    def _reply_markup(self):
        return InlineKeyboardMarkup().add(InlineKeyboardButton(text='DETAILS', url=self._movie.url))

    def _input_message_content(self):
        msg_first_line = f'<b>{self.title}</b>\n'
        msg_second_line = f'{", ".join(self._movie.genres)}\n' if self._movie.genres else ''
        overview = self._movie.overview if self._movie.overview else ''
        if self._movie.vote_average and self._movie.vote_average > 0:
            if overview:
                msg_third_line = f'<b>{self.STAR_CHAR}</b> {self._movie.vote_average}\n'
            else:
                msg_third_line = f'<b>{self.STAR_CHAR}</b> {self._movie.vote_average}'
        else:
            msg_third_line = 'No ratings\n' if overview else 'No ratings'
        poster_url = self._movie.poster_url if self._movie.poster_url else self.POSTER_PLACEHOLDER
        msg_fourth_line = f'{overview}<a href="{poster_url}">&#8205;</a>'
        input_msg = f'{msg_first_line}{msg_second_line}{msg_third_line}{msg_fourth_line}'

        return InputTextMessageContent(
            message_text=input_msg,
            parse_mode='HTML',
            disable_web_page_preview=False)

    def _thumb_url(self):
        if not self._movie.thumb_url:
            return self.THUMB_PLACEHOLDER
        return self._movie.thumb_url
