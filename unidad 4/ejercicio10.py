# Ejercicio 10: Dadas 3 longitudes, decir mediante un mensaje si se forma o no un
# triángulo (cada lado tiene que ser menor que la suma de los otros dos). Escriba una
# función que recibe 3 parámetros para resolver el problema. Invoque la función en un
# programa.

def forma_triangulo(lado1,lado2,lado3):
    if lado1<(lado2+lado3) and lado2<(lado1+lado3) and lado3<(lado1+lado2) :
        return "se puede formar un triangulo"
    else:
        return "no se puede formar un triangulo"


ladoA = 40
ladoB = 30
ladoC = 20
resolucion = forma_triangulo(ladoA,ladoB,ladoC)
print(resolucion)

