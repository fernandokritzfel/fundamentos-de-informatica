def letra_mayus_minus(letraingresada):
    letrasmayus = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    letrasminus = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    if letraingresada in letrasmayus:
        return "la letra ingresada es MAYUSCULA"
    elif letraingresada in letrasminus:
        return "la letra ingresada es MINUSCULA"
    else:
        return ""

letra1 = input("ingrese una letra: ")
resultado = letra_mayus_minus(letra1)

print(resultado)