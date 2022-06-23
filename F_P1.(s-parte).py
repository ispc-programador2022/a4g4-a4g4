#Ejercicio 10
#Función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las funciones anteriores.
#Alumno: Ancillotti Angel
#A4G4

import suma
import producto

def  ejercicio_10(a,b,c):
    sum = 0
    multi = 0

    sum = suma.suma(a,b) #llamo  a la funcion de Suma del modulo Suma y cargo en la variable sum la suma de a y b.

    multi = producto.producto( sum, c) #llamo a la funcion producto del modulo producto y multiplico el valor de la suma por la variable c

    return (multi) 

