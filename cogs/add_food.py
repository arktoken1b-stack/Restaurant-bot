import discord
from discord.ext import commands
from database.connection import conn

class AddFood(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="addfood",
        description="Agregar una comida"
    )
    async def add_food(self, interaction: discord.Interaction, nombre: str, precio: float):
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO foods (name, price) VALUES (%s, %s)",
                (nombre, precio)
            )

        await interaction.response.send_message(
            f"🍔 **{nombre}** agregado a S/{precio}"
        )

async def setup(bot):
    await bot.add_cog(AddFood(bot))
