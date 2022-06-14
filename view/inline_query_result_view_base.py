from telebot.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton


class BaseInlineQueryResultView:
    THUMB_URL = 'https://user-images.githubusercontent.com/106914205/173371421-d516836d-a96a-4e3b-adf5-786e8a36202b.png'
    NO_RESULTS_TITLE = 'NO RESULTS FOUND'

    def __init__(self, controller):
        self._controller = controller

    def show_no_results_found(self, inline_query):
        no_results = InlineQueryResultArticle(
            id=-1,
            title=self.NO_RESULTS_TITLE,
            description='Please try again',
            input_message_content=InputTextMessageContent(message_text=self.NO_RESULTS_TITLE),
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(text='TRY AGAIN', switch_inline_query_current_chat='')),
            thumb_url=self.THUMB_URL
        )
        self._controller.answer_inline_query(
            inline_query_id=inline_query.id,
            results=[no_results],
            cache_time=0
        )
