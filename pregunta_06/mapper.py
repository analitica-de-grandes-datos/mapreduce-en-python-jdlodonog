#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
        lista = line.split("   ")
            
            #
            # escribe al flujo estandar de salida
            #
        sys.stdout.write("{}\t{}\n".format(lista[0],float(lista[2])))
