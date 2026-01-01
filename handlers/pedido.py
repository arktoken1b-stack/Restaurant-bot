
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from models.pedido_model import crear_pedido

async def pedido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pedido_id = crear_pedido(update.effective_chat.id)

    keyboard = [
        [InlineKeyboardButton("🍗 Pollo", callback_data=f"plato_pollo_{pedido_id}")],
        [InlineKeyboardButton("🍔 Hamburguesa", callback_data=f"plato_burger_{pedido_id}")],
        [InlineKeyboardButton("➡️ Siguiente", callback_data=f"siguiente_{pedido_id}")]
    ]

    await update.message.reply_text(
        f"🧾 Pedido #{pedido_id}\nSelecciona los platos:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
