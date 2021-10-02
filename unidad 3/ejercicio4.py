def imprimo_fecha(dia,mes,anio):
    return dia+" de "+mes+" de "+anio

fecha_dia = input("ingrese un dia: ")
fecha_mes = input("ingrese un mes: ")
fecha_anio = input("ingrese un año: ")

fecha = imprimo_fecha(fecha_dia,fecha_mes,fecha_anio)
print (fecha)