#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:

        lista6 = line.split(" ")
            
        sys.stdout.write("{}\t{}\n".format(lista6[0],float(lista6[2])))
