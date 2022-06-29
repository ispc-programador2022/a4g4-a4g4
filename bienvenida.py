from suma import suma
from potencia import potencia
from ing2i import ing2i
from media import media
from genrd import genrd
from p11 import p11 as p3
from radicacion import radicacion


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
        elif opcion == 6:
            print(potencia(var1,var2))
        elif opcion == 7:
            print(radicacion(var1, var2))
        elif opcion == 11:
            print(p3)
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
    print("6. Para hacer la potencia del 1er valor elevado al 2do valor")
    print("7. Para hacer la raiz del 1er valor respecto del 2do valor")
    print("11. Para ejecutar la operación de resta y multiplicación con tercer parametro")
    print("16. para calcular la media")
    print("0. Salir")
    

if __name__ == '__main__':
    bienvenida()
