numero = input("Introduce un número: ")
numero = int(numero)

if numero >= 0:
    print(numero, " es positivo")
else:
    print(numero, " es negativo")

numero = -numero

print("Conversión: ", numero)
