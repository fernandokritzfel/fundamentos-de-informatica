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