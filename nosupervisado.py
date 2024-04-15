#metodo no supervisado con algoritmo Kmeans
#import pandas as 
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.cluster import KMeans

#ponemos nuestros datos para X y para Y
Data = ('x'|[25,28,30,27,25,26,30,29,26,25,27,28,29,30,29],
        'y'|[1,2,1,3,5,1,2,3,1,1,4,2,5,3,1])

#asignamos al dataframe 
df = DataFrame(Data,columns = ['x','y'])

#creamos variable 
KMeans = KMeans(n_clusters=3).fit(df)
centroid = KMeans.cluster_centers_

print(centroid)

#realizamos la grafica para traer X y Y, especificamos que lo que definimos sea flotante
plt.scatter(df['x'], df['y'], c=KMeans.labels_.astype(float), s=50, alpha=0.5)

#definimos graficas para que agrege valores y color, tamaño del punto
plt.scatter(centroid[:,0], centroid[:,1], c='red', s=50)

#mostramos los centroides en nuestra grafica
plt.show()

