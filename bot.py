from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from scrap import *
import os
from dotenv import load_dotenv


load_dotenv()

PORT = int(os.environ.get('PORT', 5000))
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""Este bot consta de los siguientes comandos:\n
    /help este comando
    /ayuda este comando
    /preciosDivisas precio del cambio de las divisas en el mercado informal en Cuba usando de fuente eltoque.com, trataremos de aumentar el número de fuentes en la medida de lo posible
    
    Los precios de compra y venta de divisas los extraemos directamente de nuestras fuentes y no son alterados. El objetivo de este bot es informativo.
    """)

async def getPrecioMLC(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{getElToqueMLCPrice()}\nFuente: eltoque.com')
    await update.message.reply_text(f'{getBCCPrice()}\nFuente: www.bc.gob.cu')


app = ApplicationBuilder().token(os.getenv("TOKEN")).build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("start", help))

app.add_handler(CommandHandler("ayuda", help))

app.add_handler(CommandHandler("preciosDivisas", getPrecioMLC))
app.add_handler(CommandHandler("precio", getPrecioMLC))

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
