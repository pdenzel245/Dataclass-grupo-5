from funciones import (
    registrar_cliente,
    mostrar_clientes,
    registrar_servicio,
    mostrar_servicios,
    registrar_sistema,
    mostrar_sistemas,
    registrar_amenaza,
    mostrar_amenazas,
    registrar_empleado,
    mostrar_empleados
)


def menu():

    while True:

        print("\n==============================")
        print("    SISTEMA NICASHIELD 🛡️")
        print("==============================")

        print("1. Registrar cliente")
        print("2. Mostrar clientes")

        print("3. Registrar servicio")
        print("4. Mostrar servicios")

        print("5. Registrar sistema")
        print("6. Mostrar sistemas")

        print("7. Registrar amenaza")
        print("8. Mostrar amenazas")

        print("9. Registrar empleado")
        print("10. Mostrar empleados")

        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")


        if opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            mostrar_clientes()

        elif opcion == "3":
            registrar_servicio()

        elif opcion == "4":
            mostrar_servicios()

        elif opcion == "5":
            registrar_sistema()

        elif opcion == "6":
            mostrar_sistemas()

        elif opcion == "7":
            registrar_amenaza()

        elif opcion == "8":
            mostrar_amenazas()

        elif opcion == "9":
            registrar_empleado()

        elif opcion == "10":
            mostrar_empleados()

        elif opcion == "0":
            print("\nGracias por usar NICASHIELD ")
            break

        else:
            print("\nOpción no válida ")


menu()
