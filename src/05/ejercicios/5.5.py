import random

class Numero:
    @staticmethod
    def aleatorio (max):
      return random.randint(0, max)

for i in range(5):
  print(Numero.aleatorio(10))
