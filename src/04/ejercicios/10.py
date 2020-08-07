import random

def aleatorio (max):
    return random.randint(0, max)

def generarAtributos (nivelCompensacion):
    darPuntosA = 0
    inteligencia = 0
    fuerza = 0
    velocidad = 0

    puntosRestantes = 20
    puntos = 0

    while puntosRestantes > 0:
        if nivelCompensacion > puntosRestantes:
            puntos = puntosRestantes
            puntosRestantes = 0
        else:
            puntos = aleatorio(nivelCompensacion+1)
            puntosRestantes = puntosRestantes - puntos

        darPuntosA = aleatorio(3)

        if darPuntosA == 0:
            inteligencia = inteligencia + puntos
        elif darPuntosA == 1:
            fuerza = fuerza + puntos
        elif darPuntosA == 2:
            velocidad = velocidad + puntos

    print("\nValores asignados por compensación: ", nivelCompensacion)
    print("Inteligencia: ", inteligencia)
    print("Fuerza: ", fuerza)
    print("Velocidad: ", velocidad)


generarAtributos(3)
