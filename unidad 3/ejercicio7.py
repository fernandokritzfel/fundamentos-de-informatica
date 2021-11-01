def calcula_area_circulo(radio):
    return 3.14*(radio**2)

def calcula_area_rectangulo(base,altura):
    return base*altura

def calcula_area_triangulo(base1,altura1):
    return (base1*altura1)/2

rad = 6
resul = calcula_area_circulo(rad)
print(resul)

bas = 5
alt = 10
res = calcula_area_rectangulo(bas,alt)
print (res)

bas1 = 6
alt1 = 8
res1 = calcula_area_triangulo(bas1,alt1)
print(res1)


