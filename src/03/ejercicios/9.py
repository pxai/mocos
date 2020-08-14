frase = input("Escribe una frase: ")
palabra = input("Escribe una palabra de esa frase: ")

posicion = frase.index(palabra)

if posicion != -1:
    inicio = frase[0:posicion]
    final = frase[posicion + len(palabra):len(frase)]
    resultado = f"{inicio}{palabra.upper()}{final}"

    print(resultado)
else:
    print(palabra, "no está en la frase.")
