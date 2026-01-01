from utils.database.db import get_connection

def crear_pedido(chat_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO pedidos (chat_id, estado) VALUES (%s, %s) RETURNING id",
                (chat_id, "creando")
            )
            pedido_id = cur.fetchone()[0]
            return pedido_id
