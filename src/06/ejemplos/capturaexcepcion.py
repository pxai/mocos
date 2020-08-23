valor = input("Introduce un número: ")

try:
    valor = int(valor)
    cuadrado = valor * valor
    print("El cuadrado es: ", cuadrado)
except:
    print("Error al convertir dato!")
