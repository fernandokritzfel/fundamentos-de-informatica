def calculo_rebaja(previejo,prenuevo):
    resul1 = (prenuevo*100)/previejo
    resul2 = resul1-100
    return resul2

precio_viejo = 120
precio_nuevo = 80
res = calculo_rebaja(precio_viejo,precio_nuevo)
print(str(int(-res))+" %"+" de rebaja")