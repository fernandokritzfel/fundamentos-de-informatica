def calculo_dosis(dias,veces,envase):
    return (dias*veces)<=envase

dias1 = int(input("ingrese cantidad de dias que debe tomar la medicacion: "))
veces1 = int(input("cantidad de veces al dia que debe tomar: "))
envase1 = int(input("cantidad por envase: "))

resultado = calculo_dosis(dias1,veces1,envase1)
print(resultado)
