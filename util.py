from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




def get_lat_lon(filename,_skiprows=6,_skipfooter=11):

    """
    Código para parsear longitud y latitud de un archivo .txt
    """

    data_df = pd.read_csv(filename,delim_whitespace =True,skiprows = _skiprows,error_bad_lines = False, skipfooter = _skipfooter, engine = 'python')
    data_df = data_df.apply(pd.to_numeric, errors='coerce')
    data_df = data_df.dropna()
    data = data_df.values
    N = data.shape[0]
    tiempo = data[:,0].reshape(N,1)
    lat = data[:,1].reshape(N,1)
    lon = data[:,2].reshape(N,1)
    Rasc = data[:,3].reshape(N,1)
    Dec = data[:,4].reshape(N,1)

    return (tiempo,lat,lon,Rasc,Dec)
