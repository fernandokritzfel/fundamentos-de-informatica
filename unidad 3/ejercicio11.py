def armo_cartel(nombreproducto,precioanterior,preciorebajado):
    print("*************************************")
    print("Atención!!! Gran rebaja para el producto de "+nombreproducto)
    print("Antes: precio anterior "+str(precioanterior))
    print("Ahora: precio rebajado "+str(preciorebajado))
    print("----------------------------------------")


producto = "zapatillas"
precioa = 1200
precior = 800
mensaje = armo_cartel(producto,precioa,precior)
