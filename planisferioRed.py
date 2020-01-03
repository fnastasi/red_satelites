import numpy as np


class  planisferioRed():

    latitud_ini = -80
    latitud_fin = 80
    longitud_ini = -180
    longitud_fin = 180

    def __init__(self, _n_fil, _n_col,_IP_vec):

        if len(_IP_vec) != _n_col * _n_fil:
            raise Exception('Cantitdad de IPs no coincide con grilla' )

        self.n_fil =  _n_fil
        self.n_col =  _n_col
        self.latitudes = np.linspace(self.latitud_ini, self.latitud_fin, self.n_fil+1)
        self.longitudes = np.linspace(self.longitud_ini, self.longitud_fin, self.n_col+1)
        self.IP_map =  dict() # Se genera un diccionario con las IP como valores y con ci como las keys
        for i in range(self.n_fil * self.n_col):
            self.IP_map["c"+str(i)] = _IP_vec[i]

    def get_IP_map(self):
        return self.IP_map

    def get_cuad(self, coord_lon, coord_lat):
        # Se obtiene en que celda está segun las coordenadas de latitud y longitud
        for idx, lon in enumerate(self.longitudes):

            if coord_lon < lon:
                i_lon = idx -1
                break 
                
        for idx, lat in enumerate(self.latitudes):
            if coord_lat < lat:
                j_lat = idx -1 
                break
            
        return "c" + str(i_lon + self.n_col * j_lat)
    


