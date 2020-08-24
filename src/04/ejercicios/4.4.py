def positivo (valor):
    if valor < 0:
        return -valor

    return valor


def potencia (valor1, valor2):
    return valor1 ** valor2

print(positivo(-1))
print(potencia(2, 3))
print(potencia(positivo(2), positivo(4)))
potencia(positivo(-5), positivo(4))
