
from telegram import Update
from telegram.ext import ContextTypes

async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("plato_"):
        await query.edit_message_text("🍽 Plato agregado")

    elif data.startswith("siguiente_"):
        await query.edit_message_text("➡️ Continuando con el pedido...")
