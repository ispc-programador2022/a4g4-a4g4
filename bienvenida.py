import time
from suma import suma
from potencia import potencia
from ing2i import ing2i
from media import media
from genrd import genrd
from p11 import fun11 as p3
from radicacion import radicacion
from producto import producto

lista_cargada = False

def bienvenida():
    ultimaOpcionValida = 31
    var1, var2 = ing2i()
    while True:
        printMenu()
        opcion = int(input('Ingrese la operacion que desee realizar: '))
        if opcion == 0:
            break        
        if opcion == 1:        
            print(suma(var1, var2))
        elif opcion == 2:
            print('resta(var1, var2)')
        elif opcion == 3:
            print("El producto entre", var1, "y", var2, "es:", producto(var1, var2))
        elif opcion == 4:
            print('cociente(var1, var2)')
        elif opcion == 5:
            print('modulo(var1, var2)')
        elif opcion == 6:
            print(potencia(var1,var2))
        elif opcion == 7:
            print(radicacion(var1, var2))
        elif opcion == 9:
            print('p1(var1, var2)')
        elif opcion == 10:
            print('p2(var1, var2)')
        elif opcion == 11:
            print(p3(var1, var2))
        elif opcion == 12:
            list = genrd()
            lista_cargada = True
        elif opcion == 16:
            print(media(list))

            start = time.time()
        else:
            print('no esta dentro de las opciones')
            
    
def printMenu():
    print("")
    print('Esta aplicacion pertenece al aula 4 grupo 4,vamos a desarrollar diferentes funciones con lo aprendido')
    print("1.  Función paara sumar")
    print("2.  Función para restar")
    print("3.  Función para multiplicar")
    print("4.  Función para dividir")
    print("5.  Función para calcular el módulo")
    print("6.  Función Para hacer la potencia del 1er valor elevado al 2do valor")
    print("7.  Función para calcular la raíz enésima(segundo valor) del primer valor")
    print("9.  Para ejecutar la operación de producto y suma con tercer parametro")
    print("10. Para ejecutar la operación de suma y producto con tercer parametro")
    print("11. Para ejecutar la operación de resta y multiplicación con tercer parametro")
    print("12. Generar lista con 50 números aleatorios")
    print("13. ")
    print("12. ")
    print("0. Salir")
    

if __name__ == '__main__':
    bienvenida()
