from mpi4py import MPI
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


# Function for means comparation
def are_means_equals(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if np.array_equal(array1[i], array2[i]) == False:
                return False
        return True
    else:
        return False


def kmeans(dataset, n):
    # ***** Algorithm start *****

    # Define some variables
    ds_dimensions = dataset.shape[1]
    ds_size = dataset.shape[0]

    # Select n random elements from the dataset
    means = []
    for i in range(n):
        means.append(dataset[random.randint(0,ds_size-1)])

    # Loop for defining clusters
    do = True
    new_means = means
    iterations = 0
    while are_means_equals(means, new_means) == False or do:
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

    variances = [np.var(c) for c in clusters]
    average_variance = sum(variances)/len(variances)
    
    return [clusters, average_variance, iterations]


if __name__ == "__main__":
    if rank == 0:
        # Setting up the dataset and number of clusters (n) variable
        n = int(input('Introduce la cantidad de clusters: '))
        # n = 3
        filename = input('Introduce el nombre del archivo con el dataset a utilizar: ')
        csv = pd.read_csv(filename, header=None)
        csv = csv.loc[:, [i for i in range(csv.shape[1]) if ((csv[i].dtype == 'float64' or csv[i].dtype == 'int64'))]]
        # iris = pd.read_csv('/home/fernando-dlz/Documents/python/computo avanzado/multithreading/data/wine.data', header=None)
        print("Archivo cargado exitosamente.")

        cstm_colms = None
        while (cstm_colms != 'si' and cstm_colms != 'no'):
            cstm_colms = input('¿Deseas especificar las columnas del dataset a utilizar (de no ser asi se utilizarán todas las columnas)?: ')
            if cstm_colms == 'si':
                colms = input('Introduce las columnas a utilizar, separadas por coma (ej:1,3,4): ').split(',')
                colms = [int(e) for e in colms]
                print(f"Se utilizaran las columas {colms}")
                dataset = np.array(csv.iloc[:, colms])
            elif cstm_colms == 'no':
                print("Se utilizaran todas las columnas.")
                dataset = np.array(csv.iloc[:, :])
            else:
                print("Respuesta introducida invalida, opciones validas: [si/no]")

        # dataset = np.array(iris.loc[:, 2:3])
        ds_dimensions = dataset.shape[1]

    else:
        dataset = None
        n = 0

    dataset = comm.bcast(dataset, root=0)
    n = comm.bcast(n, root=0)

    result = kmeans(dataset, n)
    results = comm.gather(result, root=0)


    if rank == 0:
        # once all the workers finish its process we find the best result
        clusters_variances = [result[1] for result in results]
        index_best = clusters_variances.index(min(clusters_variances))

        clusters = results[index_best][0]

        print('Numero total de iteraciones antes de la convergencia: ' + str(results[index_best][2]))

        if ds_dimensions == 2 and n==3:
            # Graph designed to work specifically with 3 clusters and 2 dimensions
            plt.scatter(clusters[0][:, 0], clusters[0][:, 1], color='red', alpha=0.5)
            plt.scatter(clusters[1][:, 0], clusters[1][:, 1], color='blue', alpha=0.5)
            plt.scatter(clusters[2][:, 0], clusters[2][:, 1], color='green', alpha=0.5)
            plt.show()
        else:
            for c in clusters:
                print(c)