#EJERCICIO N° 12: generador de 50 numeros random
""" necessario para el desarrollo posterior de los ejercicios 13 a final"""

import random
list = []
def genrd ():
    for i in range(50):
        rndInt = random.randint(0,50)
        list.append(rndInt)
genrd()

#*******************************************************************************
#EJERCICIO N° 16
"""     calcular la media aritmetica del vector de list    """

def fun16():
    counter = 0
    for i in list:
        counter += i
    return counter / len(list)

print(fun16())
