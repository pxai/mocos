def unir(*palabras):
    frase = ""

    for palabra in palabras:
        frase = frase + " " + palabra
    
    return frase


print(unir("Hola", "qué", "tal"))