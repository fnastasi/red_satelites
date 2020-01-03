from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from util import *


def ejercicio1(nobmre_sat,lat,lon,nombre_guardar="", tiempo_real = False):
    

    

    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # lat_ts is the latitude of true scale.
    # resolution = 'c' means use crude resolution coastlines.
    m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
                llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
    
    
    #m.bluemarble()
    #m.shadedrelief()
    #m.etopo()
    m.drawcoastlines()
    #m.fillcontinents(color='coral',lake_color='aqua')
    #m.drawmapboundary(fill_color='aqua')
    
    plt.title("Trayectoria" + nobmre_sat)
    
    
    # draw parallels and meridians.
    #m.drawparallels(np.array([69.519]),labels=[True,True,False,False]) # -90 a 91 
    #m.drawmeridians(np.array([-127.023]),labels=[False,False,True,True]) # -180 a 181
    
    # Graficar todos los puntos al mismo tiempo
    if not tiempo_real:
        print("")#m.scatter(lon,lat,latlon=True,s = 1)
    else:
        long1 = lon[0:10000]
        lat1 = lat[0:10000]
        
        #m.scatter(lon[0:172800,0],lat[0:172800,0],latlon=True)
        #plt.show()
        """
        for idx, lon_e in enumerate(lon):
            m.scatter(lon_e,idx,latlon=True)
        plt.show()
        """
        for i in range(len(long1)):
            m.scatter(long1[i],lat1[i],latlon=True,c='b')
            plt.pause(0.00000001)

    if nombre_guardar != "":
        plt.savefig(nombre_guardar+".png",dpi = 300)
    else:
        plt.show()
        
    


if __name__ == "__main__":
    

    filename = "Satellite-LEO_0003-To-Satellite-LEO_0000 SST+access.txt"
    tiempo,lat,lon,Rasc,Dec = get_lat_lon(filename)
    ejercicio1("Satelite 0003",lat,lon)