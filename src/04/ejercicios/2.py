def calcular (valor1, valor2, op):
    if op ==  "+": return valor1 + valor2
    elif op == "-": return valor1 - valor2
    elif op == "*": return valor1 * valor2
    elif op == "/": return valor1 / valor2
    else: return "Operación desconocida"

resultado = calcular(4, 6, "*")
print(resultado)

resultado = calcular(5, 5, "-")
print(resultado)

resultado = calcular(4, 3, "@")
print(resultado)
