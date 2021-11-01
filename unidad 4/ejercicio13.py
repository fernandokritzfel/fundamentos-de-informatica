# Ejercicio 13: Dado la duración (en segundos) de una llamada telefónica, calcular su
# costo, de la siguiente manera: El primer minuto $1,10, luego $0,25 cada fracción de 15
# segundos (un cuarto de minuto). Resuélvalo utilizando funciones.

def costo_llamada(duracion):
    if duracion<=60:
        return "$ 1.10"
    elif duracion>60:
        return ((duracion-60)/15) * 0.25 + 1.10

costo = int(input("ingrese duracion de la llamada en segundos: "))
resul = costo_llamada(costo)
print(resul)
