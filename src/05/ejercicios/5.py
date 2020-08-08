import random

class Numero:
    def aleatorio (max):
      return random.randint(max)


Numero.aleatorio = staticmethod(Numero.aleatorio)

for in range(5):
  print(Numero.aleatorio(10))
