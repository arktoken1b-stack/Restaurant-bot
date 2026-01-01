import discord
from discord.ext import commands
from database.db import get_connection

class Pedido(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pedido(self, ctx):
        # Crear nuevo pedido
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

        # Mensaje inicial
        await ctx.send(f"🧾 Pedido creado: #{pedido_id}\nAhora empieza a agregar platos, gaseosas, acompañamientos y cremas.")

def setup(bot):
    bot.add_cog(Pedido(bot))
