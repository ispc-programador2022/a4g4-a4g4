from suma import suma
from ing2i import ing2i
from media import media
from genrd import genrd


def bienvenida():
    ultimaOpcionValida = 31
    while True:
        printMenu()
        opcion = int(input('Ingrese la operacion que desee realizar: '))
        if opcion == 0:
            break
        if opcion >0 or opcion <= ultimaOpcionValida:
            var1, var2 = ing2i()
        
        if opcion == 1:        
            print(suma(var1, var2))
        elif opcion == 2:
            print('resta(var1, var2)')
        elif opcion == 16:
            list = genrd()
            print(media(list))
        else:
            print('no esta dentro de las opciones')
            
    
def printMenu():
    print("")
    print('Esta aplicacion pertenece al aula 4 grupo 4,vamos a desarrollar diferentes funciones con lo aprendido')
    print("1. Para Sumar")
    print("2. para restar")
    print("3. para calcular la media")
    print("0. Salir")
    

if __name__ == '__main__':
    bienvenida()
