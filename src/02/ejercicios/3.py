valor = input("Introduce un número: ")
valor = int(valor)

for i in range(11):
    print(valor,"x",i,"=",(valor*i))
    # Alternativas:
    # print("%d x %d = %d" % (valor, i, valor * i))
