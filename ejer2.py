import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import fileinput

import satelite
import planisferioRed




def ejercicio2(n_fil=2,n_col=2):
    
    # Red de IP
    fil = 2
    col = 2
    IP_vec = np.array(["192.168.255.0", "192.168.255.1",
                       "192.168.255.2", "192.168.255.3", 
                       ])

    p = planisferioRed.planisferioRed(fil,col,IP_vec)

    # Creación de un satelite
    sat = satelite.satelite("satelite_0003")
    
    for line in fileinput.input("test.txt", inplace=True):
        try:
            l = line.lstrip()
            valores =  np.array(line.split()).astype(float)
            if valores.size != 0: # Cuando lees una línea vacía (o una línea lleno de espacios en blanco)
                sat.coord_lat = valores[1]
                sat.coord_lon = valores[2]
                cuad = p.get_cuad(sat.coord_lon,sat.coord_lat)
                line = line[0:-1] + "                     " + p.IP_map[cuad]
            else:
                line = line[0:-1]
        except:
            pass
        finally:
            print(line)
    """ 
    with open("test.txt", 'r+') as f:
        
        for line in fileinput.input("test.txt", inplace=True):
            try:
                line
                print('{} {}'.format(fileinput.filelineno(), line), end='') # for Python 3
        
        
        
        line = f.readline()
        while line:
            try: # Para cuando lees una línea con letras
                
                line = line.lstrip()
                valores =  np.array(line.split()).astype(float)
                print(valores)
                if valores.size != 0: # Cuando lees una línea vacía (o una línea lleno de espacios en blanco)
                    
                    sat.coord_lat = valores[1]
                    sat.coord_lon = valores[2]
                    cuad = p.get_cuad(sat.coord_lon,sat.coord_lat)
                    line_aux = line + p.IP_map[cuad]
                    print(line_aux)
                    print(N)
                    f.seek(N)
                    f.write(line_aux)
                    
            except:
                print("Hola")
                pass
            finally:
                N = N + len(line) +1 
                line = f.readline()
    """
        
    #for line in fileinput.input("test.txt", inplace=1):
    #    s = line.readline()
    #    print(s)


if __name__ == "__main__":
    ejercicio2()
    
    
    

    #print('{} {}'.format(fileinput.filelineno(), line), end='') # for Python 3
    # print "%d: %s" % (fileinput.filelineno(), line), # for Python 2