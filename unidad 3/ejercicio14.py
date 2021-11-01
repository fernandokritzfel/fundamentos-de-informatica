# Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y
# convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y
# devuelve su conversión respectiva.

def convertir_a_dolar(montopesos):
    conversion = montopesos/197.5
    return conversion

def convertir_a_euro(montopesos):
    conversion = montopesos/233
    return conversion

def convertir_a_real(montopesos):
    conversion = montopesos/17.69
    return conversion

pesos_dolar = 2000
resultado = convertir_a_dolar(pesos_dolar)
print(str(int(resultado))+ " dolares")

pesos_euro = 2000
resultado1 = convertir_a_euro(pesos_euro)
print(str(int(resultado1))+" euros")

pesos_real = 2000
resultado2 = convertir_a_real(pesos_real)
print(str(int(resultado2))+" reales")