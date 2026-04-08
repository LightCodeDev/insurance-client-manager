from db import insertar_cliente, obtener_clientes_por_nombre, obtener_clientes, obtener_cliente_por_id
from config import TIPOS_SEGURO, ESTADOS_PAGO

def registrar_cliente(nombre, dui, telefono, correo, tipo_seguro, fecha_pago, estado_pago, observaciones, documentos):

    nombre = nombre.strip()
    dui = dui.strip()
    telefono = telefono.strip()
    correo = correo.strip().lower()
    tipo_seguro = tipo_seguro.strip().lower()
    estado_pago = estado_pago.strip().lower()
    fecha_pago = fecha_pago.strip()
    observaciones = observaciones.strip() if observaciones else ""
    documentos = documentos.strip() if documentos else ""

    if not nombre:
        return False, "El nombre es obligatorio"

    if not dui:
        return False, "El dui es obligatorio"

    if not telefono:
        return False, "El telefono es obligatorio"

    if not correo:
        return False, "El correo es obligatorio"

    if not tipo_seguro:
        return False, "El tipo de seguro es obligatorio"

    if not fecha_pago:
        return False, "La fecha de pago es obligatoria"

    if not estado_pago:
        return False, "El estado de pago es obligatorio"

    if "@" not in correo:
        return False, "Correo inválido"

    if tipo_seguro not in TIPOS_SEGURO:
        return False, "Tipo de seguro no válido"

    if estado_pago not in ESTADOS_PAGO:
        return False, "Estado de pago no válido"

    resultado = insertar_cliente(
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

    if resultado:
        return True, "Cliente registrado correctamente"
    else:
        return False, "Error al registrar el cliente"
    
def listar_clientes():
    return obtener_clientes()

def buscar_cliente_por_id(id_cliente):
    cliente = obtener_cliente_por_id(id_cliente)

    if cliente is not None:
        return True, cliente
    else:
        return False, "Cliente no encontrado."
    
def buscar_clientes_por_nombre(nombre):
        clientes = obtener_clientes_por_nombre(nombre)

        if len(clientes) > 0:
            return True, clientes
        else:
            return False, "No se encontraron clientes."