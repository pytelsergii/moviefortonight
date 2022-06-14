from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class CommandsMessageView:
    SEARCH_TITLE = 'SEARCH'

    def __init__(self, controller):
        self._controller: TeleBot = controller

    def send_welcome_message(self, message: Message) -> None:
        welcome_message = ('MovieForTonight bot can help you find and share movies, tv shows and people.'
                           'It works in any chat, simply type @movieftbot in the text field.')

        self._controller.send_message(
            chat_id=message.chat.id,
            text=welcome_message,
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(text=self.SEARCH_TITLE, switch_inline_query_current_chat='')),
            parse_mode='HTML',
            disable_web_page_preview=True
        )
