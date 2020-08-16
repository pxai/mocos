numeros = [3, 5, -4, 2, 1, 4, 0, 6, -9, 8, 3]

positivos = 0
negativos = 0
ceros = 0

for numero in numeros:
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
        ceros = ceros + 1

print("Positivos: ", positivos)
print("Negativos: ", negativos)
print("Ceros: ", ceros)
