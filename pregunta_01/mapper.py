#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python3
# Se define una funcion que mapea la entrada de las parejas clave valor 
#
import sys
if __name__ == "__main__":

    #
    # Luego  se itera sobre cada linea de codigo recibida a traves del flujo de entrada
    for line in sys.stdin:
        # genera las tuplas palabra \tabulador 1 en el conteo de palabras
        lista = line.split(",")
            
            
        # se escribe el en salida 
            
        sys.stdout.write("{}\t1\n".format(lista[2]))
