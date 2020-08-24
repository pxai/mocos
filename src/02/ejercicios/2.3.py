numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    for i in range(0, numero):
        print("Python mola!")
