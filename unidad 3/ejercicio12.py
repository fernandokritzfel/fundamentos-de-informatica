def calculo_litros(largo,ancho,profundidad):
    metros_cubicos = largo*ancho*profundidad
    litros = metros_cubicos*1000
    return litros


larg = 7
anch = 5
prof = 2
lit = calculo_litros(larg,anch,prof)
print(str(lit)+" litros")
