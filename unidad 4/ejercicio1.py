# Ejercicio 1: Definir una función que permita que reciba como parámetro un número e
# imprima por pantalla si es positivo, negativo o cero. Utilice esta función para escribir un
# programa que lee un número ingresado por el usuario y muestre si es positivo, negativo o
# cero.


def determina_negativo_positivo(numero):
    if numero>0:
        return "su numero es positivo"
    elif numero==0:
        return "su numero es cero"
    else:
        return "su numero es negativo"

numero_ingresado = int(input("ingrese un numero: "))
num1 = determina_negativo_positivo(numero_ingresado)
print(num1)