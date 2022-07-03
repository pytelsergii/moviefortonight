from telebot.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

from model.person import Person
from model.services.themoviedb_service.media_type import MediaType


class PersonResultArticle(InlineQueryResultArticle):
    PERSON_TITLE = 'Person'
    THUMB_PLACEHOLDER = 'https://user-images.githubusercontent.com/106914205/177016383-a7bb712e-df8f-4881-9be0-6db84a3f378e.jpg'
    POSTER_PLACEHOLDER = 'https://user-images.githubusercontent.com/106914205/177016380-fb47cd48-5a19-44d1-8b8d-52dec2d80419.jpg'
    STAR_CHAR = chr(11088)

    def __init__(self, person: Person):
        super().__init__(person.id, title='', input_message_content=InputTextMessageContent(''))
        self._person: Person = person
        self.title: str = self._title()
        self.description: str = self._description()
        self.reply_markup: InlineKeyboardMarkup = self._reply_markup()
        self.input_message_content: InputTextMessageContent = self._input_message_content()
        self.thumb_url: str = self._thumb_url()

    def _title(self):
        return self._person.name

    def _description(self):
        known_for = []
        for item in self._person.known_for:
            if item.media_type == MediaType.MOVIE:
                known_for.append(item.title)
            elif item.media_type == MediaType.TV_SHOW:
                known_for.append(item.name)

        return ', '.join(known_for) if known_for else ''

    def _reply_markup(self):
        return InlineKeyboardMarkup().add(InlineKeyboardButton(text='DETAILS', url=self._person.url))

    def _input_message_content(self):
        msg_first_line = f'<b>{self.title}</b>\n'
        msg_second_line = f'{self.description}'
        msg_third_line = f''
        poster_url = self._person.poster_url if self._person.poster_url else self.POSTER_PLACEHOLDER
        msg_fourth_line = f'<a href="{poster_url}">&#8205;</a>'
        input_msg = f'{msg_first_line}{msg_second_line}{msg_third_line}{msg_fourth_line}'

        return InputTextMessageContent(
            message_text=input_msg,
            parse_mode='HTML',
            disable_web_page_preview=False)

    def _thumb_url(self):
        if not self._person.thumb_url:
            return self.THUMB_PLACEHOLDER
        return self._person.thumb_url
