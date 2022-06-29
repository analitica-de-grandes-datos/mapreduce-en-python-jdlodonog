#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    v_suma  = 0
    v_cont  = 0


    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            v_suma = v_suma + val  
            v_cont =  v_cont + 1

        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_suma, v_suma/v_cont))

            curkey = key
            v_suma = val
            v_cont = 1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_suma, v_suma/v_cont))
