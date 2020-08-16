numeros = [3, 5, -4, 2, 1, 4, 0, 6, 9, 8, 3]
repetido = False
i = 0
j = 0

while i < len(numeros) and not repetido:
    while j < len(numeros):
        if numeros[i] == numeros[j]:
            repetido = True
            break
        j = j + 1
    i = i + 1

if repetido:
    print("Hay un número repetido")
else:
    print("No hay un número repetido")
