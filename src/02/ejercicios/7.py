numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0 or numero % 2 != 0:
    print("Debes introducir un número par mayor que 0")
else:
    estrellas = ""
    while numero > 0:
        estrellas  = estrellas + "*"
        numero = numero - 1

    print(estrellas)
