
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
    for cliente in clientes:
        print(cliente)