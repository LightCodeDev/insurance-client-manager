from db import insertar_cliente

def registrar_cliente(nombre, dui, telefono, correo, tipo_seguro, fecha_pago, estado_pago, observaciones, documentos):

    if not nombre.strip():
        return False, "El nombre es obligatorio"

    if not dui.strip():
        return False, "El dui es obligatorio"

    if not telefono.strip():
        return False, "El telefono es obligatorio"

    if not correo.strip():
        return False, "El correo es obligatorio"

    if not tipo_seguro.strip():
        return False, "El tipo de seguro es obligatorio"

    if not fecha_pago.strip():
        return False, "La fecha de pago es obligatoria"

    if not estado_pago.strip():
        return False, "El estado de pago es obligatorio"

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