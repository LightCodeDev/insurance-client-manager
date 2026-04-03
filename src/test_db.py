import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!!!!!!!!!",
    database="saas_seguros"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

resultados = cursor.fetchall()

for cliente in resultados:
    print(cliente)

cursor.close()
conexion.close()