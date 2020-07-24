numero = input("Introduce un número: ")
numero = int(numero)

if numero >= 0 and numero % 2 == 0:
    print(numero, " es par y positivo")
elif numero < 0 and numero % 2 != 0:
    print(numero, " es impar y negativo")
elif numero < 0:
    print(numero, " es negativo")
else:
    print(numero, " es impar")
