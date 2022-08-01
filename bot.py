from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from scrap import *
import os
from dotenv import load_dotenv

PORT = int(os.environ.get('PORT', 5000))
load_dotenv()

TOKEN = os.getenv("TOKEN")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def getPrecioMLC(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{getElToqueMLCPrice()}\nFuente: eltoque.com')


updater = Updater(TOKEN, use_context=True)

def main():
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("ayuda", help))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("preciosDivisas", getPrecioMLC))

    # # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))



    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=TOKEN)
    updater.bot.setWebhook('https://mlctelegrambot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()