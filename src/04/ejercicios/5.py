def iniciarConNumero (longitud, numero):
    numeros = []
    for i in range(longitud):
        numeros.append(numero)
    return numeros

def iniciarConNumero1 (longitud, numero): return [numero] * longitud

print(iniciarConNumero(10, 3))
print(iniciarConNumero1(10, 3))
