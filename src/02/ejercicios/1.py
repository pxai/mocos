numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    while numero > 0:
        print("Hola!")
        numero = numero - 1
