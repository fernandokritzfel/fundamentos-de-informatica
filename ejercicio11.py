# Ejercicio 11: Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar
# cuánto se gasta por cada producto y el total

producto1 = input("ingrese 1er producto comprado: ")
cant1 = int(input("ingrese cantidad de unidades: "))
precio_unitario1 =float(input("ingrese precio por unidad: "))

producto2 = input("ingrese 2do producto comprado: ")
cant2 =int(input("ingrese cantidad de unidades: "))
precio_unitario2 =float(input("ingrese precio por unidad: "))

producto3 = input("ingrese 3er producto comprado: ")
cant3 =int(input("ingrese cantidad de unidades: "))
precio_unitario3 =float(input("ingrese precio por unidad: "))

producto4 = input("ingrese 4to producto comprado: ")
cant4 =int(input("ingrese cantidad de unidades: "))
precio_unitario4 =float (input("ingrese precio por unidad: "))

subtotal_producto1 = cant1*precio_unitario1
subtotal_producto2 = cant2*precio_unitario2
subtotal_producto3 = cant3*precio_unitario3
subtotal_producto4 = cant4*precio_unitario4

print("cantidad gastada en: "+ producto1 +"$ "+ str(subtotal_producto1))
print("cantidad gastada en: "+ producto2 +"$ "+ str(subtotal_producto2))
print("cantidad gastada en: "+ producto3 +"$ "+ str(subtotal_producto3))
print("cantidad gastada en: "+ producto4 +"$ "+ str(subtotal_producto4))

total = subtotal_producto1+subtotal_producto2+subtotal_producto3+subtotal_producto4

print("total: $"+str(total))