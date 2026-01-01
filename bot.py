import os
import discord
from discord.ext import commands
from database.init_db import init_db

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    init_db()
    print(f"Bot conectado como {bot.user}")

# Cargamos comandos
bot.load_extension("commands.pedido")

bot.run(os.getenv("DISCORD_TOKEN"))
