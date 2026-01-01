from database.db import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Tabla pedidos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id SERIAL PRIMARY KEY,
        cliente_nombre TEXT,
        direccion TEXT,
        metodo_pago TEXT,
        total NUMERIC DEFAULT 0,
        delivery NUMERIC DEFAULT 1.00,
        estado TEXT DEFAULT 'pendiente',
        creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Tabla platos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS platos (
        id SERIAL PRIMARY KEY,
        nombre TEXT,
        precio NUMERIC
    );
    """)

    # Tabla de los platos de cada pedido
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pedido_platos (
        id SERIAL PRIMARY KEY,
        pedido_id INTEGER REFERENCES pedidos(id),
        plato_id INTEGER REFERENCES platos(id),
        cantidad INTEGER
    );
    """)

    # Tabla acompañamientos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS acompanamientos (
        id SERIAL PRIMARY KEY,
        nombre TEXT
    );
    """)

    # Tabla acompañamientos por pedido
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pedido_acompanamientos (
        id SERIAL PRIMARY KEY,
        pedido_plato_id INTEGER REFERENCES pedido_platos(id),
        acompanamiento_id INTEGER REFERENCES acompanamientos(id)
    );
    """)

    # Tabla gaseosas
    cur.execute("""
    CREATE TABLE IF NOT EXISTS gaseosas (
        id SERIAL PRIMARY KEY,
        nombre TEXT,
        precio NUMERIC
    );
    """)

    # Tabla gaseosas por pedido
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pedido_gaseosas (
        id SERIAL PRIMARY KEY,
        pedido_id INTEGER REFERENCES pedidos(id),
        gaseosa_id INTEGER REFERENCES gaseosas(id),
        cantidad INTEGER
    );
    """)

    # Tabla cremas
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cremas (
        id SERIAL PRIMARY KEY,
        nombre TEXT
    );
    """)

    # Tabla cremas por pedido
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pedido_cremas (
        id SERIAL PRIMARY KEY,
        pedido_id INTEGER REFERENCES pedidos(id),
        crema_id INTEGER REFERENCES cremas(id),
        cantidad INTEGER
    );
    """)

    conn.commit()
    cur.close()
    conn.close()
