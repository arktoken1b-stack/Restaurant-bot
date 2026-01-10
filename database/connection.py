import psycopg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(
    DATABASE_URL,
    autocommit=True
)
