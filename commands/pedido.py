import discord
from discord.ext import commands
from discord import app_commands
from database.db import get_connection

class Pedido(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="pedido",
        description="Crea un nuevo pedido"
    )
    async def pedido(self, interaction: discord.Interaction):
        # Crear nuevo pedido en la DB
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO pedidos (estado) VALUES (%s) RETURNING id",
            ("pendiente",)
        )
        pedido_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        # Responder en Discord
        await interaction.response.send_message(
            f"🧾 Pedido creado: #{pedido_id}\nAhora puedes agregar platos, gaseosas, acompañamientos y cremas.",
            ephemeral=True  # Solo lo ve el que lo ejecuta
        )

async def setup(bot):
    await bot.add_cog(Pedido(bot))
