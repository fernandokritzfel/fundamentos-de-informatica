def a_pagar(cantper,gastobebida,gastocomida,alquiler):
    division = (gastobebida + gastocomida + alquiler)/cantper
    return division


personas = 5
gasto_bebida = 5000
gasto_comida = 7000
alquiler1 = 10000
dinero_por_persona = a_pagar(personas,gasto_bebida,gasto_comida,alquiler1)
print (dinero_por_persona)
