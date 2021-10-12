def determina_si_son_divsibles(numero1,numero2):
    if numero1%numero2 == 0:
        return "el numero " + str(numero1)+ " es divisible por "+str(numero2)

    else:
        return "el numero " +  str(numero1)+ " NO es divisible por "+str(numero2)

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un segundo numero: "))

resultado = determina_si_son_divsibles(num1,num2)
print(resultado)
