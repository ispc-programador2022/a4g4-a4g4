#EJERCICIO N° 11
"""
 A los efectos de que funcione este bloque se entenderá que el usuario ya ha pasado 
las primeras lineas de codigo y ha definido valores para las variables val1 y val2.
 Caso contrario, si dichas variables aún no han sido definidas, el codigo presentará
errores.

def  ing2i ():
    val1 = int ( input ( "ingresar el primer valor: " ))
    val2 = int ( input ( "ingresar el segundo valor: " ))
    return val1, val2

val1, val2 = ing2i()
"""

#Función n° 11, resta de variables 1 y 2, multiplicada por 3er parametro val3
def fun11 (val1, val2):
    resta = val1 - val2
    print( f"el total de {val1} - {val2} es {resta}")
    val3 = int ( input ( "por favor, ingresar un tercer valor par multiplicar: " ))
    return resta * val3

print("el total de la función numero 11 es : ", fun11(val1, val2))

"""perdón si el Main no es el lugar indicado para subir el ejercicio, aún no termino de entender Git"""
