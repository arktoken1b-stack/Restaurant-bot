import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot listo como {bot.user}")

# Cargar cogs
initial_extensions = [
    "cogs.admin.add_food",
    "cogs.admin.add_soda",
    "cogs.admin.add_extra",
    "cogs.admin.edit_command",
    "cogs.orders.new_order",
    "cogs.orders.view_orders"
]

for ext in initial_extensions:
    try:
        bot.load_extension(ext)
    except Exception as e:
        print(f"❌ Error cargando {ext}: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))
