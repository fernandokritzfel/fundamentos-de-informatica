# Ejercicio 12: Escribir un programa que dado un año determine si es bisiesto o no. Un
# año es bisiesto si es múltiplo de 4 (por ejemplo 1984). Los años múltiplos de 100 no son
# bisiestos, salvo si ellos son también múltiplos de 400 (2000 es bisiesto, pero 1800 no lo
# es).

def es_no_es_bisiesto(anios):
    if anios%4==0 and (anios%100!=0 or anios%400==0):
        return "es año bisiesto"
    else:
        return "no es año bisiesto"

anio1 = 1970
anio2 = 1948
anio3 = 2000

resultado = es_no_es_bisiesto(anio1)
resultado2 = es_no_es_bisiesto(anio2)
resultado3 = es_no_es_bisiesto(anio3)
print(resultado)
print(resultado2)
print(resultado3)

