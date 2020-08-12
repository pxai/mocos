import random

def aleatorio (max):
    return random.randint(0, max)


class Moneda:
    def tirar (self):
        lados = ["cara", "cruz"]
        numero =  aleatorio(2)

        return lados[numero]



moneda = Moneda()

for i in range(10):
    print(moneda.tirar())
