# Ejercicio 16: Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse. Mostrar
# el siguiente mensaje “La solicitud de inscripción a la comisión <comision> solicitada por el
# alumno <apellido>, <nombre> está siendo procesada”
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
n_alumno = input("ingrese su N° de alumno: ")
comision = input("ingrese numero de comision al que desea suscribirse: ")
print("La solicitud de inscripción a la comisión "+str(comision)+" solicitada por el alumno "+apellido+", "+nombre+" está siendo procesada")