from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class CommandsMessageView:

    def __init__(self, controller):
        self._controller = controller

    def send_welcome_message(self, message):
        welcome_message = ('MovieForTonight bot can help you find and share movies.'
                           'It works in any chat, simply type @movieftbot in the text field.')

        self._controller.send_message(
            chat_id=message.chat.id,
            text=welcome_message,
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(text='SEARCH FOR A MOVIE', switch_inline_query_current_chat='')),
            parse_mode='HTML',
            disable_web_page_preview=True
        )
