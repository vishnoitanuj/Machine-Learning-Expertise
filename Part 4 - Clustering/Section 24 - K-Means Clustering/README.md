# K-Means Clustering

Step 1: Choose the number K of clusters
Step 2: Select at random K points, the centroids (not necessarily from your datatset)
Step 3: Assign each data point to the closest centroid that forms K clusters.
Step 4: Compute and place the new centroid of each cluster.
Step 5: Reassign each data point to the new closest centroid. If any reassignment took place, go to STEP 4, otherwise go to FINISH. 

#### Note: A random initialization of centroids can lay a trap, that forms incorrect/bad clusters. Thus, selection of centroid at start matters a lot.

## Selecting number of clusters

The elbow method help select the optimum change, when the changes drop slowly.