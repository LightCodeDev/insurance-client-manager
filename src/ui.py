
def pedir_datos_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    dui = input("Ingrese el DUI del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    tipo_seguro = input("Ingrese el tipo de seguro: ")
    fecha_pago = input("Ingrese la fecha de pago (YYYY-MM-DD): ")
    estado_pago = input("Ingrese el estado de pago: ")
    observaciones = input("Ingrese observaciones (opcional): ")
    documentos = input("Ingrese documentos (opcional): ")

    return nombre, dui, telefono, correo, tipo_seguro, fecha_pago, estado_pago, observaciones, documentos


def mostrar_mensaje(texto):
    print(f"\n>> {texto}\n")


def mostrar_error(texto):
    print(f"\n[ERROR]: {texto}\n")

def mostrar_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        id_cliente, nombre, dui, telefono, correo, tipo_seguro, fecha_pago, estado_pago, observaciones, documentos, fecha_registro = cliente

        print(f"ID: {id_cliente}")
        print(f"Nombre: {nombre}")
        print(f"DUI: {dui}")
        print(f"Teléfono: {telefono}")
        print(f"Correo: {correo}")
        print(f"Seguro: {tipo_seguro}")
        print(f"Fecha de pago: {fecha_pago}")
        print(f"Estado: {estado_pago}")
        print(f"Observaciones: {observaciones if observaciones else 'Sin observaciones'}")
        print(f"Documentos: {documentos if documentos else 'Sin documentos'}")
        print(f"Registro: {fecha_registro}")
        print("-" * 40)

def pedir_id_cliente():
    while True:
        id_cliente = input("¿Cuál es el ID del cliente? ").strip()

        if id_cliente == "":
            print("Respuesta inválida.")
        elif not id_cliente.isdigit():
            print("El ID debe ser un número.")
        else:
            return int(id_cliente)
        
def mostrar_cliente(cliente):
    
    if not cliente:
        print("ID no valido")
        return

    id_cliente, nombre, dui, telefono, correo, tipo_seguro, fecha_pago, estado_pago, observaciones, documentos, fecha_registro = cliente

    print(f"ID: {id_cliente}")
    print(f"Nombre: {nombre}")
    print(f"DUI: {dui}")
    print(f"Teléfono: {telefono}")
    print(f"Correo: {correo}")
    print(f"Seguro: {tipo_seguro}")
    print(f"Fecha de pago: {fecha_pago}")
    print(f"Estado: {estado_pago}")
    print(f"Observaciones: {observaciones if observaciones else 'Sin observaciones'}")
    print(f"Documentos: {documentos if documentos else 'Sin documentos'}")
    print(f"Registro: {fecha_registro}")
    print("-" * 40)