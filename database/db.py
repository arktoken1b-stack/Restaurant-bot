import os
import psycopg2

# Leer la URL desde la variable de entorno que configuraste en Render
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)
