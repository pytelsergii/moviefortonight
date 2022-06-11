from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class CommandsMessageView:

    def __init__(self, controller):
        self._controller = controller

    def send_welcome_message(self, message):
        welcome_message = ('MovieForTonight bot can help you find and share movies.'
                           'It works in any chat, simply type @movieftbot in the text field.')

        btn_text = 'SEARCH FOR A MOVIE'
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton(text=btn_text, switch_inline_query_current_chat='')
        markup.add(btn)

        self._controller.send_message(
            chat_id=message.chat.id,
            text=welcome_message,
            reply_markup=markup,
            parse_mode='HTML',
            disable_web_page_preview=True
        )
