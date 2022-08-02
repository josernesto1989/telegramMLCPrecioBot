from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from scrap import *
import os
from dotenv import load_dotenv


load_dotenv()

PORT = int(os.environ.get('PORT', 5000))
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def getPrecioMLC(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{getElToqueMLCPrice()}\nFuente: eltoque.com')


app = ApplicationBuilder().token(os.getenv("TOKEN")).build()

app.add_handler(CommandHandler("help", help))

app.add_handler(CommandHandler("ayuda", help))

app.add_handler(CommandHandler("preciosDivisas", getPrecioMLC))

app.run_polling()

# app.run_webhook(listen="0.0.0.0", port=PORT, url_path=os.getenv("TOKEN"))
# app.bot.setWebhook('https://mlctelegrambot.herokuapp.com/' + os.getenv("TOKEN"))
# app.run_polling()
# app.run_webhook(
#     listen='0.0.0.0',
#     port=5000,
#     url_path='TOKEN',
#     webhook_url='https://mlctelegrambot.herokuapp.com/'+os.getenv("TOKEN")
#     # cert='cert_bot1.pem'
#     )
