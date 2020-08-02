valor = ""

while valor != 0:
    valor = input("Introduce un numero: ")
    valor = int(valor)
    if valor < 0:
        break

    for i in range(valor):
        print("Hola")
