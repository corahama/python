from multiprocessing import Pool
import pandas as pd
import numpy as np
import math

def normilize(vector):
    norm = math.sqrt(sum([i**2 for i in vector]))
    return np.array([e/norm for e in vector])

def get_eta(epoca):
    return 1/(4*math.sqrt(epoca))

def training(data_set, etapas):
    alpha = np.random.rand(data_set[0].shape[1])
    alpha = normilize(alpha)

    correct = 0
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
                else:
                    correct += 1
            set_indicator *= -1

    return (alpha, correct)

def testing(begin, data_Set, step, alpha):
    correct = 0
    for set_data in data_set:
        for i in range(begin, set_data.shape[0], step):
            if np.dot(alpha, set_data[i]) >= 0:
                correct += 1
    return correct

if __name__ == "__main__":
    etapas = 10

    iris = pd.read_csv('/home/fernando-dlz/Documents/python/computo avanzado/multithreading/data/iris.data', header=None)

    # TRAINING
    i_virginicat = np.array(iris.iloc[100:110, [0,1,2,3]])
    i_versicolort = np.array(iris.iloc[50:60, [0,1,2,3]])
    data_set = [i_virginicat, i_versicolort]

    results_test = training(data_set, etapas)
    alpha = results_test[0]
    correct_test = results_test[1]
    print(correct_test)

    # TESTING
    process = 4
    i_virginica = np.array(iris.iloc[110:150, [0,1,2,3]])
    i_versicolor = np.array(iris.iloc[60:100, [0,1,2,3]])
    data_set = [i_virginica, i_versicolor]

    pool = Pool()
    results = [pool.apply_async(testing, args=(i, data_set, process, alpha)) for i in range(process)]
    pool.close()
    pool.join()

    results = [e.get() for e in results]
    print(sum(results))
