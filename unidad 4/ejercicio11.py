# Ejercicio 11: Diseñar una función que dado un carácter imprima en pantalla si es una
# letra, un dígito, un carácter especial u otro tipo de carácter. Muestre su uso en un
# programa.
# Ayuda: utilice las funciones definidas en el ejercicio 9. Además, defina las funciones
# necesarias con sus respectivos parámetros, para poder determinar los otros casos.

def es_letra(caracter):
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    numero = ["1","2","3","4","5","6","7","8","9","0"]
    caracterespecial = [".",",","!","?","$","/","(",")"]
    if caracter in letras:
        return "su caracter es una letra"
    elif caracter in numero:
        return "su caracter es un numero"
    elif caracter in caracterespecial:
        return "su caracter es un signo"
    else:
        return "su caracter es de otro tipo"

caracter_ingresado = input("ingrese un caracter: ")
resultado = es_letra(caracter_ingresado)
print(resultado)
