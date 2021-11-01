def calculo_transporte(sala1,sala2,sala3,asientos):
    micros = (sala1+sala2+sala3)/asientos
    return micros

adultos = 3
primer_sala = 80 + adultos
segunda_sala = 85 + adultos
tercer_sala = 98 + adultos
asientos1 = 60
micro = calculo_transporte(primer_sala,segunda_sala,tercer_sala,asientos1)
print(int(micro+1))
print(tercer_sala)
