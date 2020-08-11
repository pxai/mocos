numeros = []
opcion = -1

while opcion != "4":
    print("Elige opción")
    print("1. Meter elemento.")
    print("2. Sacar elemento.")
    print("3. Mostrar array.")
    print("4. Salir.")
    opcion = input("Elige opción: ")

    if "1":
        numeros.append(0)
    elif "2":
        numeros.pop()
    elif "3":
        print(numeros)
    elif "4":
        print("Hasta otra")
    else:
        print("Opción desconocida")
