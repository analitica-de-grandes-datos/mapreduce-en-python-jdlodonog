#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# reduce  elementos con la misma clave
#
if __name__ == "__main__":
    contador = 0

    for line in sys.stdin:

        lista9 = line.split('   ')

        sys.stdout.write("{}   {}   {}\n".format(lista9[1], lista9[2].strip(), int(lista9[0]))) 
        if contador >= 5: 
            break 
        contador += 1
