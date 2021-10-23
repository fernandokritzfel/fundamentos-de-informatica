def determina_talle(largo,cuello):
    if (largo>= 15 and largo<=18) and (cuello<=18 or cuello<=19):
     return "talle 1"
    elif (largo>= 19 and largo<=22) and (cuello<=20 or cuello<=21):
        return "talle 2"
    elif (largo>= 25 and largo<=27) and (cuello<=22 or cuello<=23):
        return "talle 3"
    elif (largo>= 28 and largo<=30) and (cuello<=24 or cuello<=25):
        return "talle 4"
    elif (largo>= 31 and largo<=36) and (cuello<=26 or cuello<=29):
        return "talle 5"
    elif (largo>= 37 and largo<=45) and (cuello<=30 or cuello<=35):
        return "talle 6"
    elif (largo>= 46 and largo<=55) and (cuello<=36 or cuello<=40):
        return "talle 7"
    elif largo>= 55 and cuello>=41:
        return "talle 8"


largo_cm = int(input("ingrese largo en cm: "))
cuello_cm = int(input("ingrese cuello en cm: "))

talle_recomendado = determina_talle(largo_cm,cuello_cm)
print(talle_recomendado)