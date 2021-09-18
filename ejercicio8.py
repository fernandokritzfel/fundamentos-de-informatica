# Ejercicio 8: Pedir 2 números y mostrar la división entre ellos y el resto.

numero1 = float(input("ingrese el 1er numero: "))
numero2 = float(input("ingrese el 2do numero: "))
resultado = numero1//numero2
resto = numero1%numero2
print("la division entre ambos es: "+ str(resultado) + " y el resto: "+str(resto))