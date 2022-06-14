from datetime import datetime

from telebot.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from model.tv_show import TVShow


class TVShowResultArticle(InlineQueryResultArticle):
    TV_SHOW_TITLE = 'TV Show'
    THUMB_PLACEHOLDER = 'https://user-images.githubusercontent.com/106914205/177016124-241beb1f-1167-4163-bd4c-3e7afa6627c3.jpg'
    POSTER_PLACEHOLDER = 'https://user-images.githubusercontent.com/106914205/177016114-94fd391f-b7c8-4427-86bc-b5f50717ed8d.jpg'
    STAR_CHAR = chr(11088)

    def __init__(self, tv_show):
        super().__init__(tv_show.id, title='', input_message_content=InputTextMessageContent(''))
        self._tv_show: TVShow = tv_show
        self.title: str = self._title()
        self.description: str = self._description()
        self.reply_markup: InlineKeyboardMarkup = self._reply_markup()
        self.input_message_content: InputTextMessageContent = self._input_message_content()
        self.thumb_url: str = self._thumb_url()

    def _title(self):
        release_year = f'({datetime.strptime(self._tv_show.first_air_date, "%Y-%m-%d").year})' if self._tv_show.first_air_date else ''
        return f'{self._tv_show.name} {release_year}'

    def _description(self):
        if self._tv_show.vote_average and self._tv_show.vote_average > 0:
            desc_first_line = f'{self.STAR_CHAR} {self._tv_show.vote_average}  {self.TV_SHOW_TITLE}\n'
        else:
            desc_first_line = f'No ratings  {self.TV_SHOW_TITLE}\n'

        desc_second_line = f'{", ".join(self._tv_show.genres)}' if self._tv_show.genres else ''
        description = f'{desc_first_line}{desc_second_line}'

        return description

    def _reply_markup(self):
        return InlineKeyboardMarkup().add(InlineKeyboardButton(text='DETAILS', url=self._tv_show.url))

    def _input_message_content(self):
        msg_first_line = f'<b>{self.title}</b>\n'
        msg_second_line = f'{", ".join(self._tv_show.genres)}\n' if self._tv_show.genres else ''
        msg_third_line = f'<b>{self.STAR_CHAR}</b> {self._tv_show.vote_average}\n' if self._tv_show.vote_average > 0 else 'No ratings\n'
        poster_url = self._tv_show.poster_url if self._tv_show.poster_url else self.POSTER_PLACEHOLDER
        msg_fourth_line = f'{self._tv_show.overview if self._tv_show.overview else ""}<a href="{poster_url}">&#8205;</a>'
        input_msg = f'{msg_first_line}{msg_second_line}{msg_third_line}{msg_fourth_line}'

        return InputTextMessageContent(
            message_text=input_msg,
            parse_mode='HTML',
            disable_web_page_preview=False)

    def _thumb_url(self):
        if not self._tv_show.thumb_url:
            return self.THUMB_PLACEHOLDER
        return self._tv_show.thumb_url
