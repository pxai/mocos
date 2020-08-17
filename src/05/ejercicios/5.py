import random

class Numero:
    def aleatorio (max):
      return random.randint(0, max)


Numero.aleatorio = staticmethod(Numero.aleatorio)

for i in range(5):
  print(Numero.aleatorio(10))
