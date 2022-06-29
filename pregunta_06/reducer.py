#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    v_max  = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
    
            if val > v_max:
                v_max = val
            if val < v_min:
                v_min = val

        else:
   
            if curkey is not None:
      
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_max, v_min))

            curkey = key
            v_max = val
            v_min = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_max, v_min))
