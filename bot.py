'''Learn Python 28
Урок 1 Telegram эхо-чат-бот
использовал python-telegram-bot 20.1'''


import logging
import settings

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    filename='bot.log',
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('Бот стартовал')
    await update.message.reply_text(f'Здравствуй {update.effective_user.first_name}')

async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    logging.info(text)
    await update.message.reply_text(text)

def main() -> None:
    mybot = ApplicationBuilder().token(settings.API_KEY).build()
    mybot.add_handler(CommandHandler('start', greet_user))
    mybot.add_handler(MessageHandler(filters.TEXT, talk_to_me))

    mybot.run_polling()

if __name__ == '__main__':
    main()
