#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
datatset = pd.read_csv('mall.csv')
X = datatset.iloc[:,[3,4]].values

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++',n_init=10,max_iter=300,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of custers')
plt.ylabel('WCSS')
plt.show()

#Applying K-means to the dataset
kmeans = KMeans(n_clusters=5, init='k-means++',n_init=10,max_iter=300,random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Visualizing the clusters
plt.scatter(X[y_kmeans ==0, 0], X[y_kmeans == 0, 1], s = 50, c= 'red', label = 'Cluster 1: Careful')
plt.scatter(X[y_kmeans ==1, 0], X[y_kmeans == 1, 1], s = 50, c= 'yellow', label = 'Cluster 2: Standard')
plt.scatter(X[y_kmeans ==2, 0], X[y_kmeans == 2, 1], s = 50, c= 'green', label = 'Cluster 3: Target')
plt.scatter(X[y_kmeans ==3, 0], X[y_kmeans == 3, 1], s = 50, c= 'cyan', label = 'Cluster 4L Careless')
plt.scatter(X[y_kmeans ==4, 0], X[y_kmeans == 4, 1], s = 50, c= 'magenta', label = 'Cluster 5: Sensible')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 150, c= 'black', label = 'Centroids')
plt.title('Clusters of clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()