#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#! /usr/bin python3

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    total = 0

    # NOTA: las lineas de texto son recibidas como clave \tabulador 
    
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        #Nota: en esa parte es la misma clave
        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #Se acumula  los valores para la misma clave
            total += val
            
        #Si cambia la clabe se pone en cero el acumulador
        else:

            if curkey is not None:
                #Despues de que se reducen los elementos con lamismca clave se imprime el resultado en lsa salida 
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = val

    sys.stdout.write("{}\t{}\n".format(curkey, total))
