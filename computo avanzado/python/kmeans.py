import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Function for means comparation
def are_means_equal(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if np.array_equal(array1[i], array2[i]) == False:
                return False
        return True
    else:
        return False


# Seting up the dataset and number of clusters (n) variable
n = int(input('Introduce la cantidad de clusters: '))
iris = pd.read_csv('iris.data', header=None)
dataset = np.array(iris.loc[:, 0:1])
ds_dimensions = dataset.shape[1]
ds_size = dataset.shape[0]


# ***** Algorithm start *****

# Select n random elements from the dataset
means = []
for i in range(n):
    means.append(dataset[random.randint(0,149)])

# Loop for defining clusters
do = True
new_means = means
iterations = 0
while are_means_equal(means, new_means) == False or do:
    means = new_means.copy()
    clusters = [[] for i in range(n)]

    for e in dataset:
        distances = []
        for m in means:
            distances.append(sum([(m[i]-e[i])**2 for i in range(ds_dimensions)]))
        clusters[distances.index(min(distances))].append(e)

    new_means = []
    for c in clusters:
        mean = []
        for i in range(ds_dimensions):
            mean.append(sum([point[i] for point in c])/len(c))
        new_means.append(np.array(mean))
    
    do = False
    iterations += 1
    
for i in range(len(clusters)):
    clusters[i] = np.array(clusters[i])
    
print('Numero total de iteraciones antes de la convergencia: ' + str(iterations))

if ds_dimensions == 2 and n==3:
    # Graph designed to work specifically with 3 clusters and 2 dimensions
    plt.scatter(clusters[0][:, 0], clusters[0][:, 1], color='red', alpha=0.5)
    plt.scatter(clusters[1][:, 0], clusters[1][:, 1], color='blue', alpha=0.5)
    plt.scatter(clusters[2][:, 0], clusters[2][:, 1], color='green', alpha=0.5)
    plt.show()
else:
    for c in clusters:
        print(c)