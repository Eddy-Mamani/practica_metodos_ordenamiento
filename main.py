from metodos_ord import ordenamiento_burbuja, ordenamiento_seleccion, ordenamiento_insercion, ordenamiento_quick_sort, ordenamiento_mezcla

def mostrar_menu():
    print("\n*** MENÚ DE MÉTODOS DE ORDENAMIENTO ***")
    print("1. Burbuja")
    print("2. Selección")
    print("3. Inserción")
    print("4. Quick Sort")
    print("5. Mezcla (Merge Sort)")
    print("6. Salir")

def pedir_lista():
    entrada = input("Ingrese números separados por espacios: ")
    try:
        lista = list(map(int, entrada.strip().split()))
        return lista
    except ValueError:
        print("Error: Solo ingrese números enteros separados por espacios.")
        return None

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("¡Hasta luego!")
            break

        lista = pedir_lista()
        if lista is None:
            continue

        if opcion == "1":
            resultado = ordenamiento_burbuja(lista)
        elif opcion == "2":
            resultado = ordenamiento_seleccion(lista)
        elif opcion == "3":
            resultado = ordenamiento_insercion(lista)
        elif opcion == "4":
            resultado = ordenamiento_quick_sort(lista)
        elif opcion == "5":
            resultado = ordenamiento_mezcla(lista)
        else:
            print("Opción inválida, intente de nuevo.")
            continue

        print("Lista ordenada:", resultado)

if __name__ == "__main__":
    main()
