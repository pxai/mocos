numero = input("Introduce un número: ")
numero = int(numero)

if numero <= 0:
    print("Debes introducir un número mayor que 0")
else:
    estrellas = "\n"
    for i in range(numero):
        for j in range(numero):
            estrellas = estrellas + "*"
            
        estrellas = estrellas + "\n"

    print(estrellas)
