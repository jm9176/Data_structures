'''
K-means clustering for a random data input of 1000 points
The code returns 3 cluster regions, with the list of data
points stored un list_k1, list_k2, and list_k3 respectively

Variable diff_k1, diff_k2, diff_k3 calculates the distance
between the previous and the new centroid value. These
variables acts as a condition for the iteration of the outer
loop of the kmeans_clust function if the value of all the
variable goes below 0.001.
'''

import numpy as np
import matplotlib.pyplot as plt

# Calculating the euclidean distance
def dist(point1, point2):
    return pow(pow(point1[0]-point2[0],2) + pow(point1[1]-point2[1],2), 0.5)

# Updating the centroid value using the old and new value
def upd_cent(curr_cent, n, new_pt):
    temp_sum_x = (curr_cent[0])*(n+1)
    temp_sum_y = (curr_cent[1])*(n+1)

    new_pt_x = (temp_sum_x + new_pt[0])/(n+2)
    new_pt_y = (temp_sum_y + new_pt[1])/(n+2)

    return (new_pt_x, new_pt_y)

# Function inserting the points into different clusters
def kmeans_clust(dataSet, k):

    # List storing the set of updated centroids
    cent = []
    list_k1, list_k2, list_k3 = [], [], []

    # Generating the random centroids for a given num of clusters
    for i in range(k):
        x = np.random.uniform(0,10)
        y = np.random.uniform(0,10)
        cent.append((x,y))

    # Finding the minimum distance between the two randomly generated centroids
    k1 = cent[0]
    k2 = cent[1]
    k3 = cent[2]
    diff_k1, diff_k2, diff_k3 = np.inf, np.inf, np.inf

    # Condition to stop the iteration if the centroid update
    # distance for all the clusters is below 0.001 units
    while diff_k1 > 0.001 and diff_k2 > 0.001 and diff_k3 >0.001:

        # Iterating for the entire dataset
        for i in range(len(dataSet)):
            dist_k1 = dist(dataSet[i], k1)
            dist_k2 = dist(dataSet[i], k2)
            dist_k3 = dist(dataSet[i], k3)

            # Condition to update the current centroid value
            # by comparing with the distance value of the current
            # point from the other clusters
            if dist_k1 < dist_k2 and dist_k1 < dist_k3:
                prev_k1 = k1
                k1 = upd_cent(k1, len(list_k1), dataSet[i])
                list_k1.append(dataSet[i])

                # Removing dataSet[i] from list_k2 and list_k3,
                # if in both the lists from previous iterations
                if dataSet[i] in list_k2:
                    list_k2.remove(dataSet[i])

                if dataSet[i] in list_k3:
                    list_k3.remove(dataSet[i])

                diff_k1 = dist(prev_k1, k1)

            elif dist_k2 < dist_k1 and dist_k2 < dist_k3:
                prev_k2 = k2
                k2 = upd_cent(k2, len(list_k2), dataSet[i])
                list_k2.append(dataSet[i])
                if dataSet[i] in list_k1:
                    list_k1.remove(dataSet[i])
                if dataSet[i] in list_k3:
                    list_k3.remove(dataSet[i])

                diff_k2 = dist(prev_k2, k2)

            elif dist_k3 < dist_k1 and dist_k3 < dist_k2:
                prev_k3 = k3
                k3 = upd_cent(k3, len(list_k3), dataSet[i])
                list_k3.append(dataSet[i])
                if dataSet[i] in list_k1:
                    list_k1.remove(dataSet[i])
                if dataSet[i] in list_k2:
                    list_k2.remove(dataSet[i])

                diff_k3 = dist(prev_k3, k3)

    # Plotting the final data poitns for each cluster
    for i in range(len(list_k1)):
        plt.plot(list_k1[i][0], list_k1[i][1], marker = 'o', color = 'darkred', markersize = 3)

    for i in range(len(list_k2)):
        plt.plot(list_k2[i][0], list_k2[i][1], marker = 'o', color = 'darkgrey', markersize = 3)

    for i in range(len(list_k3)):
        plt.plot(list_k3[i][0], list_k3[i][1], marker = 'o', color = 'darkorange', markersize = 3)


# Taking a set of 2000 random data points
dataSet = [(np.random.uniform(0,10), np.random.uniform(0,10)) for k in range(2000)]
plt.figure()
plt.axis([0,10,0,10])
kmeans_clust(dataSet, 3)
plt.show()
