# Ejercicio 18: Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una
# clave con esos datos (su clave seria sus iniciales seguido de un guión bajo y de su año de
# nacimiento) y mostrarla.

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
fecha = input("ingrese fecha de nacimiento: ")
print("su contraseña es: "+nombre[0]+apellido[0]+"_"+fecha[-4:])