from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from scrap import *
import os
from dotenv import load_dotenv


load_dotenv()
onServer=True
PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.getenv("TOKEN")

async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def getPrecioMLC(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'{getElToqueMLCPrice()}\nFuente: eltoque.com')


# app = ApplicationBuilder().token(os.getenv("TOKEN")).build()

# app.add_handler(CommandHandler("help", help))

# app.add_handler(CommandHandler("ayuda", help))

# app.add_handler(CommandHandler("preciosDivisas", getPrecioMLC))

      
def main():
  ############################# Handlers #########################################
  updater = Updater(TOKEN, use_context=True)

  dp = updater.dispatcher

  dp.add_handler(CommandHandler('help', help))
  dp.add_handler(CommandHandler('ayuda', help))
  dp.add_handler(CommandHandler('preciosDivisas', getPrecioMLC))

  updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
  updater.bot.setWebhook('https://mlctelegrambot.herokuapp.com/' + TOKEN)

  updater.start_polling()
  updater.idle()
  ################################################################################

if __name__ == '__main__':
    main()