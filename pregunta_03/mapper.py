#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:

        lista1 = line.split(",")
  
        sys.stdout.write("{},{}\n".format(lista1[1].strip(),lista1[0]))
