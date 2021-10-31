# defino la funcion que determina la cantidad de pulsaciones
def pulsaciones_cada_10_seg(anios,entrena):
    if entrena == "si":
        return (220-anios)/10
    elif entrena =="no":
        return (210-anios)/10
# solicito en dos variables los datos por teclado
edad = int(input("ingrese su edad: "))
entrenamiento = input("indique si entrena o no: ")

# defino la variable que llamara a la funcion con los datos ingresados
pulsaciones = int(pulsaciones_cada_10_seg(edad,entrenamiento))

# imprimo el el resultado
print("cantidad de pulsaciones que debe tener en 10 segundos: " +str(pulsaciones)) 