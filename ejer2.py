import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import fileinput

import satelite
import planisferioRed




def ejercicio2(n_fil=2,n_col=2):
    
    # Red de IP
    #fil = 2
    #col = 2
    IP_vec = np.array(["192.168.255.0", "192.168.255.1",
                       "192.168.255.2", "192.168.255.3", 
                       ])

    p = planisferioRed.planisferioRed(n_fil,n_col,IP_vec)

    # Creación de un satelite
    sat = satelite.satelite("satelite_0003")
    
    
    filename = "test.txt"
    for line in fileinput.input(filename, inplace=True): # Recorro cada línea del archivo
        try:
            valores =  np.array(line.split()).astype(float) # Parseo los valores
            if valores.size != 0: # Cuando no lees una línea vacía (o una línea lleno de espacios en blanco)
                sat.coord_lat = valores[1] # actualizo coordenadas del satélite
                sat.coord_lon = valores[2]
                cuad = p.get_cuad(sat.coord_lon,sat.coord_lat) #obtengo en que parte de la celda se encuentra el satélite
                line = line[0:-1] + "                     " + p.IP_map[cuad] # Agrego a la línea la IP correspondiente
            else:
                line = line[0:-1] # Si estaba vacía, dejo la línea igual (el '\n' lo pone print)
        except:
            line = line[0:-1] # Si no pudo convertir a float, no hace nada
        finally:
            print(line) # imprime la línea en el archivo
    
    #for line in fileinput.input("test.txt", inplace=1):
    #    s = line.readline()
    #    print(s)


if __name__ == "__main__":
    ejercicio2()