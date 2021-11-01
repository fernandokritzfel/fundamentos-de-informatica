# Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un
# producto dado su precio de venta sin IVA.

def precio_con_iva(precioneto):
    bruto = precioneto*1.21
    return bruto

precio = 500
resultado = precio_con_iva(precio)
print(resultado)
