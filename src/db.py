import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def conectar_db():
    conexion = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
     )
    return conexion

def crear_tabla_clientes():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        dui VARCHAR(20),
        telefono VARCHAR(20),
        correo VARCHAR(100),
        tipo_seguro VARCHAR(50),
        fecha_pago DATE,
        estado_pago VARCHAR(20),
        observaciones TEXT,
        documentos,         
        fecha_registro DATE DEFAULT CURRENT_DATE
    )
    """)

    conexion.commit()
    cursor.close()
    conexion.close()

def insertar_cliente(nombre, dui, telefono, correo, tipo_seguro, fecha_pago, estado_pago, observaciones, documentos):
    conexion = conectar_db()
    cursor = conexion.cursor()

    query = """
    INSERT INTO clientes (
        nombre,
        dui,
        telefono,
        correo,
        tipo_seguro,
        fecha_pago,
        estado_pago,
        observaciones,
        documentos
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        nombre,
        dui,
        telefono,
        correo,
        tipo_seguro,
        fecha_pago,
        estado_pago,
        observaciones,
        documentos
    )

    try:
        cursor.execute(query, valores)
        conexion.commit()
        return True
    except Exception as e:
        return False
    finally:
        cursor.close()
        conexion.close()