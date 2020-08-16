import random

matriz = [([0] * 10)] * 5

print(matriz)

for i in range(len(matriz)):
    random.seed()
    for j in range(len(matriz[i])):
        matriz[i][j] = random.randint(0, 30)

print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 15:
            print("Encontrado 15 en ", i, )
