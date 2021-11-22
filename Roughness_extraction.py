# Package installs

import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks
import pandas as pd
from osgeo import gdal,ogr
import glob
import os
from scipy.stats import sem

from tqdm import tqdm
import time

# Extract slope values along transect
def Transect_data_roughness_to_df(DEM_tiff_pathway,T_pathway,T_no):
    DEM_tiff_pathway = DEM_tiff_pathway
    layer = gdal.Open(DEM_tiff_pathway)
    gt =layer.GetGeoTransform()
    bands = layer.RasterCount
#     print(bands)
#     print(gt)

    def Val_raster(x,y,layer,bands,gt):
        col=[]
        px = int((x - gt[0]) / gt[1])
        py =int((y - gt[3]) / gt[5])
        for j in range(bands):
            band = layer.GetRasterBand(j+1)
            data = band.ReadAsArray(px,py, 1, 1)
            col.append(data[0][0])
        return col

    # creation of an empty ogr linestring to handle all possible segments of a line with  Union (combining the segements)
    profilogr = ogr.Geometry(ogr.wkbLineString)
    # open the profile shapefile
    attempt = '01'
    
    T_pathway = T_pathway
    T_no = T_no
    
    path = glob.glob(os.path.join('/Users/domhardy/Desktop/REMA DEM/',T_pathway))[T_no]
    source = ogr.Open(path)
    cshp = source.GetLayer()
    # union the segments of the line
    for element in cshp:
        geom = element.GetGeometryRef()
        profilogr = profilogr.Union(geom)

    from shapely.wkb import loads
    # transformation in Shapely geometry
    profilshp = loads(profilogr.ExportToWkb())
    # creation the equidistant points on the line with a step of 8m
    lenght=profilshp.length
    REMA_x = []
    REMA_y = []
    REMA_roughness = []
    # distance of the topographic profile
    REMA_distance = []

    import decimal
    def float_range(start, stop, step):
        while start < stop:
            yield float(start)
            start += decimal.Decimal(step)

    # As REMA is 8m resolution change lenght value to correspond
    for currentdistance  in float_range(0,lenght,8):
        point = profilshp.interpolate(currentdistance)
        xp,yp=point.x, point.y
        REMA_x.append(xp)
        REMA_y.append(yp)
        REMA_roughness.append(Val_raster(xp,yp,layer, bands,gt)[0])
        REMA_distance.append(currentdistance)

    df = pd.DataFrame()

    df['REMA_x'] = REMA_x
    df['REMA_y'] = REMA_y
    df['REMA_roughness'] = REMA_roughness
    df['REMA_distance'] = REMA_distance
    

    return df

#DEM_pathway = '/Users/domhardy/Desktop/REMA DEM/Site A roughness tif.tif'
DEM_pathway = '/Volumes/LaCie/MD filter files/REMA 100m roughness.tif'
attempt = '01'
transect_pathway = f'Site_A_T*{attempt}*.shp'

start = time.time()
df1 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,0)
df2 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,1)
df3 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,2)
df4 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,3)
df5 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,4)
df6 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,5)
df7 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,6)
df8 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,7)
df9 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,8)
df10 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,9)
df11 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,10)
df12 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,11)
df13 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,12)
df14 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,13)
df15 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,14)
df16 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,15)
df17 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,16)
df18 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,17)
df19 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,18)
df20 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,19)
df21 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,20)
df22 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,21)
df23 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,22)
df24 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,23)
df25 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,24)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site B

#DEM_pathway = '/Users/domhardy/Desktop/REMA DEM/Site B roughness tif.tif'
DEM_pathway = '/Volumes/LaCie/MD filter files/REMA 100m roughness.tif'
attempt = '01'
transect_pathway = f'Site_B_T*{attempt}*.shp'

start = time.time()
SB_df1 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,0)
SB_df2 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,1)
SB_df3 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,2)
SB_df4 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,3)
SB_df5 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,4)
SB_df6 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,5)
SB_df7 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,6)
SB_df8 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,7)
SB_df9 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,8)
SB_df10 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,9)
SB_df11 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,10)
SB_df12 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,11)
SB_df13 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,12)
SB_df14 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,13)
SB_df15 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,14)
SB_df16 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,15)
SB_df17 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,16)
SB_df18 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,17)
SB_df19 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,18)
SB_df20 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,19)
SB_df21 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,20)
SB_df22 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,21)
SB_df23 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,22)
SB_df24 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,23)
SB_df25 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,24)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site C

#DEM_pathway = '/Users/domhardy/Desktop/REMA DEM/Site C roughness tif.tif'
DEM_pathway = '/Volumes/LaCie/MD filter files/REMA 100m roughness.tif'
attempt = '01'
transect_pathway = f'Site_C_T*{attempt}*.shp'

start = time.time()
SC_df1 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,0)
#SC_df2 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,1)
#SC_df3 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,2)
SC_df4 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,3)
SC_df5 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,4)
SC_df6 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,5)
SC_df7 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,6)
#SC_df8 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,7)
SC_df9 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,8)
SC_df10 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,9)
SC_df11 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,10)
SC_df12 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,11)
SC_df13 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,12)
SC_df14 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,13)
SC_df15 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,14)
SC_df16 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,15)
SC_df17 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,16)
SC_df18 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,17)
SC_df19 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,18)
SC_df20 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,19)
SC_df21 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,20)
SC_df22 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,21)
SC_df23 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,22)
SC_df24 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,23)
SC_df25 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,24)
SC_df26 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,25)
SC_df27 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,26)
SC_df28 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,27)
SC_df29 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,28)
SC_df30 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,29)
SC_df31 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,30)
SC_df32 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,31)
SC_df33 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,32)
SC_df34 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,33)
SC_df35 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,34)
SC_df36 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,35)
SC_df37 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,36)
SC_df38 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,37)
SC_df39 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,38)
SC_df40 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,39)
#SC_df41 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,40)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site D

#DEM_pathway = '/Users/domhardy/Desktop/REMA DEM/Site D roughness tif.tif'
DEM_pathway = '/Volumes/LaCie/MD filter files/REMA 100m roughness.tif'
attempt = '01'
transect_pathway = f'Site_D_T*{attempt}*.shp'

start = time.time()
SD_df1 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,0)
SD_df2 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,1)
SD_df3 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,2)
SD_df4 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,3)
SD_df5 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,4)
SD_df6 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,5)
SD_df7 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,6)
SD_df8 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,7)
SD_df9 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,8)
SD_df10 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,9)
SD_df11 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,10)
SD_df12 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,11)
SD_df13 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,12)
SD_df14 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,13)
SD_df15 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,14)
SD_df16 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,15)
SD_df17 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,16)
SD_df18 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,17)
SD_df19 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,18)
SD_df20 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,19)
SD_df21 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,20)
SD_df22 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,21)
SD_df23 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,22)
SD_df24 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,23)
SD_df25 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,24)
SD_df26 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,25)
SD_df27 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,26)
SD_df28 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,27)
SD_df29 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,28)
SD_df30 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,29)
SD_df31 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,30)
SD_df32 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,31)
SD_df33 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,32)
SD_df34 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,33)
SD_df35 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,34)
SD_df36 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,35)
SD_df37 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,36)
SD_df38 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,37)
SD_df39 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,38)
SD_df40 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,39)
SD_df41 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,40)
SD_df42 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,41)
SD_df43 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,42)
SD_df44 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,43)
SD_df45 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,44)
SD_df46 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,45)
SD_df47 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,46)
SD_df48 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,47)
SD_df49 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,48)
SD_df50 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,49)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site E

#DEM_pathway = '/Users/domhardy/Desktop/REMA DEM/Site E roughness tif.tif'
DEM_pathway = '/Volumes/LaCie/MD filter files/REMA 100m roughness.tif'
attempt = '01'
transect_pathway = f'Site_E_T*{attempt}*.shp'

start = time.time()
SE_df1 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,0)
SE_df2 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,1)
SE_df3 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,2)
SE_df4 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,3)
SE_df5 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,4)
SE_df6 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,5)
SE_df7 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,6)
SE_df8 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,7)
SE_df9 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,8)
SE_df10 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,9)
SE_df11 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,10)
SE_df12 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,11)
SE_df13 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,12)
SE_df14 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,13)
SE_df15 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,14)
SE_df16 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,15)
SE_df17 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,16)
SE_df18 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,17)
SE_df19 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,18)
SE_df20 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,19)
SE_df21 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,20)
SE_df22 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,21)
SE_df23 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,22)
SE_df24 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,23)
SE_df25 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,24)
SE_df26 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,25)
SE_df27 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,26)
SE_df28 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,27)
SE_df29 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,28)
SE_df30 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,29)
SE_df31 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,30)
SE_df32 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,31)
SE_df33 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,32)
SE_df34 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,33)
SE_df35 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,34)
SE_df36 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,35)
SE_df37 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,36)
SE_df38 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,37)
SE_df39 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,38)
SE_df40 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,39)
SE_df41 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,40)
SE_df42 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,41)
SE_df43 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,42)
SE_df44 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,43)
SE_df45 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,44)
SE_df46 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,45)
SE_df47 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,46)
SE_df48 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,47)
SE_df49 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,48)
SE_df50 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,49)
SE_df51 = Transect_data_roughness_to_df(DEM_pathway,transect_pathway,50)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)

def collect_roughness_val_from_mini_df(All_data_per_site):
    df_T = []
    for i in range(len(All_data_per_site)):
        a = All_data_per_site[i]['REMA_roughness']
        b = All_data_per_site[i]['REMA_distance']
        
        df = pd.DataFrame( columns=['roughness', 'REMA_dist'])
        df['roughness'] = a
        df['REMA_dist'] = b
        df_T.append(df)
        
        # Stats
        SEM_roughness = sem(df['roughness'])
        standard_deviation_roughness = np.std(df['roughness'])
##        print('roughness mean: ', np.mean(df['roughness']),
##              'roughness SEM: ', SEM_roughness,
##              'roughness SD: ', standard_deviation_roughness,
##              'No. of roughness points: ',len(df['roughness']))

        #print("")    

        #Add download bar for visual progress
        for i in tqdm (range(len(All_data_per_site[i])), desc="Loading…", ascii=False):
                time.sleep(0.01)
                #print(i)
        
    reformed_df = pd.concat(df_T, axis=1)
        
    return reformed_df

# list of transects
df_list = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,
          df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,
          df21,df22,df23,df24,df25]

start = time.time()
SA = collect_roughness_val_from_mini_df(df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SA)
# p = SA.iloc[:,1::2]
# print(p)

# list of transects
SB_df_list = [SB_df1, SB_df2, SB_df3, SB_df4,SB_df5, SB_df6, SB_df7, SB_df8, SB_df9, SB_df10,
             SB_df11, SB_df12, SB_df13, SB_df14,SB_df15, SB_df16, SB_df17, SB_df18, SB_df19, SB_df20,
             SB_df21, SB_df22, SB_df23, SB_df24,SB_df25]

start = time.time()
SB = collect_roughness_val_from_mini_df(SB_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SA)
# p = SA.iloc[:,1::2]
# print(p)

# list of transects
SC_df_list = [SC_df1,  SC_df4, SC_df5, SC_df6, SC_df7, SC_df9, SC_df10,
             SC_df11, SC_df12, SC_df13, SC_df14, SC_df15, SC_df16, SC_df17, SC_df18, SC_df19, SC_df20,
             SC_df21, SC_df22, SC_df23, SC_df24, SC_df25, SC_df26, SC_df27, SC_df28, SC_df29, SC_df30,
             SC_df31, SC_df32, SC_df33, SC_df34, SC_df35, SC_df36, SC_df37, SC_df38, SC_df39, SC_df40]


start = time.time()
SC = collect_roughness_val_from_mini_df(SC_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SA)
# p = SA.iloc[:,1::2]
# print(p)

# list of transects
SD_df_list = [SD_df1, SD_df2, SD_df3, SD_df4, SD_df5, SD_df6, SD_df7, SD_df8, SD_df9, SD_df10,
              SD_df11,SD_df12, SD_df13, SD_df14, SD_df15, SD_df16, SD_df17, SD_df18, SD_df19, SD_df20,
              SD_df21,SD_df22, SD_df23, SD_df24, SD_df25, SD_df26, SD_df27, SD_df28, SD_df29, SD_df30,
              SD_df31,SD_df32, SD_df33, SD_df34, SD_df35, SD_df36, SD_df37, SD_df38, SD_df39, SD_df40,
              SD_df41,SD_df42, SD_df43, SD_df44, SD_df45, SD_df46, SD_df47, SD_df48, SD_df49, SD_df50]

start = time.time()
SD = collect_roughness_val_from_mini_df(SD_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SA)
# p = SA.iloc[:,1::2]
# print(p)

# list of transects
SE_df_list = [SE_df1,SE_df2,SE_df3, SE_df4, SE_df5, SE_df6, SE_df7, SE_df8, SE_df9, SE_df10,
             SE_df11,SE_df12,SE_df13, SE_df14, SE_df15, SE_df16, SE_df17, SE_df18, SE_df19, SE_df20,
             SE_df21,SE_df22,SE_df23, SE_df24, SE_df25, SE_df26, SE_df27, SE_df28, SE_df29, SE_df30,
             SE_df31,SE_df32,SE_df33, SE_df34, SE_df35, SE_df36, SE_df37, SE_df38, SE_df39, SE_df40,
             SE_df41,SE_df42,SE_df43, SE_df44, SE_df45, SE_df46, SE_df47, SE_df48, SE_df49, SE_df50,
             SE_df51]

start = time.time()
SE = collect_roughness_val_from_mini_df(SE_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SA)
# p = SA.iloc[:,1::2]
# print(p)

def MD_roughness_calc_graphs(SA_roughness, SA_No_T,
                             SB_roughness, SB_No_T, 
                             SC_roughness, SC_No_T, 
                             SD_roughness, SD_No_T,
                             SE_roughness, SE_No_T):
    
    SA_new_list = []
    SB_new_list = []
    SC_new_list = []
    SD_new_list = []
    SE_new_list = []
    
    # convert columns to functionalm lists (un-nest the list)
    SA = SA_roughness.values.tolist()

    for i in range(SA_No_T):
        p = [x[i] for x in SA]
        for y in range(len(p)):
            SA_new_list.append(p[y])
                
    SA_new_list = [x for x in SA_new_list if np.isnan(x) == False]
    
    SB = SB_roughness.values.tolist()

    for i in range(SB_No_T):
        p = [x[i] for x in SB]
        for y in range(len(p)):
            SB_new_list.append(p[y])
                
    SB_new_list = [x for x in SB_new_list if np.isnan(x) == False]
            
    SC = SC_roughness.values.tolist()

    for i in range(SC_No_T):
        p = [x[i] for x in SC]
        for y in range(len(p)):
            SC_new_list.append(p[y])
                
    SC_new_list = [x for x in SC_new_list if np.isnan(x) == False]
    
    SD = SD_roughness.values.tolist()

    for i in range(SD_No_T):
        p = [x[i] for x in SD]
        for y in range(len(p)):
            SD_new_list.append(p[y])
                
    SD_new_list = [x for x in SD_new_list if np.isnan(x) == False]
    
    SE = SE_roughness.values.tolist()

    for i in range(SE_No_T):
        p = [x[i] for x in SE]
        for y in range(len(p)):
            SE_new_list.append(p[y])
                
    SE_new_list = [x for x in SE_new_list if np.isnan(x) == False]
    
#################################################################################################################    
# Plots    

    # Histogram plot
    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1,figsize=(22,12),tight_layout=True)
    ax1.hist(SA_new_list,bins = 500,edgecolor='gray', facecolor='gray', alpha=0.6) #Add range=[x,y] to remove outliers typical range 2-8m 
    ax2.hist(SB_new_list,bins = 500,edgecolor='gray', facecolor='gray', alpha=0.6)
    ax3.hist(SC_new_list,bins = 500,edgecolor='gray', facecolor='gray', alpha=0.6)
    ax4.hist(SD_new_list,bins = 500,edgecolor='gray', facecolor='gray', alpha=0.6)
    ax5.hist(SE_new_list,bins = 500,edgecolor='gray', facecolor='gray', alpha=0.6)
    
    ax1.set_ylabel('frequency',fontsize=18)
    ax2.set_ylabel('frequency',fontsize=18)
    ax3.set_ylabel('frequency',fontsize=18)
    ax4.set_ylabel('frequency',fontsize=18)
    ax5.set_ylabel('frequency',fontsize=18)
    
    ax1.set_title('(A)', loc='left',fontsize=22)
    ax2.set_title('(B)', loc='left',fontsize=22)
    ax3.set_title('(C)', loc='left',fontsize=22)
    ax4.set_title('(D)', loc='left',fontsize=22)
    ax5.set_title('(E)', loc='left',fontsize=22)
    
    ax1.xaxis.get_ticklocs(minor=True)
    ax1.minorticks_on()
    
    ax1.set_xlim(0,0.5)
    ax2.set_xlim(0,0.5)
    ax3.set_xlim(0,0.5)
    ax4.set_xlim(0,0.5)
    ax5.set_xlim(0,0.5) 
    
    ax5.set_xlabel('roughness ',fontsize=22)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    plt.savefig('/Users/domhardy/Dissertation/Dissertation---Megadunes/Megadune quantification/All Sites roughness extraction hist.jpg',dpi=900, transparent=True)
    plt.savefig('/Users/domhardy/Desktop/Undergrad dissertation/Dissertation Layout - LaTex/Images/All Sites roughness extraction hist.jpg',dpi=900, transparent=True)
    plt.show()

    #############################################


     # Combined list
    all_sites = []
    for i in range(len(SA_new_list)):
        a = SA_new_list[i]
        all_sites.append(a)
        
    for i in range(len(SB_new_list)):
        a = SB_new_list[i]
        all_sites.append(a)
        
    for i in range(len(SC_new_list)):
        a = SC_new_list[i]
        all_sites.append(a)
        
    for i in range(len(SD_new_list)):
        a = SD_new_list[i]
        all_sites.append(a)
        
    for i in range(len(SE_new_list)):
        a = SE_new_list[i]
        all_sites.append(a)


    fig, (ax1) = plt.subplots(figsize=(18,8),tight_layout=True)

    #continent spread from 1km res
    def continent_pixel_extraction(data, res):
    
        #Extract
        
        import rasterio
        raster = rasterio.open(data)
        band_arr = raster.read(1)
        px_vals = []
        
        for x in range(band_arr.shape[0]):
            for y in range(band_arr.shape[1]):
                if band_arr[x, y] != (-9999.0):
                    px_vals.append(band_arr[x, y])
        
        # plot
        import matplotlib.pyplot as plt
        
        if res == '1km':
            n, bins, patches = ax1.hist(x=px_vals, range=[0,100],bins=2500, color='MidnightBlue',
                                alpha=0.7, rwidth=0.85, label='Continent range')
    
    r_data = '/Volumes/LaCie/1km res Roughness_cont.tif'
    continent_pixel_extraction(r_data, '1km')

    ax1.hist(all_sites,bins = 200,edgecolor='firebrick', facecolor='firebrick', alpha=0.6,label='MD range')
    
    ax1.set_ylabel('frequency',fontsize=18)
    ax1.xaxis.get_ticklocs(minor=True)
    ax1.minorticks_on()
    ax1.set_title('(1km res Continent Spread)', loc='left',fontsize=22)
    ax1.set_xlabel('roughness ',fontsize=22)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    ax1.set_xlim(0,)
    plt.legend()

    plt.savefig('/Users/domhardy/Dissertation/Dissertation---Megadunes/Megadune quantification/Continent and combined roughness extraction hist.jpg',dpi=400, transparent=True)
    plt.savefig('/Users/domhardy/Desktop/Undergrad dissertation/Dissertation Layout - LaTex/Images/Continent and combined roughness extraction hist.jpg',dpi=400, transparent=True)
    plt.show()

#################################################################################################################    

# Stats
    print("Site A: ")
    SEM_roughness = sem(SA_new_list)
    standard_deviation_roughness = np.std(SA_new_list)
    print('roughness mean: ', np.mean(SA_new_list),
          'roughnesse SEM: ', SEM_roughness,
          'roughness SD: ', standard_deviation_roughness,
          'No. of roughness points: ',len(SA_new_list),
          'Q1: ', np.percentile(SA_new_list, [25]),
          'Q3: ', np.percentile(SA_new_list, [75]),
          'IQR: ', (np.percentile(SA_new_list, [75]) - np.percentile(SA_new_list, [25])),
          'Lower bound: ', np.percentile(SA_new_list, [25]) - (1.5*(np.percentile(SA_new_list, [75]) - np.percentile(SA_new_list, [25]))),
          'Upper bound: ', np.percentile(SA_new_list, [75]) + (1.5*(np.percentile(SA_new_list, [75]) - np.percentile(SA_new_list, [25])))
         )
    
    print("") 

    print("Site B: ")
    SB_SEM_roughness = sem(SB_new_list)
    SB_standard_deviation_roughness = np.std(SB_new_list)
    print('roughness mean: ', np.mean(SB_new_list),
          'roughness SEM: ', SB_SEM_roughness,
          'roughness SD: ', SB_standard_deviation_roughness,
          'No. of roughness points: ',len(SB_new_list),
          'Q1: ', np.percentile(SB_new_list, [25]),
          'Q3: ', np.percentile(SB_new_list, [75]),
          'IQR: ', (np.percentile(SB_new_list, [75]) - np.percentile(SB_new_list, [25])),
          'Lower bound: ', np.percentile(SB_new_list, [25]) - (1.5*(np.percentile(SB_new_list, [75]) - np.percentile(SB_new_list, [25]))),
          'Upper bound: ', np.percentile(SB_new_list, [75]) + (1.5*(np.percentile(SB_new_list, [75]) - np.percentile(SB_new_list, [25])))
         )

    print("") 

    print("Site C: ")
    SC_SEM_roughness = sem(SC_new_list)
    SC_standard_deviation_roughness = np.std(SC_new_list)
    print('roughness mean: ', np.mean(SB_new_list),
          'roughness SEM: ', SC_SEM_roughness,
          'roughness SD: ', SC_standard_deviation_roughness,
          'No. of roughness points: ',len(SC_new_list),
          'Q1: ', np.percentile(SC_new_list, [25]),
          'Q3: ', np.percentile(SC_new_list, [75]),
          'IQR: ', (np.percentile(SC_new_list, [75]) - np.percentile(SC_new_list, [25])),
          'Lower bound: ', np.percentile(SC_new_list, [25]) - (1.5*(np.percentile(SC_new_list, [75]) - np.percentile(SC_new_list, [25]))),
          'Upper bound: ', np.percentile(SC_new_list, [75]) + (1.5*(np.percentile(SC_new_list, [75]) - np.percentile(SC_new_list, [25])))
         )

    print("")

    print("Site D: ")
    SD_SEM_roughness = sem(SD_new_list)
    SD_standard_deviation_roughness = np.std(SD_new_list)
    print('roughness mean: ', np.mean(SD_new_list),
          'roughness SEM: ', SD_SEM_roughness,
          'roughness SD: ', SD_standard_deviation_roughness,
          'No. of roughness points: ',len(SD_new_list),
          'Q1: ', np.percentile(SD_new_list, [25]),
          'Q3: ', np.percentile(SD_new_list, [75]),
          'IQR: ', (np.percentile(SD_new_list, [75]) - np.percentile(SD_new_list, [25])),
          'Lower bound: ', np.percentile(SD_new_list, [25]) - (1.5*(np.percentile(SD_new_list, [75]) - np.percentile(SD_new_list, [25]))),
          'Upper bound: ', np.percentile(SD_new_list, [75]) + (1.5*(np.percentile(SD_new_list, [75]) - np.percentile(SD_new_list, [25])))
         )

    print("")

    print("Site E: ")
    SE_SEM_roughness = sem(SE_new_list)
    SE_standard_deviation_roughness = np.std(SE_new_list)
    print('roughness mean: ', np.mean(SE_new_list),
          'roughness SEM: ', SE_SEM_roughness,
          'roughness SD: ', SE_standard_deviation_roughness,
          'No. of roughness points: ',len(SE_new_list),
          'Q1: ', np.percentile(SE_new_list, [25]),
          'Q3: ', np.percentile(SE_new_list, [75]),
          'IQR: ', (np.percentile(SE_new_list, [75]) - np.percentile(SE_new_list, [25])),
          'Lower bound: ', np.percentile(SE_new_list, [25]) - (1.5*(np.percentile(SE_new_list, [75]) - np.percentile(SE_new_list, [25]))),
          'Upper bound: ', np.percentile(SE_new_list, [75]) + (1.5*(np.percentile(SE_new_list, [75]) - np.percentile(SE_new_list, [25])))
         )

    print("")

        


    #print(all_sites)

    SEM_all_sites = sem(all_sites)
    standard_deviation_all_sites = np.std(all_sites)
    print('roughness mean: ', np.mean(all_sites),
          'roughness SEM: ', SEM_all_sites,
          'roughness SD: ', standard_deviation_all_sites,
          'No. of roughness points: ',len(all_sites),
          'Q1: ', np.percentile(all_sites, [25]),
          'Q3: ', np.percentile(all_sites, [75]),
          'Lower bound: ', np.percentile(all_sites, [25]) - (1.5*(np.percentile(all_sites, [75]) - np.percentile(all_sites, [25]))),
          'Upper bound: ', np.percentile(all_sites, [75]) + (1.5*(np.percentile(all_sites, [75]) - np.percentile(all_sites, [25]))),
          'min: ', min(all_sites)
          )


    print("")

    #convert to csv file dataframe.
    df_A_roughness = pd.DataFrame(SA_new_list, columns=['A'])
    df_B_roughness = pd.DataFrame(SB_new_list, columns=['B'])
    df_C_roughness = pd.DataFrame(SC_new_list, columns=['C'])
    df_D_roughness = pd.DataFrame(SD_new_list, columns=['D'])
    df_E_roughness = pd.DataFrame(SE_new_list, columns=['E'])

    df_A_roughness = df_A_roughness.reset_index()
    df_B_roughness = df_B_roughness.reset_index()
    df_C_roughness = df_C_roughness.reset_index()
    df_D_roughness = df_D_roughness.reset_index()
    df_E_roughness = df_E_roughness.reset_index()
    
    roughness_df = [df_A_roughness, df_B_roughness, df_C_roughness, df_D_roughness, df_E_roughness]
    
    roughness_df_fin = pd.concat(roughness_df, axis=1)
    
    roughness_df_fin.to_csv('/Users/domhardy/Desktop/Roughness_100m_df.csv', index=False)
    
    # Mann Whitney U test
    
    
##    from scipy import stats
##
##    print("Site A v A : " ,{stats.mannwhitneyu(SA_new_list, SA_new_list)}) 
##    print(f"Site A v B : " ,{stats.mannwhitneyu(SA_new_list, SB_new_list)}) 
##    print(f"Site A v C : ", {stats.mannwhitneyu(SA_new_list, SC_new_list)})
##    print(f"Site A v D : " ,{stats.mannwhitneyu(SA_new_list, SD_new_list)}) 
##    print(f"Site A v E : ", {stats.mannwhitneyu(SA_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site B v A : ", {stats.mannwhitneyu(SB_new_list, SA_new_list)}) 
##    print(f"Site B v B : ", {stats.mannwhitneyu(SB_new_list, SB_new_list)}) 
##    print(f"Site B v C : ", {stats.mannwhitneyu(SB_new_list, SC_new_list)})
##    print(f"Site B v D : ", {stats.mannwhitneyu(SB_new_list, SD_new_list)}) 
##    print(f"Site B v E : ", {stats.mannwhitneyu(SB_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site C v A : ", {stats.mannwhitneyu(SC_new_list, SA_new_list)}) 
##    print(f"Site C v B : ", {stats.mannwhitneyu(SC_new_list, SB_new_list)}) 
##    print(f"Site C v C : ", {stats.mannwhitneyu(SC_new_list, SC_new_list)})
##    print(f"Site C v D : ", {stats.mannwhitneyu(SC_new_list, SD_new_list)}) 
##    print(f"Site C v E : ", {stats.mannwhitneyu(SC_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site D v A : ", {stats.mannwhitneyu(SD_new_list, SA_new_list)})
##    print(f"Site D v B : ", {stats.mannwhitneyu(SD_new_list, SB_new_list)}) 
##    print(f"Site D v C : ",{stats.mannwhitneyu(SD_new_list, SC_new_list)})
##    print(f"Site D v D : ", {stats.mannwhitneyu(SD_new_list, SD_new_list)}) 
##    print(f"Site D v E : ", {stats.mannwhitneyu(SD_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site E v A : ", {stats.mannwhitneyu(SE_new_list, SA_new_list)})
##    print(f"Site E v B : ", {stats.mannwhitneyu(SE_new_list, SB_new_list)}) 
##    print(f"Site E v C : ", {stats.mannwhitneyu(SE_new_list, SC_new_list)})
##    print(f"Site E v D : ", {stats.mannwhitneyu(SE_new_list, SD_new_list)}) 
##    print(f"Site E v E : ", {stats.mannwhitneyu(SE_new_list, SE_new_list)})
##    
##    # Kolmogorov–Smirnov tests
##    
##    from scipy.stats import kstest
##    
##    print("A: ", kstest(SA_new_list, 'norm'))
##    print("B: ", kstest(SB_new_list, 'norm'))
##    print("C: ", kstest(SC_new_list, 'norm'))
##    print("D: ", kstest(SD_new_list, 'norm'))
##    print("E: ", kstest(SE_new_list, 'norm'))
##    
##    from scipy.stats import ks_2samp
##    
##    print("Site A v A : " ,{ks_2samp(SA_new_list, SA_new_list)}) 
##    print(f"Site A v B : " ,{ks_2samp(SA_new_list, SB_new_list)}) 
##    print(f"Site A v C : ", {ks_2samp(SA_new_list, SC_new_list)})
##    print(f"Site A v D : " ,{ks_2samp(SA_new_list, SD_new_list)}) 
##    print(f"Site A v E : ", {ks_2samp(SA_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site B v A : ", {ks_2samp(SB_new_list, SA_new_list)}) 
##    print(f"Site B v B : ", {ks_2samp(SB_new_list, SB_new_list)}) 
##    print(f"Site B v C : ", {ks_2samp(SB_new_list, SC_new_list)})
##    print(f"Site B v D : ", {ks_2samp(SB_new_list, SD_new_list)}) 
##    print(f"Site B v E : ", {ks_2samp(SB_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site C v A : ", {ks_2samp(SC_new_list, SA_new_list)}) 
##    print(f"Site C v B : ", {ks_2samp(SC_new_list, SB_new_list)}) 
##    print(f"Site C v C : ", {ks_2samp(SC_new_list, SC_new_list)})
##    print(f"Site C v D : ", {ks_2samp(SC_new_list, SD_new_list)}) 
##    print(f"Site C v E : ", {ks_2samp(SC_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site D v A : ", {ks_2samp(SD_new_list, SA_new_list)})
##    print(f"Site D v B : ", {ks_2samp(SD_new_list, SB_new_list)}) 
##    print(f"Site D v C : ", {ks_2samp(SD_new_list, SC_new_list)})
##    print(f"Site D v D : ", {ks_2samp(SD_new_list, SD_new_list)}) 
##    print(f"Site D v E : ", {ks_2samp(SD_new_list, SE_new_list)})
##    
##    #####
##    
##    print(f"Site E v A : ", {ks_2samp(SE_new_list, SA_new_list)})
##    print(f"Site E v B : ", {ks_2samp(SE_new_list, SB_new_list)}) 
##    print(f"Site E v C : ", {ks_2samp(SE_new_list, SC_new_list)})
##    print(f"Site E v D : ", {ks_2samp(SE_new_list, SD_new_list)}) 
##    print(f"Site E v E : ", {ks_2samp(SE_new_list, SE_new_list)})


SA_data = SA.iloc[:,::2]
SB_data = SB.iloc[:,::2]
SC_data = SC.iloc[:,::2]
SD_data = SD.iloc[:,::2]
SE_data = SE.iloc[:,::2]


MD_roughness_calc_graphs(SA_data,25,
                         SB_data,25,
                         SC_data,37,
                         SD_data,50,
                         SE_data,51)

