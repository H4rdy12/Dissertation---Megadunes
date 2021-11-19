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
import peakdetect

def Transect_data_to_df(DEM_tiff_pathway,T_pathway,T_no):
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
    REMA_z = []
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
        REMA_z.append(Val_raster(xp,yp,layer, bands,gt)[0])
        REMA_distance.append(currentdistance)

    df = pd.DataFrame()

    df['REMA_x'] = REMA_x
    df['REMA_y'] = REMA_y
    df['REMA_z'] = REMA_z
    df['REMA_distance'] = REMA_distance
    

    return df

# list of transects
## Site A

DEM_pathway = '/Users/domhardy/Desktop/REMA DEM/Wilkes Land merged tiffs.tif'
attempt = '01'
transect_pathway = f'Site_A_T*{attempt}*.shp'

start = time.time()
df1 = Transect_data_to_df(DEM_pathway,transect_pathway,0)
df2 = Transect_data_to_df(DEM_pathway,transect_pathway,1)
df3 = Transect_data_to_df(DEM_pathway,transect_pathway,2)
df4 = Transect_data_to_df(DEM_pathway,transect_pathway,3)
df5 = Transect_data_to_df(DEM_pathway,transect_pathway,4)
df6 = Transect_data_to_df(DEM_pathway,transect_pathway,5)
df7 = Transect_data_to_df(DEM_pathway,transect_pathway,6)
df8 = Transect_data_to_df(DEM_pathway,transect_pathway,7)
df9 = Transect_data_to_df(DEM_pathway,transect_pathway,8)
df10 = Transect_data_to_df(DEM_pathway,transect_pathway,9)
df11 = Transect_data_to_df(DEM_pathway,transect_pathway,10)
df12 = Transect_data_to_df(DEM_pathway,transect_pathway,11)
df13 = Transect_data_to_df(DEM_pathway,transect_pathway,12)
df14 = Transect_data_to_df(DEM_pathway,transect_pathway,13)
df15 = Transect_data_to_df(DEM_pathway,transect_pathway,14)
df16 = Transect_data_to_df(DEM_pathway,transect_pathway,15)
df17 = Transect_data_to_df(DEM_pathway,transect_pathway,16)
df18 = Transect_data_to_df(DEM_pathway,transect_pathway,17)
df19 = Transect_data_to_df(DEM_pathway,transect_pathway,18)
df20 = Transect_data_to_df(DEM_pathway,transect_pathway,19)
df21 = Transect_data_to_df(DEM_pathway,transect_pathway,20)
df22 = Transect_data_to_df(DEM_pathway,transect_pathway,21)
df23 = Transect_data_to_df(DEM_pathway,transect_pathway,22)
df24 = Transect_data_to_df(DEM_pathway,transect_pathway,23)
df25 = Transect_data_to_df(DEM_pathway,transect_pathway,24)

time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site B

DEM_pathway = '/Volumes/LaCie/SiteB.tif'
attempt = '01'
transect_pathway = f'Site_B_T*{attempt}*.shp'

start = time.time()
SB_df1 = Transect_data_to_df(DEM_pathway,transect_pathway,0)
SB_df2 = Transect_data_to_df(DEM_pathway,transect_pathway,1)
SB_df3 = Transect_data_to_df(DEM_pathway,transect_pathway,2)
SB_df4 = Transect_data_to_df(DEM_pathway,transect_pathway,3)
SB_df5 = Transect_data_to_df(DEM_pathway,transect_pathway,4)
SB_df6 = Transect_data_to_df(DEM_pathway,transect_pathway,5)
SB_df7 = Transect_data_to_df(DEM_pathway,transect_pathway,6)
SB_df8 = Transect_data_to_df(DEM_pathway,transect_pathway,7)
SB_df9 = Transect_data_to_df(DEM_pathway,transect_pathway,8)
SB_df10 = Transect_data_to_df(DEM_pathway,transect_pathway,9)
SB_df11 = Transect_data_to_df(DEM_pathway,transect_pathway,10)
SB_df12 = Transect_data_to_df(DEM_pathway,transect_pathway,11)
SB_df13 = Transect_data_to_df(DEM_pathway,transect_pathway,12)
SB_df14 = Transect_data_to_df(DEM_pathway,transect_pathway,13)
SB_df15 = Transect_data_to_df(DEM_pathway,transect_pathway,14)
SB_df16 = Transect_data_to_df(DEM_pathway,transect_pathway,15)
SB_df17 = Transect_data_to_df(DEM_pathway,transect_pathway,16)
SB_df18 = Transect_data_to_df(DEM_pathway,transect_pathway,17)
SB_df19 = Transect_data_to_df(DEM_pathway,transect_pathway,18)
SB_df20 = Transect_data_to_df(DEM_pathway,transect_pathway,19)
SB_df21 = Transect_data_to_df(DEM_pathway,transect_pathway,20)
SB_df22 = Transect_data_to_df(DEM_pathway,transect_pathway,21)
SB_df23 = Transect_data_to_df(DEM_pathway,transect_pathway,22)
SB_df24 = Transect_data_to_df(DEM_pathway,transect_pathway,23)
SB_df25 = Transect_data_to_df(DEM_pathway,transect_pathway,24)

time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site C

DEM_pathway = '/Volumes/LaCie/REMA/mosaic/v1.1/8m/44_42/44_42_8m/44_42_8m_dem.tif'
attempt = '01'
transect_pathway = f'Site_C_T*{attempt}*.shp'

start = time.time()
SC_df1 = Transect_data_to_df(DEM_pathway,transect_pathway,0)
#SC_df2 = Transect_data_to_df(DEM_pathway,transect_pathway,1)
#SC_df3 = Transect_data_to_df(DEM_pathway,transect_pathway,2)
SC_df4 = Transect_data_to_df(DEM_pathway,transect_pathway,3)
SC_df5 = Transect_data_to_df(DEM_pathway,transect_pathway,4)
SC_df6 = Transect_data_to_df(DEM_pathway,transect_pathway,5)
SC_df7 = Transect_data_to_df(DEM_pathway,transect_pathway,6)
#SC_df8 = Transect_data_to_df(DEM_pathway,transect_pathway,7)
SC_df9 = Transect_data_to_df(DEM_pathway,transect_pathway,8)
SC_df10 = Transect_data_to_df(DEM_pathway,transect_pathway,9)
SC_df11 = Transect_data_to_df(DEM_pathway,transect_pathway,10)
SC_df12 = Transect_data_to_df(DEM_pathway,transect_pathway,11)
SC_df13 = Transect_data_to_df(DEM_pathway,transect_pathway,12)
SC_df14 = Transect_data_to_df(DEM_pathway,transect_pathway,13)
SC_df15 = Transect_data_to_df(DEM_pathway,transect_pathway,14)
SC_df16 = Transect_data_to_df(DEM_pathway,transect_pathway,15)
SC_df17 = Transect_data_to_df(DEM_pathway,transect_pathway,16)
SC_df18 = Transect_data_to_df(DEM_pathway,transect_pathway,17)
SC_df19 = Transect_data_to_df(DEM_pathway,transect_pathway,18)
SC_df20 = Transect_data_to_df(DEM_pathway,transect_pathway,19)
SC_df21 = Transect_data_to_df(DEM_pathway,transect_pathway,20)
SC_df22 = Transect_data_to_df(DEM_pathway,transect_pathway,21)
SC_df23 = Transect_data_to_df(DEM_pathway,transect_pathway,22)
SC_df24 = Transect_data_to_df(DEM_pathway,transect_pathway,23)
SC_df25 = Transect_data_to_df(DEM_pathway,transect_pathway,24)
SC_df26 = Transect_data_to_df(DEM_pathway,transect_pathway,25)
SC_df27 = Transect_data_to_df(DEM_pathway,transect_pathway,26)
SC_df28 = Transect_data_to_df(DEM_pathway,transect_pathway,27)
SC_df29 = Transect_data_to_df(DEM_pathway,transect_pathway,28)
SC_df30 = Transect_data_to_df(DEM_pathway,transect_pathway,29)
SC_df31 = Transect_data_to_df(DEM_pathway,transect_pathway,30)
SC_df32 = Transect_data_to_df(DEM_pathway,transect_pathway,31)
SC_df33 = Transect_data_to_df(DEM_pathway,transect_pathway,32)
SC_df34 = Transect_data_to_df(DEM_pathway,transect_pathway,33)
SC_df35 = Transect_data_to_df(DEM_pathway,transect_pathway,34)
SC_df36 = Transect_data_to_df(DEM_pathway,transect_pathway,35)
SC_df37 = Transect_data_to_df(DEM_pathway,transect_pathway,36)
SC_df38 = Transect_data_to_df(DEM_pathway,transect_pathway,37)
SC_df39 = Transect_data_to_df(DEM_pathway,transect_pathway,38)
SC_df40 = Transect_data_to_df(DEM_pathway,transect_pathway,39)
#SC_df41 = Transect_data_to_df(DEM_pathway,transect_pathway,40)


time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site D

DEM_pathway = '/Volumes/LaCie/Site D extended area.tif'
attempt = '01'
transect_pathway = f'Site_D_T*{attempt}*.shp'

start = time.time()
SD_df1 = Transect_data_to_df(DEM_pathway,transect_pathway,0)
SD_df2 = Transect_data_to_df(DEM_pathway,transect_pathway,1)
SD_df3 = Transect_data_to_df(DEM_pathway,transect_pathway,2)
SD_df4 = Transect_data_to_df(DEM_pathway,transect_pathway,3)
SD_df5 = Transect_data_to_df(DEM_pathway,transect_pathway,4)
SD_df6 = Transect_data_to_df(DEM_pathway,transect_pathway,5)
SD_df7 = Transect_data_to_df(DEM_pathway,transect_pathway,6)
SD_df8 = Transect_data_to_df(DEM_pathway,transect_pathway,7)
SD_df9 = Transect_data_to_df(DEM_pathway,transect_pathway,8)
SD_df10 = Transect_data_to_df(DEM_pathway,transect_pathway,9)
SD_df11 = Transect_data_to_df(DEM_pathway,transect_pathway,10)
SD_df12 = Transect_data_to_df(DEM_pathway,transect_pathway,11)
SD_df13 = Transect_data_to_df(DEM_pathway,transect_pathway,12)
SD_df14 = Transect_data_to_df(DEM_pathway,transect_pathway,13)
SD_df15 = Transect_data_to_df(DEM_pathway,transect_pathway,14)
SD_df16 = Transect_data_to_df(DEM_pathway,transect_pathway,15)
SD_df17 = Transect_data_to_df(DEM_pathway,transect_pathway,16)
SD_df18 = Transect_data_to_df(DEM_pathway,transect_pathway,17)
SD_df19 = Transect_data_to_df(DEM_pathway,transect_pathway,18)
SD_df20 = Transect_data_to_df(DEM_pathway,transect_pathway,19)
SD_df21 = Transect_data_to_df(DEM_pathway,transect_pathway,20)
SD_df22 = Transect_data_to_df(DEM_pathway,transect_pathway,21)
SD_df23 = Transect_data_to_df(DEM_pathway,transect_pathway,22)
SD_df24 = Transect_data_to_df(DEM_pathway,transect_pathway,23)
SD_df25 = Transect_data_to_df(DEM_pathway,transect_pathway,24)
SD_df26 = Transect_data_to_df(DEM_pathway,transect_pathway,25)
SD_df27 = Transect_data_to_df(DEM_pathway,transect_pathway,26)
SD_df28 = Transect_data_to_df(DEM_pathway,transect_pathway,27)
SD_df29 = Transect_data_to_df(DEM_pathway,transect_pathway,28)
SD_df30 = Transect_data_to_df(DEM_pathway,transect_pathway,29)
SD_df31 = Transect_data_to_df(DEM_pathway,transect_pathway,30)
SD_df32 = Transect_data_to_df(DEM_pathway,transect_pathway,31)
SD_df33 = Transect_data_to_df(DEM_pathway,transect_pathway,32)
SD_df34 = Transect_data_to_df(DEM_pathway,transect_pathway,33)
SD_df35 = Transect_data_to_df(DEM_pathway,transect_pathway,34)
SD_df36 = Transect_data_to_df(DEM_pathway,transect_pathway,35)
SD_df37 = Transect_data_to_df(DEM_pathway,transect_pathway,36)
SD_df38 = Transect_data_to_df(DEM_pathway,transect_pathway,37)
SD_df39 = Transect_data_to_df(DEM_pathway,transect_pathway,38)
SD_df40 = Transect_data_to_df(DEM_pathway,transect_pathway,39)
SD_df41 = Transect_data_to_df(DEM_pathway,transect_pathway,40)
SD_df42 = Transect_data_to_df(DEM_pathway,transect_pathway,41)
SD_df43 = Transect_data_to_df(DEM_pathway,transect_pathway,42)
SD_df44 = Transect_data_to_df(DEM_pathway,transect_pathway,43)
SD_df45 = Transect_data_to_df(DEM_pathway,transect_pathway,44)
SD_df46 = Transect_data_to_df(DEM_pathway,transect_pathway,45)
SD_df47 = Transect_data_to_df(DEM_pathway,transect_pathway,46)
SD_df48 = Transect_data_to_df(DEM_pathway,transect_pathway,47)
SD_df49 = Transect_data_to_df(DEM_pathway,transect_pathway,48)
SD_df50 = Transect_data_to_df(DEM_pathway,transect_pathway,49)

time.time()
print("time to run (minutes): ", (time.time() - start)/60)

# list of transects
## Site E

DEM_pathway = '/Volumes/LaCie/Site E ; near Ross ice shelf.tif'
attempt = '01'
transect_pathway = f'Site_E_T*{attempt}*.shp'

start = time.time()
SE_df1 = Transect_data_to_df(DEM_pathway,transect_pathway,0)
SE_df2 = Transect_data_to_df(DEM_pathway,transect_pathway,1)
SE_df3 = Transect_data_to_df(DEM_pathway,transect_pathway,2)
SE_df4 = Transect_data_to_df(DEM_pathway,transect_pathway,3)
SE_df5 = Transect_data_to_df(DEM_pathway,transect_pathway,4)
SE_df6 = Transect_data_to_df(DEM_pathway,transect_pathway,5)
SE_df7 = Transect_data_to_df(DEM_pathway,transect_pathway,6)
SE_df8 = Transect_data_to_df(DEM_pathway,transect_pathway,7)
SE_df9 = Transect_data_to_df(DEM_pathway,transect_pathway,8)
SE_df10 = Transect_data_to_df(DEM_pathway,transect_pathway,9)
SE_df11 = Transect_data_to_df(DEM_pathway,transect_pathway,10)
SE_df12 = Transect_data_to_df(DEM_pathway,transect_pathway,11)
SE_df13 = Transect_data_to_df(DEM_pathway,transect_pathway,12)
SE_df14 = Transect_data_to_df(DEM_pathway,transect_pathway,13)
SE_df15 = Transect_data_to_df(DEM_pathway,transect_pathway,14)
SE_df16 = Transect_data_to_df(DEM_pathway,transect_pathway,15)
SE_df17 = Transect_data_to_df(DEM_pathway,transect_pathway,16)
SE_df18 = Transect_data_to_df(DEM_pathway,transect_pathway,17)
SE_df19 = Transect_data_to_df(DEM_pathway,transect_pathway,18)
SE_df20 = Transect_data_to_df(DEM_pathway,transect_pathway,19)
SE_df21 = Transect_data_to_df(DEM_pathway,transect_pathway,20)
SE_df22 = Transect_data_to_df(DEM_pathway,transect_pathway,21)
SE_df23 = Transect_data_to_df(DEM_pathway,transect_pathway,22)
SE_df24 = Transect_data_to_df(DEM_pathway,transect_pathway,23)
SE_df25 = Transect_data_to_df(DEM_pathway,transect_pathway,24)
SE_df26 = Transect_data_to_df(DEM_pathway,transect_pathway,25)
SE_df27 = Transect_data_to_df(DEM_pathway,transect_pathway,26)
SE_df28 = Transect_data_to_df(DEM_pathway,transect_pathway,27)
SE_df29 = Transect_data_to_df(DEM_pathway,transect_pathway,28)
SE_df30 = Transect_data_to_df(DEM_pathway,transect_pathway,29)
SE_df31 = Transect_data_to_df(DEM_pathway,transect_pathway,30)
SE_df32 = Transect_data_to_df(DEM_pathway,transect_pathway,31)
SE_df33 = Transect_data_to_df(DEM_pathway,transect_pathway,32)
SE_df34 = Transect_data_to_df(DEM_pathway,transect_pathway,33)
SE_df35 = Transect_data_to_df(DEM_pathway,transect_pathway,34)
SE_df36 = Transect_data_to_df(DEM_pathway,transect_pathway,35)
SE_df37 = Transect_data_to_df(DEM_pathway,transect_pathway,36)
SE_df38 = Transect_data_to_df(DEM_pathway,transect_pathway,37)
SE_df39 = Transect_data_to_df(DEM_pathway,transect_pathway,38)
SE_df40 = Transect_data_to_df(DEM_pathway,transect_pathway,39)
SE_df41 = Transect_data_to_df(DEM_pathway,transect_pathway,40)
SE_df42 = Transect_data_to_df(DEM_pathway,transect_pathway,41)
SE_df43 = Transect_data_to_df(DEM_pathway,transect_pathway,42)
SE_df44 = Transect_data_to_df(DEM_pathway,transect_pathway,43)
SE_df45 = Transect_data_to_df(DEM_pathway,transect_pathway,44)
SE_df46 = Transect_data_to_df(DEM_pathway,transect_pathway,45)
SE_df47 = Transect_data_to_df(DEM_pathway,transect_pathway,46)
SE_df48 = Transect_data_to_df(DEM_pathway,transect_pathway,47)
SE_df49 = Transect_data_to_df(DEM_pathway,transect_pathway,48)
SE_df50 = Transect_data_to_df(DEM_pathway,transect_pathway,49)
SE_df51 = Transect_data_to_df(DEM_pathway,transect_pathway,50)


time.time()
print("time to run (minutes): ", (time.time() - start)/60)

def Peak_trough_finder(All_data_per_site):
    df_T = []
    for i in range(len(All_data_per_site)):
        a = All_data_per_site[i]['REMA_z']
        b = All_data_per_site[i]['REMA_distance']
        peaks = peakdetect.peakdetect(a, b,50)
        formatted_peaks_detected = [[x[0], x[1]] for w in peaks for x in w]
#         df_T.append(formatted_peaks_detected)
        
        df = pd.DataFrame(formatted_peaks_detected, columns=[('xcoord'), ('ycoord')])
        df_T.append(df)

        #Add download bar for visual progress
        for i in tqdm (range(len(All_data_per_site[i])), desc="Loading…", ascii=False):
                time.sleep(0.01)
                #print(i)
        
    reformed_df = pd.concat(df_T, axis=1)
        
    return reformed_df

# list of transects
df_list = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10, df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25]

start = time.time()
SA = Peak_trough_finder(df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SA)
# p = SA.iloc[:,1::2]
# print(p)

# list of transects
SB_df_list = [SB_df1, SB_df2, SB_df3, SB_df4,SB_df5, SB_df6, SB_df7, SB_df8, SB_df9, SB_df10,
              SB_df11, SB_df12, SB_df13, SB_df14, SB_df15, SB_df16, SB_df17, SB_df18, SB_df19, SB_df20,
              SB_df21, SB_df22, SB_df23, SB_df24, SB_df25]

start = time.time()
SB = Peak_trough_finder(SB_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SB)
# p = SB.iloc[:,1::2]
# print(p)

# list of transects
SC_df_list = [SC_df1,  SC_df4, SC_df5, SC_df6, SC_df7, SC_df9, SC_df10,
             SC_df11, SC_df12, SC_df13, SC_df14, SC_df15, SC_df16, SC_df17, SC_df18, SC_df19, SC_df20,
             SC_df21, SC_df22, SC_df23, SC_df24, SC_df25, SC_df26, SC_df27, SC_df28, SC_df29, SC_df30,
             SC_df31, SC_df32, SC_df33, SC_df34, SC_df35, SC_df36, SC_df37, SC_df38, SC_df39, SC_df40]

start = time.time()
SC = Peak_trough_finder(SC_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SC)
# p = SC.iloc[:,1::2]
# print(p)

# list of transects
SD_df_list = [SD_df1, SD_df2, SD_df3, SD_df4, SD_df5, SD_df6, SD_df7, SD_df8, SD_df9, SD_df10,
              SD_df11,SD_df12, SD_df13, SD_df14, SD_df15, SD_df16, SD_df17, SD_df18, SD_df19, SD_df20,
              SD_df21,SD_df22, SD_df23, SD_df24, SD_df25, SD_df26, SD_df27, SD_df28, SD_df29, SD_df30,
              SD_df31,SD_df32, SD_df33, SD_df34, SD_df35, SD_df36, SD_df37, SD_df38, SD_df39, SD_df40,
              SD_df41,SD_df42, SD_df43, SD_df44, SD_df45, SD_df46, SD_df47, SD_df48, SD_df49, SD_df50]

start = time.time()
SD = Peak_trough_finder(SD_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SD)
# p = SD.iloc[:,1::2]
# print(p)

# list of transects
SE_df_list = [SE_df1,SE_df2,SE_df3, SE_df4, SE_df5, SE_df6, SE_df7, SE_df8, SE_df9, SE_df10, 
              SE_df11, SE_df12, SE_df13, SE_df14, SE_df15, SE_df16, SE_df17, SE_df18, SE_df19, SE_df20, 
              SE_df21, SE_df22, SE_df23, SE_df24, SE_df25, SE_df26, SE_df27, SE_df28, SE_df29, SE_df30, 
              SE_df31, SE_df32, SE_df33, SE_df34, SE_df35, SE_df36, SE_df37, SE_df38, SE_df39, SE_df40,
              SE_df41, SE_df42, SE_df43, SE_df44, SE_df45, SE_df46, SE_df47, SE_df48, SE_df49, SE_df50,
              SE_df51]

start = time.time()
SE = Peak_trough_finder(SE_df_list)
time.time()
print("time to run (minutes): ", (time.time() - start)/60)
# print(SE)
# p = SE.iloc[:,1::2]
# print(p)

##def Peak_Transect_plot_fig(SA_range,SB_range,SC_range,SD_range,SE_range):
##    List_of_Sites_A_B = ['Site A','Site B']
##    List_of_Sites_C_D = ['Site C','Site D']
##    List_of_Sites_E = ['Site E']
##
##    fig, ax = plt.subplots(nrows=len(List_of_Sites_A_B), figsize=(18,25), tight_layout=True)
##    
##    for i in List_of_Sites_A_B:
##            Site_No = List_of_Sites_A_B.index(i)
##
##            ax[Site_No].set_ylabel('Elevation (m)',fontsize=22)
##
##
##            if Site_No == 0:
##                ax[Site_No].set_title('(A)', loc='left',fontsize=22)
##
##                for w in range(len(df_list)):
##                    T_no = range(len(df_list)).index(w)+1
##                    a = df_list[w]['REMA_z']
##                    b = df_list[w]['REMA_distance']
##                    ax[Site_No].plot(b,a,linewidth=2.2, label = ('T'+str(T_no)))
##
##                    n = 0
##                    for col in range(0,SA_range):
##                        a = n + col
##                        b = n + col+1
##                        ax[Site_No].scatter(SA.iloc[:,a],SA.iloc[:,b],marker='o',s=20, color='red')
##                        n = n +1
##                        
##            ax[Site_No].tick_params(axis='x', labelsize= 18)
##            ax[Site_No].tick_params(axis='y', labelsize= 18)
##            
##            if Site_No == 1:
##                ax[Site_No].set_title('(B)', loc='left',fontsize=22)
##                ax[Site_No].set_xlabel('Distance along transect (m)',fontsize=22)
##                for w in range(len(SB_df_list)):
##                    T_no = range(len(SB_df_list)).index(w)+1
##                    a = SB_df_list[w]['REMA_z']
##                    b = SB_df_list[w]['REMA_distance']
##                    ax[Site_No].plot(b,a,linewidth=2.2, label = ('T'+str(T_no)))
##
##                    B_n = 0
##                    for col in range(0,SB_range):
##                        B_a = B_n + col
##                        B_b = B_n+ col+1
##                        ax[Site_No].scatter(SB.iloc[:,B_a],SB.iloc[:,B_b],marker='o',s=20, color='red')
##                        B_n = B_n +1
##                        
##            ax[Site_No].set_xlim(0,150000)
##            plt.xticks(fontsize=18)
##            plt.yticks(fontsize=18)
##            ax[Site_No].legend(fontsize=14)
##            
##    #plt.savefig('/Users/domhardy/Desktop/All Site extraction line Peak detection trial_Part_1.jpg',dpi=900, transparent=True)     
##    plt.savefig('/Users/domhardy/Dissertation/Dissertation---Megadunes/Megadune quantification/All Site extraction line Peak detection trial_Part_1.jpg',dpi=900, transparent=True)
##    plt.savefig('/Users/domhardy/Desktop/Undergrad dissertation/Dissertation Layout - LaTex/Images/All Site extraction line Peak detection trial_Part_1.jpg',dpi=900, transparent=True)  
##        
##            
##    fig, ax2 = plt.subplots(nrows=len(List_of_Sites_C_D), figsize=(18,25), tight_layout=True)               
##    
##    for i in List_of_Sites_C_D:
##            Site_No = List_of_Sites_C_D.index(i)
##            
##            ax2[Site_No].set_ylabel('Elevation (m)',fontsize=22)
##
##            if Site_No == 0:
##                ax2[Site_No].set_title('(C)', loc='left',fontsize=22)
##                for w in range(len(SC_df_list)):
##                    T_no = range(len(SC_df_list)).index(w)+1
##                    a = SC_df_list[w]['REMA_z']
##                    b = SC_df_list[w]['REMA_distance']
##                    ax2[Site_No].plot(b,a,linewidth=1, label = ('T'+str(T_no)))
##
##                    C_n = 0
##                    for col in range(0,SC_range):
##                        a = C_n + col
##                        b = C_n+ col+1
##                        ax2[Site_No].scatter(SC.iloc[:,a],SC.iloc[:,b],marker='o',s=8, color='red')
##                        C_n = C_n +1
##                        
##            ax2[Site_No].tick_params(axis='x', labelsize= 18)
##            ax2[Site_No].tick_params(axis='y', labelsize= 18)
##
##
##            if Site_No == 1:
##                ax2[Site_No].set_title('(D)', loc='left',fontsize=22)
##                for w in range(len(SD_df_list)):
##                    T_no = range(len(SD_df_list)).index(w)+1
##                    a = SD_df_list[w]['REMA_z']
##                    b = SD_df_list[w]['REMA_distance']
##                    ax2[Site_No].plot(b,a,linewidth=2.2, label = ('T'+str(T_no)))
##
##                    D_n = 0
##                    for col in range(0,SD_range):
##                        a = D_n + col
##                        b = D_n+ col+1
##                        ax2[Site_No].scatter(SD.iloc[:,a],SD.iloc[:,b],marker='o',s=20, color='red')
##                        D_n = D_n +1
##                        
##            ax2[Site_No].tick_params(axis='x', labelsize= 18)
##            ax2[Site_No].tick_params(axis='y', labelsize= 18)
##            
##            
##            plt.xticks(fontsize=18)
##            plt.yticks(fontsize=18)
##            ax2[Site_No].legend(fontsize=10)
##            ax2[Site_No].set_xlim(0,40000)
##
##
###     plt.savefig('/Users/domhardy/Desktop/All Site extraction line Peak detection trial_Part_2.jpg',dpi=900, transparent=True)     
##    plt.savefig('/Users/domhardy/Dissertation/Dissertation---Megadunes/Megadune quantification/All Site extraction line Peak detection trial_Part_2.jpg',dpi=900, transparent=True)
##    plt.savefig('/Users/domhardy/Desktop/Undergrad dissertation/Dissertation Layout - LaTex/Images/All Site extraction line Peak detection trial_Part_2.jpg',dpi=900, transparent=True)  
        
##    fig, ax3 = plt.subplots(figsize=(18,12.5))               
##    
##    for i in List_of_Sites_E:
##            Site_No = List_of_Sites_E.index(i) 
##
##
##            if Site_No == 0:
##                ax3[Site_No].set_xlabel('Distance along transect (m)',fontsize=22)
##                ax3[Site_No].set_title('(E)', loc='left',fontsize=22)
##                for w in range(len(SE_df_list)):
##                    T_no = range(len(SE_df_list)).index(w)+1
##                    a = SE_df_list[w]['REMA_z']
##                    b = SE_df_list[w]['REMA_distance']
##                    ax3[Site_No].plot(b,a,linewidth=2.2, label = ('T'+str(T_no)))
##
##                    E_n = 0
##                    for col in range(0,SE_range):
##                        a = E_n + col
##                        b = E_n+ col+1
##                        ax3[Site_No].scatter(SE.iloc[:,a],SE.iloc[:,b],marker='o',s=20, color='red')
##                        E_n = E_n +1
##                        
##            ax3[Site_No].tick_params(axis='x', labelsize= 18)
##            ax3[Site_No].tick_params(axis='y', labelsize= 18)
##            
##            
##            plt.xticks(fontsize=18)
##            plt.yticks(fontsize=18)
##            ax3[Site_No].legend(fontsize=10)
##            ax3[Site_No].set_xlim(0,40000)
##
##
###     plt.savefig('/Users/domhardy/Desktop/All Site extraction line Peak detection trial_Part_3.jpg',dpi=900, transparent=True)     
##    plt.savefig('/Users/domhardy/Dissertation/Dissertation---Megadunes/Megadune quantification/All Site extraction line Peak detection trial_Part_3.jpg',dpi=900, transparent=True)
##    plt.savefig('/Users/domhardy/Desktop/Undergrad dissertation/Dissertation Layout - LaTex/Images/All Site extraction line Peak detection trial_Part_3.jpg',dpi=900, transparent=True)  
##        

            
##start = time.time()
##Peak_Transect_plot_fig(25,25,37,50,51) # No. of transects per site
##time.time()
##print("time to run (seconds): ", time.time() - start)

def MD_Wavelength_calc(SA_Site_peak_data, SA_No_T,SB_Site_peak_data, SB_No_T, SC_Site_peak_data, SC_No_T, SD_Site_peak_data, SD_No_T, SE_Site_peak_data, SE_No_T):
    SA_new_list = []
    SB_new_list = []
    SC_new_list = []
    SD_new_list = []
    SE_new_list = []
    all_sites_wvl=[]
    
    # convert columns to functionalm lists (un-nest the list)
    SA = SA_Site_peak_data.values.tolist()

    for i in range(SA_No_T):
        p = [x[i] for x in SA]
        for y in range(len(p)):
        # Does this element belong in the resulting list?
            if y % 2 == 0:
            # Add this element to the resulting list
                SA_new_list.append(p[y])
                
                
    SA_new_list = [x for x in SA_new_list if np.isnan(x) == False]
            
#     print(new_list)
#     print(len(new_list))

    SA_wavelengths =[]

    freq_SA = [(n-SA_new_list[b-1]) if b else n for b,n in enumerate(SA_new_list)]
    del freq_SA[0]
    freq_SA = [item for item in freq_SA if item >= 0]

    freq_SA = freq_SA
    SA_wavelengths.append(freq_SA)
    all_sites_wvl.append(freq_SA)
    
#     print("")
#     print("_______________")
#     print(wavelengths)
#     print(len(wavelengths))

    
    SA_x_generator=[]
    for i in range(len(freq_SA)): 
        SA_x_generator.append(i)
#     print(SA_x_generator)
    
    # Site B
    # convert columns to functionalm lists (un-nest the list)
    SB = SB_Site_peak_data.values.tolist()

    for i in range(SB_No_T):
        p = [x[i] for x in SB]
        for y in range(len(p)):
        # Does this element belong in the resulting list?
            if y % 2 == 0:
            # Add this element to the resulting list
                SB_new_list.append(p[y])
            
    
    SB_new_list = [x for x in SB_new_list if np.isnan(x) == False]
            
#     print(new_list)
#     print(len(new_list))

    SB_wavelengths =[]

    freq_SB = [(n-SB_new_list[b-1]) if b else n for b,n in enumerate(SB_new_list)]
    del freq_SB[0]
    freq_SB = [item for item in freq_SB if item >= 0]

    freq_SB = freq_SB
    SB_wavelengths.append(freq_SB)
    all_sites_wvl.append(freq_SB)
    
#     print("")
#     print("_______________")
#     print(wavelengths)
#     print(len(wavelengths))

    SB_x_generator=[]
    for i in range(len(freq_SB)): 
        SB_x_generator.append(i)
#     print(SB_x_generator)
    
    # Site C
    # convert columns to functionalm lists (un-nest the list)
    SC = SC_Site_peak_data.values.tolist()

    for i in range(SC_No_T):
        p = [x[i] for x in SC]
        for y in range(len(p)):
        # Does this element belong in the resulting list?
            if y % 2 == 0:
            # Add this element to the resulting list
                SC_new_list.append(p[y])
            
    
    SC_new_list = [x for x in SC_new_list if np.isnan(x) == False]
            
#     print(new_list)
#     print(len(new_list))

    SC_wavelengths =[]

    freq_SC = [(n-SC_new_list[b-1]) if b else n for b,n in enumerate(SC_new_list)]
    del freq_SC[0]
    freq_SC = [item for item in freq_SC if item >= 0]

    freq_SC = freq_SC
    SC_wavelengths.append(freq_SC)
    all_sites_wvl.append(freq_SC)

    
#     print("")
#     print("_______________")
#     print(wavelengths)
#     print(len(wavelengths))

    SC_x_generator=[]
    for i in range(len(freq_SC)): 
        SC_x_generator.append(i)
#     print(SC_x_generator)
    
    # Site D
    # convert columns to functionalm lists (un-nest the list)
    SD = SD_Site_peak_data.values.tolist()

    for i in range(SD_No_T):
        p = [x[i] for x in SD]
        for y in range(len(p)):
        # Does this element belong in the resulting list?
            if y % 2 == 0:
            # Add this element to the resulting list
                SD_new_list.append(p[y])
            
    
    SD_new_list = [x for x in SD_new_list if np.isnan(x) == False]
            
#     print(new_list)
#     print(len(new_list))

    SD_wavelengths =[]

    freq_SD = [(n-SD_new_list[b-1]) if b else n for b,n in enumerate(SD_new_list)]
    del freq_SD[0]
    freq_SD = [item for item in freq_SD if item >= 0]

    freq_SD = freq_SD
    SD_wavelengths.append(freq_SD)
    all_sites_wvl.append(freq_SD)
    
#     print("")
#     print("_______________")
#     print(wavelengths)
#     print(len(wavelengths))

    SD_x_generator=[]
    for i in range(len(freq_SD)): 
        SD_x_generator.append(i)
#     print(SD_x_generator)
    
    # Site E
    # convert columns to functionalm lists (un-nest the list)
    SE = SE_Site_peak_data.values.tolist()

    for i in range(SE_No_T):
        p = [x[i] for x in SE]
        for y in range(len(p)):
        # Does this element belong in the resulting list?
            if y % 2 == 0:
            # Add this element to the resulting list
                SE_new_list.append(p[y])
            
    
    SE_new_list = [x for x in SE_new_list if np.isnan(x) == False]
            
#     print(new_list)
#     print(len(new_list))

    SE_wavelengths =[]

    freq_SE = [(n-SE_new_list[b-1]) if b else n for b,n in enumerate(SE_new_list)]
    del freq_SE[0]
    freq_SE = [item for item in freq_SE if item >= 0]

    freq_SE = freq_SE
    SE_wavelengths.append(freq_SE)
    all_sites_wvl.append(freq_SE)
    
#     print("")
#     print("_______________")
#     print(wavelengths)
#     print(len(wavelengths))

    SE_x_generator=[]
    for i in range(len(freq_SE)): 
        SE_x_generator.append(i)
#     print(SE_x_generator)
    
    

#################################################################################################################    
### Plots    
##
##    # Scatter plot
##    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1,figsize=(20,12),tight_layout=True)
##    ax1.scatter(SA_x_generator,freq_SA)
##    ax2.scatter(SB_x_generator,freq_SB)
##    ax3.scatter(SC_x_generator,freq_SC)
##    ax4.scatter(SD_x_generator,freq_SD)
##    ax5.scatter(SE_x_generator,freq_SE)
##    
##    ax1.set_ylabel('Wavelength (m)',fontsize=18)
##    ax2.set_ylabel('Wavelength (m)',fontsize=18)
##    ax3.set_ylabel('Wavelength (m)',fontsize=18)
##    ax4.set_ylabel('Wavelength (m)',fontsize=18)
##    ax5.set_ylabel('Wavelength (m)',fontsize=18)
##    
##    ax1.set_title('(A)', loc='left',fontsize=22)
##    ax2.set_title('(B)', loc='left',fontsize=22)
##    ax3.set_title('(C)', loc='left',fontsize=22)
##    ax4.set_title('(D)', loc='left',fontsize=22)
##    ax5.set_title('(E)', loc='left',fontsize=22)
##    
##    ax5.set_xlabel('Peak along transect',fontsize=18)
##    plt.xticks(fontsize=14)
##    plt.yticks(fontsize=14)
##    ax1.set_ylim(0,17000)
##    ax2.set_ylim(0,17000)
##    ax5.set_ylim(0,17000)
##    #plt.legend(fontsize=22)
##    plt.show()
##
##    # Histogram plot
##    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1,figsize=(20,12),tight_layout=True)
##    ax1.hist(SA_wavelengths,bins = 500,edgecolor='black', facecolor='gray', alpha=0.6) #Add range=[x,y] to remove outliers typical range 2-8m 
##    ax2.hist(SB_wavelengths,bins = 500,edgecolor='black', facecolor='gray', alpha=0.6)
##    ax3.hist(SC_wavelengths,bins = 500,edgecolor='black', facecolor='gray', alpha=0.6)
##    ax4.hist(SD_wavelengths,bins = 500,edgecolor='black', facecolor='gray', alpha=0.6)
##    ax5.hist(SE_wavelengths,bins = 500,edgecolor='black', facecolor='gray', alpha=0.6)
##    
##    ax1.set_ylabel('frequency',fontsize=18)
##    ax2.set_ylabel('frequency',fontsize=18)
##    ax3.set_ylabel('frequency',fontsize=18)
##    ax4.set_ylabel('frequency',fontsize=18)
##    ax5.set_ylabel('frequency',fontsize=18)
##    
##    ax1.set_title('(A)', loc='left',fontsize=22)
##    ax2.set_title('(B)', loc='left',fontsize=22)
##    ax3.set_title('(C)', loc='left',fontsize=22)
##    ax4.set_title('(D)', loc='left',fontsize=22)
##    ax5.set_title('(E)', loc='left',fontsize=22)
##    
##    ax1.xaxis.get_ticklocs(minor=True)
##    ax1.minorticks_on()
##    ax1.set_xlim(0,17000)
##    ax2.set_xlim(0,17000)
##    ax3.set_xlim(0)
##    ax4.set_xlim(0)
##    ax5.set_xlim(0,17000)
##    
##    ax5.set_xlabel('wavelength (m)',fontsize=22)
##    plt.xticks(fontsize=14)
##    plt.yticks(fontsize=14)
##    #plt.legend(fontsize=22)
##    
##    plt.savefig('/Users/domhardy/Dissertation/Dissertation---Megadunes/Megadune quantification/All Sites extraction wavelengths hist.jpg',dpi=900, transparent=True)
##    plt.savefig('/Users/domhardy/Desktop/Undergrad dissertation/Dissertation Layout - LaTex/Images/All Sites extraction wavelengths hist.jpg',dpi=900, transparent=True)
##    plt.show()


#################################################################################################################    
    # Stats 
    
    # Site A 
    SEM_wl = sem(freq_SA)
    standard_deviation_wl = np.std(SA_wavelengths)
    print("Site A: ")
    print('Wavelengths mean: ', np.mean(SA_wavelengths),
          'Wavelengths SEM: ', SEM_wl,
          'Wavelengths SD: ', standard_deviation_wl,
          'No. of Wavelength points: ',len(freq_SA),
          'Q1: ', np.percentile(SA_wavelengths, [25]),
          'Q3: ', np.percentile(SA_wavelengths, [75]),
          'IQR: ', (np.percentile(SA_wavelengths, [75]) - np.percentile(SA_wavelengths, [25])),
          'Lower bound: ', np.percentile(SA_wavelengths, [25]) - (1.5*(np.percentile(SA_wavelengths, [75]) - np.percentile(SA_wavelengths, [25]))),
          'Upper bound: ', np.percentile(SA_wavelengths, [75]) + (1.5*(np.percentile(SA_wavelengths, [75]) - np.percentile(SA_wavelengths, [25]))),
          'min: ', min(freq_SA),
          '10%: ', np.percentile(SA_wavelengths, [10]),
          '90%: ', np.percentile(SA_wavelengths, [90])
         )
    print("")    

    # Site B 
    SEM_wl_B = sem(freq_SB)
    standard_deviation_wl_B = np.std(SB_wavelengths)
    print("Site B: ")
    print('Wavelengths mean: ', np.mean(SB_wavelengths),
          'Wavelengths SEM: ', SEM_wl_B,
          'Wavelengths SD: ', standard_deviation_wl_B,
          'No. of Wavelength points: ',len(freq_SB),
          'Q1: ', np.percentile(SB_wavelengths, [25]),
          'Q3: ', np.percentile(SB_wavelengths, [75]),
          'IQR: ', (np.percentile(SB_wavelengths, [75]) - np.percentile(SB_wavelengths, [25])),
          'Lower bound: ', np.percentile(SB_wavelengths, [25]) - (1.5*(np.percentile(SB_wavelengths, [75]) - np.percentile(SB_wavelengths, [25]))),
          'Upper bound: ', np.percentile(SB_wavelengths, [75]) + (1.5*(np.percentile(SB_wavelengths, [75]) - np.percentile(SB_wavelengths, [25]))),
          'min: ', min(freq_SB),
          '10%: ', np.percentile(SB_wavelengths, [10]),
          '90%: ', np.percentile(SB_wavelengths, [90])
         )
    
    print("")    

    # Site C 
    SEM_wl_C = sem(freq_SC)
    standard_deviation_wl_C = np.std(SC_wavelengths)
    print("Site C: ")
    print('Wavelengths mean: ', np.mean(SC_wavelengths),
          'Wavelengths SEM: ', SEM_wl_C,
          'Wavelengths SD: ', standard_deviation_wl_C,
          'No. of Wavelength points: ',len(freq_SC),
          'Q1: ', np.percentile(SC_wavelengths, [25]),
          'Q3: ', np.percentile(SC_wavelengths, [75]),
          'IQR: ', (np.percentile(SC_wavelengths, [75]) - np.percentile(SC_wavelengths, [25])),
          'Lower bound: ', np.percentile(SC_wavelengths, [25]) - (1.5*(np.percentile(SC_wavelengths, [75]) - np.percentile(SC_wavelengths, [25]))),
          'Upper bound: ', np.percentile(SC_wavelengths, [75]) + (1.5*(np.percentile(SC_wavelengths, [75]) - np.percentile(SC_wavelengths, [25]))),
          'min: ', min(freq_SC),
          '10%: ', np.percentile(SC_wavelengths, [10]),
          '90%: ', np.percentile(SC_wavelengths, [90])
         )
    
    print("")   
    
    # Site D 
    SEM_wl_D = sem(freq_SD)
    standard_deviation_wl_D = np.std(SD_wavelengths)
    print("Site D: ")
    print('Wavelengths mean: ', np.mean(SD_wavelengths),
          'Wavelengths SEM: ', SEM_wl_D,
          'Wavelengths SD: ', standard_deviation_wl_D,
          'No. of Wavelength points: ',len(freq_SD),
          'Q1: ', np.percentile(SD_wavelengths, [25]),
          'Q3: ', np.percentile(SD_wavelengths, [75]),
          'IQR: ', (np.percentile(SD_wavelengths, [75]) - np.percentile(SD_wavelengths, [25])),
          'Lower bound: ', np.percentile(SD_wavelengths, [25]) - (1.5*(np.percentile(SD_wavelengths, [75]) - np.percentile(SD_wavelengths, [25]))),
          'Upper bound: ', np.percentile(SD_wavelengths, [75]) + (1.5*(np.percentile(SD_wavelengths, [75]) - np.percentile(SD_wavelengths, [25]))),
          'min: ', min(freq_SD),
          '10%: ', np.percentile(SD_wavelengths, [10]),
          '90%: ', np.percentile(SD_wavelengths, [90])
         )
    
    print("")    

    # Site E 
    SEM_wl_E = sem(freq_SE)
    standard_deviation_wl_E = np.std(SE_wavelengths)
    print("Site E: ")
    print('Wavelengths mean: ', np.mean(SE_wavelengths),
          'Wavelengths SEM: ', SEM_wl_E,
          'Wavelengths SD: ', standard_deviation_wl_E,
          'No. of Wavelength points: ',len(freq_SE),
          'Q1: ', np.percentile(SE_wavelengths, [25]),
          'Q3: ', np.percentile(SE_wavelengths, [75]),
          'IQR: ', (np.percentile(SE_wavelengths, [75]) - np.percentile(SE_wavelengths, [25])),
          'Lower bound: ', np.percentile(SE_wavelengths, [25]) - (1.5*(np.percentile(SE_wavelengths, [75]) - np.percentile(SE_wavelengths, [25]))),
          'Upper bound: ', np.percentile(SE_wavelengths, [75]) + (1.5*(np.percentile(SE_wavelengths, [75]) - np.percentile(SE_wavelengths, [25]))),
          'min: ', min(freq_SE),
          '10%: ', np.percentile(SE_wavelengths, [10]),
          '90%: ', np.percentile(SE_wavelengths, [90])
         )

    # Combined list
    all_sites_wvl = []
    for i in range(len(freq_SA)):
        a = freq_SA[i]
        all_sites_wvl.append(a)
        
    for i in range(len(freq_SB)):
        a = freq_SB[i]
        all_sites_wvl.append(a)
        
    for i in range(len(freq_SC)):
        a = freq_SC[i]
        all_sites_wvl.append(a)
        
    for i in range(len(freq_SD)):
        a = freq_SD[i]
        all_sites_wvl.append(a)
        
    for i in range(len(freq_SE)):
        a = freq_SE[i]
        all_sites_wvl.append(a)
        


    #print(all_sites_wvl)

    SEM_wl_all_sites = sem(all_sites_wvl)
    standard_deviation_wl_all_sites = np.std(all_sites_wvl)
    print('Wavelengths mean: ', np.mean(all_sites_wvl),
          'Wavelengths SEM: ', SEM_wl_all_sites,
          'Wavelengths SD: ', standard_deviation_wl_all_sites,
          'No. of Wavelength points: ',len(all_sites_wvl),
          'Q1: ', np.percentile(all_sites_wvl, [25]),
          'Q3: ', np.percentile(all_sites_wvl, [75]),
          'Lower bound: ', np.percentile(all_sites_wvl, [25]) - (1.5*(np.percentile(all_sites_wvl, [75]) - np.percentile(all_sites_wvl, [25]))),
          'Upper bound: ', np.percentile(all_sites_wvl, [75]) + (1.5*(np.percentile(all_sites_wvl, [75]) - np.percentile(all_sites_wvl, [25]))),
          'min: ', min(all_sites_wvl),
          '10%: ', np.percentile(all_sites_wvl, [10]),
          '90%: ', np.percentile(all_sites_wvl, [90])
          )


    df_A_wvl = pd.DataFrame(freq_SA, columns=['A'])
    df_B_wvl = pd.DataFrame(freq_SB, columns=['B'])
    df_C_wvl = pd.DataFrame(freq_SC, columns=['C'])
    df_D_wvl = pd.DataFrame(freq_SD, columns=['D'])
    df_E_wvl = pd.DataFrame(freq_SE, columns=['E'])

    df_A_wvl = df_A_wvl.reset_index()
    df_B_wvl = df_B_wvl.reset_index()
    df_C_wvl = df_C_wvl.reset_index()
    df_D_wvl = df_D_wvl.reset_index()
    df_E_wvl = df_E_wvl.reset_index()
    
    wvl_df = [df_A_wvl, df_B_wvl, df_C_wvl, df_D_wvl, df_E_wvl]
    
    wvl_df_fin = pd.concat(wvl_df, axis=1)
    
    wvl_df_fin.to_csv('/Users/domhardy/Desktop/wvl_df.csv', index=False)
    

    #Stats KW
    
    from scipy import stats
    
#     print("Site A v A : ",{stats.kruskal(SA_wavelengths, SA_wavelengths)}) 
#     print("Site A v B : ",{stats.kruskal(SA_wavelengths, SB_wavelengths)}) 
#     print("Site A v C : ",{stats.kruskal(SA_wavelengths, SC_wavelengths)})
#     print("Site A v D : ",{stats.kruskal(SA_wavelengths, SD_wavelengths)}) 
#     print("Site A v E : ",{stats.kruskal(SA_wavelengths, SE_wavelengths)})
    
#     #####
    
#     print("Site B v A : ",{stats.kruskal(SB_wavelengths, SA_wavelengths)}) 
#     print("Site B v B : ",{stats.kruskal(SB_wavelengths, SB_wavelengths)}) 
#     print("Site B v C : ",{stats.kruskal(SB_wavelengths, SC_wavelengths)})
#     print("Site B v D : ",{stats.kruskal(SB_wavelengths, SD_wavelengths)}) 
#     print("Site B v E : ",{stats.kruskal(SB_wavelengths, SE_wavelengths)})
    
#     #####
    
#     print(f"Site C v A : ",{stats.kruskal(SC_wavelengths, SA_wavelengths)}) 
#     print(f"Site C v B : ",{stats.kruskal(SC_wavelengths, SB_wavelengths)}) 
#     print(f"Site C v C : ",{stats.kruskal(SC_wavelengths, SC_wavelengths)})
#     print(f"Site C v D : ",{stats.kruskal(SC_wavelengths, SD_wavelengths)}) 
#     print(f"Site C v E : ",{stats.kruskal(SC_wavelengths, SE_wavelengths)})
    
#     #####
    
#     print(f"Site D v A : ",{stats.kruskal(SD_wavelengths, SA_wavelengths)})
#     print(f"Site D v B : ",{stats.kruskal(SD_wavelengths, SB_wavelengths)}) 
#     print(f"Site D v C : ",{stats.kruskal(SD_wavelengths, SC_wavelengths)})
#     print(f"Site D v D : ",{stats.kruskal(SD_wavelengths, SD_wavelengths)}) 
#     print(f"Site D v E : ",{stats.kruskal(SD_wavelengths, SE_wavelengths)})
    
#     #####
    
#     print(f"Site E v A : ",{stats.kruskal(SE_wavelengths, SA_wavelengths)})
#     print(f"Site E v B : ",{stats.kruskal(SE_wavelengths, SB_wavelengths)}) 
#     print(f"Site E v C : ",{stats.kruskal(SE_wavelengths, SC_wavelengths)})
#     print(f"Site E v D : ",{stats.kruskal(SE_wavelengths, SD_wavelengths)}) 
#     print(f"Site E v E : ",{stats.kruskal(SE_wavelengths, SE_wavelengths)})

start = time.time()
MD_Wavelength_calc(SA.iloc[:,::2],25,
                   SB.iloc[:,::2],25,
                   SC.iloc[:,::2],37,
                   SD.iloc[:,::2],50,
                   SE.iloc[:,::2],51) # Enter complete Site dataframe and number of Transect lines
time.time()
print("time to run (seconds): ", time.time() - start)

def MD_amplitudes_calc(SA_df_T_ycoord, SA_No_T, SB_df_T_ycoord, SB_No_T, SC_df_T_ycoord, SC_No_T, SD_df_T_ycoord, SD_No_T, SE_df_T_ycoord, SE_No_T):
    SA_amplitudes =[]
    SB_amplitudes =[]
    SC_amplitudes =[]
    SD_amplitudes =[]
    SE_amplitudes =[]
    
    SA = SA_df_T_ycoord.values.tolist()
    
    for i in range(SA_No_T):
        p = [x[i] for x in SA]
    
        for x, y in zip(p[0::],p[1::]): 
            if x > y:
                diff = x - y
                SA_amplitudes.append(diff)

            else:
                diff = y - x
                SA_amplitudes.append(diff)

    SA_amplitudes = [x for x in SA_amplitudes if np.isnan(x) == False]
#     print(amplitudes)
    
    SA_x_generator=[]
    for i in range(len(SA_amplitudes)):
        SA_x_generator.append(i)
#     print(SA_x_generator)
    
    # Site B
    SB = SB_df_T_ycoord.values.tolist()
    
    for i in range(SB_No_T):
        p = [x[i] for x in SB]
    
        for x, y in zip(p[0::],p[1::]): 
            if x > y:
                diff = x - y
                SB_amplitudes.append(diff)

            else:
                diff = y - x
                SB_amplitudes.append(diff)

    SB_amplitudes = [x for x in SB_amplitudes if np.isnan(x) == False]
#     print(amplitudes)
    
    SB_x_generator=[]
    for i in range(len(SB_amplitudes)):
        SB_x_generator.append(i)
#     print(SB_x_generator)

    
    # Site C
    SC = SC_df_T_ycoord.values.tolist()
    
    for i in range(SC_No_T):
        p = [x[i] for x in SC]
    
        for x, y in zip(p[0::],p[1::]): 
            if x > y:
                diff = x - y
                SC_amplitudes.append(diff)

            else:
                diff = y - x
                SC_amplitudes.append(diff)

    SC_amplitudes = [x for x in SC_amplitudes if np.isnan(x) == False]
#     print(amplitudes)
    
    SC_x_generator=[]
    for i in range(len(SC_amplitudes)):
        SC_x_generator.append(i)
#     print(SC_x_generator)
    
    # Site D
    SD = SD_df_T_ycoord.values.tolist()
    
    for i in range(SD_No_T):
        p = [x[i] for x in SD]
    
        for x, y in zip(p[0::],p[1::]): 
            if x > y:
                diff = x - y
                SD_amplitudes.append(diff)

            else:
                diff = y - x
                SD_amplitudes.append(diff)

    SD_amplitudes = [x for x in SD_amplitudes if np.isnan(x) == False]
#     print(amplitudes)
    
    SD_x_generator=[]
    for i in range(len(SD_amplitudes)):
        SD_x_generator.append(i)
#     print(SD_x_generator)
    
    # Site E
    SE = SE_df_T_ycoord.values.tolist()
    
    for i in range(SE_No_T):
        p = [x[i] for x in SE]
    
        for x, y in zip(p[0::],p[1::]): 
            if x > y:
                diff = x - y
                SE_amplitudes.append(diff)

            else:
                diff = y - x
                SE_amplitudes.append(diff)

    SE_amplitudes = [x for x in SE_amplitudes if np.isnan(x) == False]
#     print(amplitudes)

    
    SE_x_generator=[]
    for i in range(len(SE_amplitudes)):
        SE_x_generator.append(i)
#     print(SE_x_generator)
#################################################################################################################    
### Plots    
##
##    # Scatter plot
##    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1,figsize=(16,12), tight_layout=True)
##    ax1.scatter(SA_x_generator,SA_amplitudes)
##    ax2.scatter(SB_x_generator,SB_amplitudes)
##    ax3.scatter(SC_x_generator,SC_amplitudes)
##    ax4.scatter(SD_x_generator,SD_amplitudes)
##    ax5.scatter(SE_x_generator,SE_amplitudes)
##    
##    
##    ax1.set_ylabel('amplitudes (m)',fontsize=22)
##    ax2.set_ylabel('amplitudes (m)',fontsize=22)
##    ax3.set_ylabel('amplitudes (m)',fontsize=22)
##    ax4.set_ylabel('amplitudes (m)',fontsize=22)
##    ax5.set_ylabel('amplitudes (m)',fontsize=22)
##    
##    ax1.set_title('(A)', loc='left',fontsize=22)
##    ax2.set_title('(B)', loc='left',fontsize=22)
##    ax3.set_title('(C)', loc='left',fontsize=22)
##    ax4.set_title('(D)', loc='left',fontsize=22)
##    ax5.set_title('(E)', loc='left',fontsize=22)
##    
##    ax5.set_xlabel('Peak along transect',fontsize=22)
##    plt.xticks(fontsize=14)
##    plt.yticks(fontsize=14)
##    #plt.legend(fontsize=22)
##    plt.show()
##    
##    # Histogram plot
##    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,1,figsize=(20,12),tight_layout=True)
##    ax1.hist(SA_amplitudes,bins = 500,range=[0,25],edgecolor='black', facecolor='gray', alpha=0.6) #Add range=[x,y] to remove outliers typical range 2-8m 
##    ax2.hist(SB_amplitudes,bins = 500,range=[0,25],edgecolor='black', facecolor='gray', alpha=0.6) #Add range=[x,y] to remove outliers typical range 2-8m 
##    ax3.hist(SC_amplitudes,bins = 500,range=[0,25],edgecolor='black', facecolor='gray', alpha=0.6)
##    ax4.hist(SD_amplitudes,bins = 500,range=[0,25],edgecolor='black', facecolor='gray', alpha=0.6)
##    ax5.hist(SE_amplitudes,bins = 500,range=[0,25],edgecolor='black', facecolor='gray', alpha=0.6)
##    
##    ax1.set_ylabel('frequency',fontsize=22)
##    ax2.set_ylabel('frequency',fontsize=22)
##    ax3.set_ylabel('frequency',fontsize=22)
##    ax4.set_ylabel('frequency',fontsize=22)
##    ax5.set_ylabel('frequency',fontsize=22)
##    
##    ax1.set_title('(A)', loc='left',fontsize=22)
##    ax2.set_title('(B)', loc='left',fontsize=22)
##    ax3.set_title('(C)', loc='left',fontsize=22)
##    ax4.set_title('(D)', loc='left',fontsize=22)
##    ax5.set_title('(E)', loc='left',fontsize=22)
##    
##    ax1.xaxis.get_ticklocs(minor=True)
##    ax1.minorticks_on()
##    ax2.xaxis.get_ticklocs(minor=True)
##    ax2.minorticks_on()
##    ax3.xaxis.get_ticklocs(minor=True)
##    ax3.minorticks_on()
##    ax4.xaxis.get_ticklocs(minor=True)
##    ax4.minorticks_on()
##    ax5.xaxis.get_ticklocs(minor=True)
##    ax5.minorticks_on()
##    ax1.set_xlim(0,)
##    ax2.set_xlim(0,)
##    ax3.set_xlim(0,)
##    ax4.set_xlim(0,)
##    ax5.set_xlim(0,)
##    
##    ax1.set_ylim(0,25)
##    ax2.set_ylim(0,25)
##    ax3.set_ylim(0,25)
##    ax4.set_ylim(0,25)
##    ax5.set_ylim(0,25)
##    
##    ax5.set_xlabel('amplitudes (m)',fontsize=22)
##    plt.xticks(fontsize=14)
##    plt.yticks(fontsize=14)
##    #plt.legend(fontsize=22)
##    
##    plt.savefig('/Users/domhardy/Dissertation/Dissertation---Megadunes/Megadune quantification/All Sites extraction amplitudes hist.jpg',dpi=900, transparent=True)
##    plt.savefig('/Users/domhardy/Desktop/Undergrad dissertation/Dissertation Layout - LaTex/Images/All Sites extraction amplitudes hist.jpg',dpi=900, transparent=True)
##    plt.show()

#################################################################################################################       
    # Stats
    
    # Site A
    SEM_amp_SA = sem(SA_amplitudes)
    standard_deviation_amp_SA = np.std(SA_amplitudes)
    print("Site A: ")
    print('Amplitudes mean: ', np.mean(SA_amplitudes),
          'Amplitudes SEM: ', SEM_amp_SA,
          'Amplitudes SD: ', standard_deviation_amp_SA,
          'No. of Amplitudes points: ',len(SA_amplitudes),
          'Q1: ', np.percentile(SA_amplitudes, [25]),
          'Q3: ', np.percentile(SA_amplitudes, [75]),
          'IQR: ', (np.percentile(SA_amplitudes, [75]) - np.percentile(SA_amplitudes, [25])),
          'Lower bound: ', np.percentile(SA_amplitudes, [25]) - (1.5*(np.percentile(SA_amplitudes, [75]) - np.percentile(SA_amplitudes, [25]))),
          'Upper bound: ', np.percentile(SA_amplitudes, [75]) + (1.5*(np.percentile(SA_amplitudes, [75]) - np.percentile(SA_amplitudes, [25]))),
          'min: ', min(SA_amplitudes),
          '10%: ', np.percentile(SA_amplitudes, [10]),
          '90%: ', np.percentile(SA_amplitudes, [90]),
         )
    
    print("")
    
    # Site B
    SEM_amp_SB = sem(SB_amplitudes)
    standard_deviation_amp_SB = np.std(SB_amplitudes)
    print("Site B: ")
    print('Amplitudes mean: ', np.mean(SB_amplitudes),
          'Amplitudes SEM: ', SEM_amp_SB,
          'Amplitudes SD: ', standard_deviation_amp_SB,
          'No. of Amplitudes points: ',len(SB_amplitudes),
          'Q1: ', np.percentile(SB_amplitudes, [25]),
          'Q3: ', np.percentile(SB_amplitudes, [75]),
          'IQR: ', (np.percentile(SB_amplitudes, [75]) - np.percentile(SB_amplitudes, [25])),
          'Lower bound: ', np.percentile(SB_amplitudes, [25]) - (1.5*(np.percentile(SB_amplitudes, [75]) - np.percentile(SB_amplitudes, [25]))),
          'Upper bound: ', np.percentile(SB_amplitudes, [75]) + (1.5*(np.percentile(SB_amplitudes, [75]) - np.percentile(SB_amplitudes, [25]))),
          'min: ', min(SB_amplitudes),
          '10%: ', np.percentile(SB_amplitudes, [10]),
          '90%: ', np.percentile(SB_amplitudes, [90]),
         )
    
    print("")
    
    # Site C
    SEM_amp_SC = sem(SC_amplitudes)
    standard_deviation_amp_SC = np.std(SC_amplitudes)
    print("Site C: ")
    print('Amplitudes mean: ', np.mean(SC_amplitudes),
          'Amplitudes SEM: ', SEM_amp_SC,
          'Amplitudes SD: ', standard_deviation_amp_SC,
          'No. of Amplitudes points: ',len(SC_amplitudes),
          'Q1: ', np.percentile(SC_amplitudes, [25]),
          'Q3: ', np.percentile(SC_amplitudes, [75]),
          'IQR: ', (np.percentile(SC_amplitudes, [75]) - np.percentile(SC_amplitudes, [25])),
          'Lower bound: ', np.percentile(SC_amplitudes, [25]) - (1.5*(np.percentile(SC_amplitudes, [75]) - np.percentile(SC_amplitudes, [25]))),
          'Upper bound: ', np.percentile(SC_amplitudes, [75]) + (1.5*(np.percentile(SC_amplitudes, [75]) - np.percentile(SC_amplitudes, [25]))),
          'min: ', min(SC_amplitudes),
          '10%: ', np.percentile(SC_amplitudes, [10]),
          '90%: ', np.percentile(SC_amplitudes, [90]),
         )
    
    print("")
    
    # Site D
    SEM_amp_SD = sem(SD_amplitudes)
    standard_deviation_amp_SD = np.std(SD_amplitudes)
    print("Site D: ")
    print('Amplitudes mean: ', np.mean(SD_amplitudes),
          'Amplitudes SEM: ', SEM_amp_SD,
          'Amplitudes SD: ', standard_deviation_amp_SD,
          'No. of Amplitudes points: ',len(SD_amplitudes),
          'Q1: ', np.percentile(SD_amplitudes, [25]),
          'Q3: ', np.percentile(SD_amplitudes, [75]),
          'IQR: ', (np.percentile(SD_amplitudes, [75]) - np.percentile(SD_amplitudes, [25])),
          'Lower bound: ', np.percentile(SD_amplitudes, [25]) - (1.5*(np.percentile(SD_amplitudes, [75]) - np.percentile(SD_amplitudes, [25]))),
          'Upper bound: ', np.percentile(SD_amplitudes, [75]) + (1.5*(np.percentile(SD_amplitudes, [75]) - np.percentile(SD_amplitudes, [25]))),
          'min: ', min(SD_amplitudes),
          '10%: ', np.percentile(SD_amplitudes, [10]),
          '90%: ', np.percentile(SD_amplitudes, [90]),
         )
    
    print("")
    
    # Site E
    SEM_amp_SE = sem(SE_amplitudes)
    standard_deviation_amp_SE = np.std(SE_amplitudes)
    print("Site E: ")
    print('Amplitudes mean: ', np.mean(SE_amplitudes),
          'Amplitudes SEM: ', SEM_amp_SE,
          'Amplitudes SD: ', standard_deviation_amp_SE,
          'No. of Amplitudes points: ',len(SE_amplitudes),
          'Q1: ', np.percentile(SE_amplitudes, [25]),
          'Q3: ', np.percentile(SE_amplitudes, [75]),
          'IQR: ', (np.percentile(SE_amplitudes, [75]) - np.percentile(SE_amplitudes, [25])),
          'Lower bound: ', np.percentile(SE_amplitudes, [25]) - (1.5*(np.percentile(SE_amplitudes, [75]) - np.percentile(SE_amplitudes, [25]))),
          'Upper bound: ', np.percentile(SE_amplitudes, [75]) + (1.5*(np.percentile(SE_amplitudes, [75]) - np.percentile(SE_amplitudes, [25]))),
          'min: ', min(SE_amplitudes),
          '10%: ', np.percentile(SE_amplitudes, [10]),
          '90%: ', np.percentile(SE_amplitudes, [90]),
         )

    # Combined list
    all_sites_amp = []
    for i in range(len(SA_amplitudes)):
        a = SA_amplitudes[i]
        all_sites_amp.append(a)
        
    for i in range(len(SB_amplitudes)):
        a = SB_amplitudes[i]
        all_sites_amp.append(a)
        
    for i in range(len(SC_amplitudes)):
        a = SC_amplitudes[i]
        all_sites_amp.append(a)
        
    for i in range(len(SD_amplitudes)):
        a = SD_amplitudes[i]
        all_sites_amp.append(a)
        
    for i in range(len(SE_amplitudes)):
        a = SE_amplitudes[i]
        all_sites_amp.append(a)
        


    #print(all_sites_amp)

    SEM_amp_all_sites = sem(all_sites_amp)
    standard_deviation_amp_all_sites = np.std(all_sites_amp)
    print('Wavelengths mean: ', np.mean(all_sites_amp),
          'Wavelengths SEM: ', SEM_amp_all_sites,
          'Wavelengths SD: ', standard_deviation_amp_all_sites,
          'No. of Wavelength points: ',len(all_sites_amp),
          'Q1: ', np.percentile(all_sites_amp, [25]),
          'Q3: ', np.percentile(all_sites_amp, [75]),
          'Lower bound: ', np.percentile(all_sites_amp, [25]) - (1.5*(np.percentile(all_sites_amp, [75]) - np.percentile(all_sites_amp, [25]))),
          'Upper bound: ', np.percentile(all_sites_amp, [75]) + (1.5*(np.percentile(all_sites_amp, [75]) - np.percentile(all_sites_amp, [25]))),
          'min: ', min(all_sites_amp),
          '10%: ', np.percentile(all_sites_amp, [10]),
          '90%: ', np.percentile(all_sites_amp, [90]),
          )

    df_A_amp = pd.DataFrame(SA_amplitudes, columns=['A'])
    df_B_amp = pd.DataFrame(SB_amplitudes, columns=['B'])
    df_C_amp = pd.DataFrame(SC_amplitudes, columns=['C'])
    df_D_amp = pd.DataFrame(SD_amplitudes, columns=['D'])
    df_E_amp = pd.DataFrame(SE_amplitudes, columns=['E'])

##    amp_df['A'] = SA_amplitudes
##    amp_df['B'] = SB_amplitudes
##    amp_df['C'] = SC_amplitudes
##    amp_df['D'] = SD_amplitudes
##    amp_df['E'] = SE_amplitudes

    df_A_amp = df_A_amp.reset_index()
    df_B_amp = df_B_amp.reset_index()
    df_C_amp = df_C_amp.reset_index()
    df_D_amp = df_D_amp.reset_index()
    df_E_amp = df_E_amp.reset_index()
    
    amp_df = [df_A_amp, df_B_amp, df_C_amp, df_D_amp,df_E_amp]
    
    amp_df_fin = pd.concat(amp_df, axis=1)
    
    amp_df_fin.to_csv('/Users/domhardy/Desktop/amp_df.csv', index=False)
    
    
    # Kruskal-Wallis stats
    
    from scipy import stats

#     print(f"Site A v A : ",{stats.kruskal(SA_amplitudes, SA_amplitudes)}) 
#     print(f"Site A v B : ",{stats.kruskal(SA_amplitudes, SB_amplitudes)}) 
#     print(f"Site A v C : ",{stats.kruskal(SA_amplitudes, SC_amplitudes)})
#     print(f"Site A v D : ",{stats.kruskal(SA_amplitudes, SD_amplitudes)}) 
#     print(f"Site A v E : ",{stats.kruskal(SA_amplitudes, SE_amplitudes)})
    
#     #####
    
#     print(f"Site B v A : ",{stats.kruskal(SB_amplitudes, SA_amplitudes)}) 
#     print(f"Site B v B : ",{stats.kruskal(SB_amplitudes, SB_amplitudes)}) 
#     print(f"Site B v C : ",{stats.kruskal(SB_amplitudes, SC_amplitudes)})
#     print(f"Site B v D : ",{stats.kruskal(SB_amplitudes, SD_amplitudes)}) 
#     print(f"Site B v E : ",{stats.kruskal(SB_amplitudes, SE_amplitudes)})
    
#     #####
    
#     print(f"Site C v A : ",{stats.kruskal(SC_amplitudes, SA_amplitudes)}) 
#     print(f"Site C v B : ",{stats.kruskal(SC_amplitudes, SB_amplitudes)}) 
#     print(f"Site C v C : ",{stats.kruskal(SC_amplitudes, SC_amplitudes)})
#     print(f"Site C v D : ",{stats.kruskal(SC_amplitudes, SD_amplitudes)}) 
#     print(f"Site C v E : ",{stats.kruskal(SC_amplitudes, SE_amplitudes)})
    
#     #####
    
#     print(f"Site D v A : ",{stats.kruskal(SD_amplitudes, SA_amplitudes)})
#     print(f"Site D v B : ",{stats.kruskal(SD_amplitudes, SB_amplitudes)}) 
#     print(f"Site D v C : ",{stats.kruskal(SD_amplitudes, SC_amplitudes)})
#     print(f"Site D v D : ",{stats.kruskal(SD_amplitudes, SD_amplitudes)}) 
#     print(f"Site D v E : ",{stats.kruskal(SD_amplitudes, SE_amplitudes)})
    
#     #####
    
#     print(f"Site E v A : ",{stats.kruskal(SE_amplitudes, SA_amplitudes)})
#     print(f"Site E v B : ",{stats.kruskal(SE_amplitudes, SB_amplitudes)}) 
#     print(f"Site E v C : ",{stats.kruskal(SE_amplitudes, SC_amplitudes)})
#     print(f"Site E v D : ",{stats.kruskal(SE_amplitudes, SD_amplitudes)}) 
#     print(f"Site E v E : ",{stats.kruskal(SE_amplitudes, SE_amplitudes)})

start = time.time()
MD_amplitudes_calc(SA.iloc[:,1::2],25,
                   SB.iloc[:,1::2],25,
                   SC.iloc[:,1::2],37,
                   SD.iloc[:,1::2],50,
                   SE.iloc[:,1::2],51)
time.time()
print("time to run (seconds): ", time.time() - start)


