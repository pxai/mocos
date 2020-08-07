numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    divisible = False
    original = numero
    numero = numero - 1

    while numero > 1 and not divisible:
        if original % numero == 0:
            divisible = True

        numero = numero - 1


    if not divisible:
        print(original, " es primo.")
    else:
        print(original, " NO es primo.")
