#*******************************************************************************
#EJERCICIO N° 16
#calcular la media aritmetica del vector de list

def media(list):
    counter = 0
    for i in list:
        counter += i
    return counter / len(list)
