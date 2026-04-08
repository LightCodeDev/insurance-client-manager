from ui import pedir_datos_cliente, mostrar_mensaje, mostrar_error, mostrar_clientes, pedir_id_cliente, mostrar_cliente, pedir_nombre_busqueda
from services import registrar_cliente, listar_clientes, buscar_cliente_por_id, buscar_clientes_por_nombre

def mostrar_menu():
    print("\n" + "=" * 40)
    print("   SISTEMA DE GESTIÓN DE CLIENTES")
    print("=" * 40)
    print("1. Registrar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente por ID")
    print("4. Buscar cliente por nombre")
    print("0. Salir")
    print("=" * 40)

    return input("Seleccione una opción: ").strip()

def main():
    opcion = mostrar_menu()

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

    elif opcion == "4":
        nombre = pedir_nombre_busqueda()
        exito, resultado = buscar_clientes_por_nombre(nombre)

        if exito:
            mostrar_clientes(resultado)
        else:
            mostrar_error(resultado)

    else:
        mostrar_error("Opción no válida")

if __name__ == "__main__":
    main()