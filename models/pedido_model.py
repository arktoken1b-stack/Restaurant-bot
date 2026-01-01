
from utils.database.db import get_connection

def crear_pedido(chat_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO pedidos (chat_id, estado) VALUES (%s, %s) RETURNING id",
        (chat_id, "creando")
    )
    pedido_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return pedido_id
