def positivo (valor):
    if valor < 0:
        return -valor

    return valor


def potencia (valor1, valor2):
    resultado = valor1
    while valor2 - 1 > 0:
        resultado *= valor1
        valor2 = valor2 - 1

    return resultado

print(positivo(-1))
print(potencia(2, 3))
print(potencia(positivo(2), positivo(4)))
potencia(positivo(-5), positivo(4))
