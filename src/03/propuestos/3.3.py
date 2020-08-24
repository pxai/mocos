frase = ""
palabra = ""

while palabra != ".":
    palabra = input("Escribe una palabra: ")

    if palabra != "." or palabra != "":
        frase = frase + " " + palabra

print("Frase creada:", frase)
