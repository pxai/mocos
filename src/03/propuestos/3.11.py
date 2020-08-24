import random

numeros = [4, 7, -3, 7, 1, 11, 9, 0, 5, 8]

print(numeros)

for i in range(len(numeros)):
    indiceAleatorio = random.randint(0, len(numeros) - 1)
    anterior = numeros[i]
    numeros[i] = numeros[indiceAleatorio]
    numeros[indiceAleatorio] = anterior

print(numeros)
