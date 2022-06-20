#EJERCICIO N° 12
#genera 50 numeros random

import random
list = []
def genrd ():
    for i in range(50):
        rndInt = random.randint(0,50)
        list.append(rndInt)
    return list
