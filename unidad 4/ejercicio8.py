# Ejercicio 8: Diseña un programa que, dado un número entero, determine si éste es el
# doble de un número impar. (Ejemplo: 14 es el doble de 7, que es impar).
# Ayuda: Defina una función que reciba como parámetro un número entero y retorne un
# valor booleano indicando si ese número es el doble de un número impar.

def doble_numero_impar (numero):
    num1 = numero/2
    if num1 % 2 == 1:
        return "su numero es el doble de un numero impar"
    elif num1 % 2 == 0:
        return "su numero es el doble de un numero par"
    else:
        return "su numero es el doble de un numero con coma"
        


num = int(input("ingrese un numero: "))
resultado = doble_numero_impar(num)
print(resultado)


