#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:


        key, value = line.split('\t') 
        value =list(value.strip().split(',')) 
        key = key.zfill(4) 
        

        for letra in valor: 
            sys.stdout.write("{}\t{}\n".format(letra ,key))
