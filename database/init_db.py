from database.db import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT,
        estado TEXT,
        total NUMERIC DEFAULT 0,
        direccion TEXT,
        metodo_pago TEXT,
        creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cur.close()
    conn.close()
