def retorno_mensaje(mensaje):
    return mensaje

# A. ¿Cómo hago para mostrar ese mensaje en pantalla?
# Se debe invocar a la funcion y asignarle un valor guardado en una variable.
# B. ¿Qué diferencia encuentra con el ejercicio anterior?
# La diferencia con el ejercicio anterior radica en que en este caso la funcion es reutilizable
# ya que el return nos permite utilizar la funcion si la invocamos con valores distintos.
mens = "Estudiando Fundamentos de Informática en la UNAJ"
resul = retorno_mensaje(mens)
print(resul)


mens2 = "Estudiando Matemática I en la UNAJ"
resul2 = retorno_mensaje(mens2)
print(resul2)

mens3 = "Estudiando Python en la UNAJ"
resul3 = retorno_mensaje(mens3)
print(resul3)

