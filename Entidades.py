def crear_cliente(id_cliente, nombre, empresa, telefono, correo):

    cliente = {
        "ID": id_cliente,
        "Nombre": nombre,
        "Empresa": empresa,
        "Telefono": telefono,
        "Correo": correo
    }

    return cliente


def crear_servicio(id_servicio, nombre, descripcion, precio):

    servicio = {
        "ID": id_servicio,
        "Nombre": nombre,
        "Descripcion": descripcion,
        "Precio": precio
    }

    return servicio


def crear_sistema(id_sistema, nombre, tipo, estado):

    sistema = {
        "ID": id_sistema,
        "Nombre": nombre,
        "Tipo": tipo,
        "Estado": estado
    }

    return sistema


def crear_amenaza(id_amenaza, nombre, riesgo, descripcion):

    amenaza = {
        "ID": id_amenaza,
        "Nombre": nombre,
        "Riesgo": riesgo,
        "Descripcion": descripcion
    }

    return amenaza


def crear_empleado(id_empleado, nombre, cargo, telefono):

    empleado = {
        "ID": id_empleado,
        "Nombre": nombre,
        "Cargo": cargo,
        "Telefono": telefono
    }

    return empleado
