import random

def aleatorio (max):
    return random.randint(0, max - 1)


def generarNombre (silabas):
    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
    nombre = ""

    for i in range(silabas):
        consonante = consonantes[aleatorio(len(consonantes))]
        vocal = vocales[aleatorio(len(vocales))]
        nombre = nombre + consonante + vocal

    return nombre


print(generarNombre(3))
