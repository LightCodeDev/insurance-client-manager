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
        observaciones TEXT
    )
    """)

    conexion.commit()
    cursor.close()
    conexion.close()