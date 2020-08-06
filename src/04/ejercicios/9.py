def factura(productos, cantidades, precios):
    factura = "FACTURA\n-------------------\n"
    total = 0

    for i in range(len(productos)):
        factura = factura + productos[i]
        factura = factura + " x " + str(cantidades[i])
        factura = factura + " : " + str(precios[i]) + "\n"

        total = total + (cantidades[i] * precios[i])

    factura = factura + "\n-----------------------\n"
    factura = factura + "Total: " + str(total)

    return factura


# Ejemplo de llamada
totalFactura = factura(["Pan","Huevos","Harina"],[1,6,2],[1.2, 0.2, 0.8])
print(totalFactura)
