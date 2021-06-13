import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import math

def normilize(vector):
    norm = math.sqrt(sum([i**2 for i in vector]))
    return np.array([e/norm for e in vector])

def get_eta(epoca):
    return 1/(4*math.sqrt(epoca))

def predict(row, weights):
	# activation = weights[0]
	activation = -1
	for i in range(len(row)):
		activation += weights[i] * row[i]
	return 1.0 if activation >= 0.0 else 0.0
 
if __name__ == "__main__":
    etapas = 10

    iris = pd.read_csv('/home/fernando-dlz/Documents/python/computo avanzado/multithreading/data/iris.data', header=None)

    # TRAINING    
    i_virginicat = np.array(iris.iloc[100:110, [2,3]])
    i_versicolort = np.array(iris.iloc[50:60, [2,3]])

    plt.scatter([data[0] for data in i_virginicat], [data[1] for data in i_virginicat], 20, "k")
    plt.scatter([data[0] for data in i_versicolort], [data[1] for data in i_versicolort], 20, "r")
    # plt.show()

    data_set = [i_virginicat, i_versicolort]

    alpha = np.random.rand(data_set[0].shape[1])
    alpha = normilize(alpha)

    for etapa in range(1, etapas+1):
        eta = get_eta(etapa)
        set_indicator = -1
        for set_data in data_set:
            for z in set_data:
                v = 1 if np.dot(alpha, z) > 0 else -1
                if v != set_indicator:
                    m = -1 if np.dot(alpha, z) >= 0 else 1
                    alpha = alpha + eta*m*z
                    alpha = normilize(alpha)
            set_indicator *= -1

    print(alpha)
    # alpha = np.array([0.37010417, -0.92899026])

    for set_data in data_set:
        for z in set_data:
            print(np.dot(alpha, z))


    plt.plot(alpha)
    # plt.show()
