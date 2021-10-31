def determina_si_son_divsibles(numero1):
    if numero1%6 == 0:
        return "el numero es divisible por 6"

    else:
        return "el numero no es divisible por 6"

num1 = int(input("ingrese un numero: "))
resultado = determina_si_son_divsibles(num1)
print(resultado)
