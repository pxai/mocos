numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    factorial = numero
    while numero > 1:
        numero = numero - 1
        factorial = factorial * numero

    print("Resultado: ", factorial)
