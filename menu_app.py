def agregar_compra(compras, total_gastado):

    nombre_producto = input("Ingresa el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        compras.append((nombre_producto, precio))
        total_gastado += precio
        print("Compra agregada correctamente.")
    except ValueError:
        print("Error: Ingrese un valor numerico valido para el precio.")


def mostrar_compra(compras):
    if not compras:
        print("\nNo hay compras registradas.")
    else:
        print("\n2Lista de compras: ")
        for i, (producto, precio) in enumerate(compras, 1):
            print(f"{i}, {producto}: ${precio: .2f}")


def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado: .2f}")


def main():
    compras = []
    total_gastado = 0
    while True:
        print("\nMenu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("\nSelecciona una opcion: ")
        if opcion == "1":
            agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compra(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            break
        else:
            print("\nOpcion no valida. Eliga una opcion valida.")


main()