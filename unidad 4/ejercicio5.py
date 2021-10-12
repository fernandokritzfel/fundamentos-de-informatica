def transporte_adecuado(cant_pasajeros):
    if cant_pasajeros<=0:
        return " ERROR! la cantidad debe ser mayor a 0."
    elif cant_pasajeros==1:
        return lista[0]
    elif cant_pasajeros==2:
        return lista[1]
    elif cant_pasajeros>2 and cant_pasajeros<=4:
        return lista[2]
    elif cant_pasajeros>4 and cant_pasajeros<=12:
        return lista[3]
    elif cant_pasajeros>12 and cant_pasajeros<=40:
        return lista[4]
    elif cant_pasajeros>40 and cant_pasajeros<=200:
        return lista[5]
    elif cant_pasajeros>200:
        return "Debe buscar un vehiculo alternativo."


lista = ["Hoverboard o Monopatin electrico ","Bicicleta o moto","Auto","Camioneta","Colectivo ","Avión"]

cantidad_pasajeros = int(input("ingrese cantidad de pasajeros: "))
resultado = transporte_adecuado(cantidad_pasajeros)
print("el vehiculo apropiado es: "+ str(resultado))

