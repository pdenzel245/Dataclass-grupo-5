from datos import clientes, servicios, sistemas, amenazas, empleados

from entidades import (
    crear_cliente,
    crear_servicio,
    crear_sistema,
    crear_amenaza,
    crear_empleado
)


# =========================
# CLIENTES
# =========================

def registrar_cliente():

    print("\n--- REGISTRAR CLIENTE ---")

    id_cliente = input("Ingrese el ID: ")
    nombre = input("Ingrese el nombre: ")
    empresa = input("Ingrese la empresa: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo: ")

    cliente = crear_cliente(
        id_cliente,
        nombre,
        empresa,
        telefono,
        correo
    )

    clientes.append(cliente)

    print("Cliente registrado correctamente ✅")


def mostrar_clientes():

    print("\n--- LISTA DE CLIENTES ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print(cliente)


# =========================
# SERVICIOS
# =========================

def registrar_servicio():

    print("\n--- REGISTRAR SERVICIO ---")

    id_servicio = input("Ingrese el ID: ")
    nombre = input("Ingrese el nombre: ")
    descripcion = input("Ingrese la descripción: ")
    precio = input("Ingrese el precio: ")

    servicio = crear_servicio(
        id_servicio,
        nombre,
        descripcion,
        precio
    )

    servicios.append(servicio)

    print("Servicio registrado correctamente ✅")


def mostrar_servicios():

    print("\n--- LISTA DE SERVICIOS ---")

    if len(servicios) == 0:
        print("No hay servicios registrados.")
    else:
        for servicio in servicios:
            print(servicio)


# =========================
# SISTEMAS
# =========================

def registrar_sistema():

    print("\n--- REGISTRAR SISTEMA ---")

    id_sistema = input("Ingrese el ID: ")
    nombre = input("Ingrese el nombre: ")
    tipo = input("Ingrese el tipo: ")
    estado = input("Ingrese el estado de seguridad: ")

    sistema = crear_sistema(
        id_sistema,
        nombre,
        tipo,
        estado
    )

    sistemas.append(sistema)

    print("Sistema registrado correctamente ✅")


def mostrar_sistemas():

    print("\n--- LISTA DE SISTEMAS ---")

    if len(sistemas) == 0:
        print("No hay sistemas registrados.")
    else:
        for sistema in sistemas:
            print(sistema)


# =========================
# AMENAZAS
# =========================

def registrar_amenaza():

    print("\n--- REGISTRAR AMENAZA ---")

    id_amenaza = input("Ingrese el ID: ")
    nombre = input("Ingrese el nombre de la amenaza: ")
    riesgo = input("Ingrese el nivel de riesgo: ")
    descripcion = input("Ingrese la descripción: ")

    amenaza = crear_amenaza(
        id_amenaza,
        nombre,
        riesgo,
        descripcion
    )

    amenazas.append(amenaza)

    print("Amenaza registrada correctamente ⚠️")


def mostrar_amenazas():

    print("\n--- LISTA DE AMENAZAS ---")

    if len(amenazas) == 0:
        print("No hay amenazas registradas.")
    else:
        for amenaza in amenazas:
            print(amenaza)


# =========================
# EMPLEADOS
# =========================

def registrar_empleado():

    print("\n--- REGISTRAR EMPLEADO ---")

    id_empleado = input("Ingrese el ID: ")
    nombre = input("Ingrese el nombre: ")
    cargo = input("Ingrese el cargo: ")
    telefono = input("Ingrese el teléfono: ")

    empleado = crear_empleado(
        id_empleado,
        nombre,
        cargo,
        telefono
    )

    empleados.append(empleado)

    print("Empleado registrado correctamente 👨‍💻")


def mostrar_empleados():

    print("\n--- LISTA DE EMPLEADOS ---")

    if len(empleados) == 0:
        print("No hay empleados registrados.")
    else:
        for empleado in empleados:
            print(empleado)
