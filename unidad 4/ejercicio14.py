def pulsaciones_cada_10_seg(anios,entrena):
    if entrena == "si":
        return (220-anios)/10
    elif entrena =="no":
        return (210-anios)/10

edad = int(input("ingrese su edad: "))
entrenamiento = input("indique si entrena o no: ")
pulsaciones = int(pulsaciones_cada_10_seg(edad,entrenamiento))
print("cantidad de pulsaciones que debe tener en 10 segundos: " +str(pulsaciones)) 