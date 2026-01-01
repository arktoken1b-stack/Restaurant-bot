import os
import psycopg2

DATABASE_URL = os.getenv("postgresql://restaurant_db_w2yj_user:r3PK7YSftqvfmCNULcZ6Eku5oEavhBuc@dpg-d5baukuuk2gs73f64tog-a.virginia-postgres.render.com/restaurant_db_w2yj")

def get_connection():
    return psycopg2.connect(DATABASE_URL)
