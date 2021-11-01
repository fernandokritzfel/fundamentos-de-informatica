def calculo_nuevo_precio(precioviejo,porcentajeAum):
    precionuevo = ( precioviejo + (porcentajeAum*(precioviejo/100)))
    return precionuevo


preciov = 50
porcen = 30
resul = calculo_nuevo_precio(preciov,porcen)
print (str(int(resul))+" es el precio nuevo")
