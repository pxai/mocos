numeros = [3, 5, -4, 2, 1, 4, 0, 6, 9, 8, 3]

for numero in numeros:
    print(numero)

for i in range(len(numeros)):
    numeros[i] = numeros[i] + 1

for numero in numeros:
    print(numero)


# Alternativa para la suma:
# numerosIncrementados = numeros.map( numero => numero + 1 )
