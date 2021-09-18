# Ejercicio 9: Pedir alto, ancho y largo de una pileta. Calcular el volumen y la cantidad de litros
# que tiene. (saber que 1000 cm3=1 litro)
alto = float (input("ingrese alto de la pileta: "))
ancho = float (input("ingrese ancho de la pileta: "))
largo = float (input("ingrese largo de la pileta: "))
metros_cubicos = (alto*ancho*largo)
centimetros_cubicos = metros_cubicos*1000000
litros = int(centimetros_cubicos/1000)
print("su pileta tiene: "+str(litros)+" litros")
