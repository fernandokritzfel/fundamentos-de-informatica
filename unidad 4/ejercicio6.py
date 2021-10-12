def indica_anios(anionacimiento):
    anios =2021-anionacimiento
    return anios

def indica_grupo_segun_edad(anios):
    if anios<2:
        return "bebe"
    elif anios>=2 and anios<=12:
        return "menor"
    elif anios>12 and anios <=18:
        return "adolescente"
    elif anios>18 and anios <=75:
        return "adulto"
    elif anios>75:
        return "adulto mayor"


edad = int(input("ingrese año de nacimiento: "))
edad1 = indica_anios(edad)
# print(edad1)
grupo = indica_grupo_segun_edad(edad1)
print ("la persona es un "+str(grupo))
