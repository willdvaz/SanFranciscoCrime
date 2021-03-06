
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import csv
import pandas as pd
import sklearn
from sklearn.cluster import KMeans



#import some points of the dataset
print('Loading the data...')
df = pd.read_csv('../data/train.csv')
print('Data Loaded.')
#df = pd.read_csv('../data/train.csv', nrows = 50000)

#LENGTH = 100000
LENGTH =df.size 
print('Pre-processing...\n')
longitudes = df['X'].as_matrix()
latitudes = df['Y'].as_matrix()
#couleurs = ['r' for _ in range(len(latitudes)) ]
#rayons =[30  for _ in range(len(latitudes)) ]
classes = pd.Series(df['Category'], dtype = 'category').cat.categories
nb_classes = len(df['Category'].unique())
# replacing categories by numbers labels
df['Category'] = pd.Series(df['Category'], dtype = 'category').cat.rename_categories(range(nb_classes))

#computes the prototypes of kmeans and add it to latitude and longitude
print('Geographic clustering...')
clus = sklearn.cluster.KMeans(n_clusters = 100)
x_train = df[['X','Y']];
clus.fit(x_train.as_matrix())
clus_long = clus.cluster_centers_[:,0]
clus_lat = clus.cluster_centers_[:,1]
#create the cluster points and add it to the data
new_X = clus.predict(x_train)
df['Clus_loc']=new_X
print('Clustering finished.')


#create vector of colors for the display of the cities
#from random import randint
#colors = []
#for i in range(max(new_X+1)):
#  colors.append("#%06x" % randint(0, 0xFFFFFF))
#couleurs = [ colors[new_X[i]] for i in range(len(x_train))]
#longitudes= np.append(longitudes, clus_long)
#latitudes= np.append(latitudes,clus_lat)
##couleurs = np.append(couleurs, ['b' for _ in range(len(clus_lat)) ])
#rayons =[30  for _ in range(len(clus_lat )) ]

# Crée une projection centrée sur San Francisco
#frame = ((-122.52, 37.68), (-122.38,37.82))
#map = Basemap(
#        llcrnrlon=frame[0][0], llcrnrlat=frame[0][1],
#        urcrnrlon=frame[1][0], urcrnrlat=frame[1][1],
#        epsg=3493)
## Charge le plan associé à la projection
#map.arcgisimage(
#        service='ESRI_StreetMap_World_2D',
#        xpixels = 1000, verbose= True)
## Convertit (long,lat) en position image
#(X,Y)=map(longitudes, latitudes)
# Appel classique aux fonctions matplotlib
#plt.scatter(X, Y, rayons, marker = 'o', color = couleurs,
#        alpha = 0.4)
# Lance l’affichage
#plt.show()



#do the learning with a random forest
execfile('rf.py')
