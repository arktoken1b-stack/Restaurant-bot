from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)
from config import BOT_TOKEN
from database.init_db import init_db
from handlers.pedido import pedido
from handlers.callbacks import botones

def main():
    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("pedido", pedido))
    app.add_handler(CallbackQueryHandler(botones))

    print("🤖 Bot iniciado correctamente")
    app.run_polling()

if __name__ == "__main__":
    main()
