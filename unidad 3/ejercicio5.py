

def cuantos_dias(mes):
    lista = [["enero",31],["febrero", 28],["marzo",31],["abril",30],["mayo",31],["junio",30],["julio",31],["agosto",31],["septiembre",30],["octubre",31],["noviembre",30],["diciembre",31]]
    dia = ("cantidad de dias del mes: ")+str(lista[mes-1][1])
    return dia


numero = (cuantos_dias(int(input("ingrese numero de mes: "))))
print (numero)

