numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0 or numero % 2 != 0:
    print("Debes introducir un número par mayor que 0")
else:
    secuencia = ""
    numero = numero / 2
    while numero > 0:
        secuencia  = secuencia + "*-"
        numero = numero - 1

    secuencia = secuencia + "*"

    print(secuencia)
