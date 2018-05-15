import logging
import telebot
import config

from krasuvo import make_krasuvo


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('BOT')
logger.info('Hello from bot')

bot = telebot.TeleBot(config.token)


@bot.inline_handler(func=lambda query: str(query.query).strip())
def query_text(query):
    text = str(query.query)
    logger.info('New query: "{}"'.format(text))
    res_text = make_krasuvo(text)
    res = telebot.types.InlineQueryResultArticle(
        id='1',
        title='Click to send message K P A C U B O',
        input_message_content=telebot.types.InputTextMessageContent(
            message_text=res_text,
            parse_mode='HTML'
        )
    )
    bot.answer_inline_query(query.id, [res])


if __name__ == '__main__':
    bot.polling(none_stop=True)

logger.info('Bot says "Goodbye!"')
