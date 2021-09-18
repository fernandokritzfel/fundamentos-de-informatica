# Ejercicio 20:Ejecutar los siguientes códigos. ¿Cuál es el resultado de las siguientes ejecuciones?.
# Justificar
# a) tupla=(1,True,['a','b','c'], "hola")
# tupla[1]=False
# b) tupla=(1,True,['a','b','c'], "hola")
# tupla[2][0]='b'

tupla=(1,True,['a','b','c'], "hola")
tupla[2][0]='b'
# b) es posible modificar datos de listas, [2] indica que es la 2da posicion dentro de la tupla, [0] es la posicion del # elemento a modificar


tupla=(1,True,['a','b','c'], "hola")
tupla[1]=False

# a) TypeError: 'tuple' object does not support item assignment
# No es posible modificar elementos de las tuplas ya que son inmutables




