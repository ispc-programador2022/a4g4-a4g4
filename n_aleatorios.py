#Ejercicio N°12
#Función genrnd que retorna una lista con 50 números aleatorios.
#Alumno: Ancillotti Angel
#Grupo: A4G4


import random
lista = []
fin = 50
for i in range (1, fin+1):
        lista.append(random.randint(1,50))
        aleatorios = list(dict.fromkeys(lista))

print("lista",aleatorios)        
