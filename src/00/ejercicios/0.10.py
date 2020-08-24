valor = input("Introduce un número: ")
valor = int(valor)

positivoYPar = (valor >= 0) and (valor % 2 == 0)
resultado = not positivoYPar
print("¿Es par y positivo?", resultado)
