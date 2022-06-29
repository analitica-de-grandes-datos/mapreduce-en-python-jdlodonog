#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    v_aux  = 0

    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        if key == curkey:

            if val > v_aux:
                v_aux = val
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey, v_aux))

           # curkey = key
           # v_aux = val

    sys.stdout.write("{}\t{}\n".format(curkey, v_aux))
