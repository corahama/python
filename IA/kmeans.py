import random

from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# function for means comparation
def are_means_equals(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if np.array_equal(array1[i], array2[i]) == False:
                return False
        return True
    return False


# function for setting up the clusters asynchronously
def setting_clusters(i):
    clusters = [[] for i in range(n)]
    ds_chunk = dataset[(i-1)*chunks:i*chunks]

    for e in ds_chunk:
        distances = []
        for m in means:
            distances.append(sum([(m[i]-e[i])**2 for i in range(ds_dimensions)]))
        clusters[distances.index(min(distances))].append(e)

    return clusters


# function for setting up the new means asynchronously
def setting_means(c):
    mean = []
    for i in range(ds_dimensions):
        mean.append(sum([point[i] for point in clusters[c]])/len(clusters[c]))
    np.array(mean)

    return mean


# ***** Main code *****
if __name__ == "__main__":
    # Setting up the dataset and number of clusters (n) variable
    n = int(input('Introduce la cantidad de clusters: '))
    # n = 3
    file_path = input('Introduce la ruta del archivo con el dataset a utilizar: ')
    # file_path = 'datasets/iris.data'
    csv = pd.read_csv(file_path, header=None)

    colms = input('Introduce las columnas a utilizar, separadas por coma (ej:1,3,4): ').split(',')
    colms = [int(e) for e in colms]
    # colms = [2,3]
    dataset = np.array(csv.iloc[:, colms])

    ds_size, ds_dimensions = dataset.shape


    # ***** Algorithm start *****

    # Select n random elements from the dataset
    means = []
    for i in range(n):
        means.append(dataset[random.randint(0,ds_size-1)])

    # Loop for defining clusters
    do = True
    new_means = means
    iterations = 0
    chunks = int(ds_size/n)
    while are_means_equals(means, new_means) == False or do:
        means = new_means.copy()
        clusters = [[] for i in range(n)]

        # setting clusters asynchronously
        pool = Pool(n)
        results = []
        results = [pool.apply_async(setting_clusters, args=(i,)) for i in range(1,n+1)]
        pool.close()
        pool.join()
        for r in results:
            c = r.get()
            for i in range(n):
                for e in c[i]:
                    clusters[i].append(e)

        # setting new means asynchronously
        new_means = []
        pool = Pool(n)
        results = [pool.apply_async(setting_means, args=(i,)) for i in range(len(clusters))]
        pool.close()
        pool.join()
        for r in results:
            result = r.get()
            new_means.append(result)

        do = False
        iterations += 1

    for i in range(len(clusters)):
        clusters[i] = np.array(clusters[i])

    print('Numero total de iteraciones antes de la convergencia: ' + str(iterations))

    if ds_dimensions == 2:
        colors = ['green', 'blue', 'red', 'black', 'orange', 'gray']

        # Graph designed to work with 2 dimensions
        for i in range(n) :
            plt.scatter(clusters[i][:, 0], clusters[i][:, 1], color=colors[i%len(colors)], alpha=0.6)
        plt.show()

    else:
        for c in clusters:
            print(c)
