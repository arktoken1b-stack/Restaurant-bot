# utils/keyboard.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def teclado_menu():
    keyboard = [
        [InlineKeyboardButton("🍗 Pollo", callback_data="pollo")],
        [InlineKeyboardButton("🍔 Hamburguesa", callback_data="hamburguesa")],
        [InlineKeyboardButton("✅ Finalizar", callback_data="finalizar")]
    ]
    return InlineKeyboardMarkup(keyboard)
