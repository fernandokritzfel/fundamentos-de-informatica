def dia_semana(diasem):
    if diasem>=1 and diasem<=7:
        listasem = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
        return listasem[diasem-1]
    else:
        return "Numero incorrecto, recuerde elegir un numero del 1 al 7"

dia_de_la_semana = int(input("ingrese un numero (1 a 7): "))
resultado = dia_semana(dia_de_la_semana)
print(resultado)