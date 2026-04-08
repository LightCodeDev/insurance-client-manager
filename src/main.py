from ui import pedir_datos_cliente, mostrar_mensaje, mostrar_error, mostrar_clientes, pedir_id_cliente, mostrar_cliente
from services import registrar_cliente, listar_clientes, buscar_cliente_por_id

def main():
    opcion = input("Escribe 1 para registrar o 2 para listar: ")

    if opcion == "1":
        datos = pedir_datos_cliente()
        exito, mensaje = registrar_cliente(*datos)

        if exito:
            mostrar_mensaje(mensaje)
        else:
            mostrar_error(mensaje)

    elif opcion == "2":
        clientes = listar_clientes()
        mostrar_clientes(clientes)

    elif opcion == "3":
        id_cliente = pedir_id_cliente()
        exito, resultado = buscar_cliente_por_id(id_cliente)

        if exito:
            mostrar_cliente(resultado)
        else:
            mostrar_error(resultado)

    else:
        mostrar_error("Opción no válida")

if __name__ == "__main__":
    main()