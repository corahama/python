from multiprocessing import Pool
import random

import pandas as pd
import numpy as np

from naive_bayes import get_model, classify


bag_itr = 100
# dataset = ""
# cl_col = 0
# ch_cols = 0

dataset = pd.read_csv("datasets/iris.data", header=None).values
cl_col = 4
ch_cols = (0,1,2,3)

# dataset = pd.read_csv("datasets/wine.data", header=None).values
# cl_col = 0
# ch_cols = (1,2,3,4,5,6,7,8,9,10,11,12,13)

# cl_col = 0
# dataset = pd.read_csv("datasets/balance-scale.data", header=None).sort_values(
#             by=cl_col, ignore_index=True).values
# ch_cols = (1,2,3,4)

# dataset = pd.read_csv("datasets/glass.data", header=None).values
# cl_col = 9
# ch_cols = (0,1,2,3,4,5,6,7,8)


# Multiprocessing function to calculate class divisions of chunks
def calc_divs(beginning, final):
    cs_name = dataset[beginning][cl_col]
    divs = []
    for i, e in enumerate(dataset[beginning:final], start=beginning):
        if e[cl_col] != cs_name:
            divs.append(i)
            cs_name = e[cl_col]
    return divs

# Function to calculate dataset class divisions
def get_divs():
    ps = 4
    ds_len = len(dataset)
    ck_size = int(ds_len/ps)
    with Pool(ps) as pool:
        results = [pool.apply_async(calc_divs, args=(i*ck_size, i*ck_size+ck_size if
                    i*ck_size+ck_size <= ds_len else ds_len%ck_size)) for i in range(ps)]
        pool.close()
        pool.join()
    divs = [0]
    for r in results:
        divs += r.get()
    divs.append(ds_len)
    return divs


def main():
    # global dataset, ch_cols, cl_col, bag_itr

    # dataset_str = input("Introducce la ruta del dataset a trabajar: ")
    # ch_cols = input("Introduce las columnas a utilizar, separadas por coma (ej:1,3,4): ").split(',')
    # ch_cols = [int(e) for e in ch_cols]
    # cl_col = int(input("Introduce el indice de la columna de las clases: "))
    # dataset = pd.read_csv(dataset_str, header=None).sort_values(
    #         by=cl_col, ignore_index=True).values
    # bag_itr = int(input("Introduce el numero de muestras bagging: "))

    divs = get_divs()
    print()


    # ***** Setting up training and testing subsets *****
    # Generate random indexes to extract the testing elements from dataset
    testing_items = []
    for i in range(len(divs)-1):
        indexes = []
        while len(indexes) < int((divs[i+1]-divs[i])*.1):
            n = random.randint(divs[i], divs[i+1]-1)
            if n not in indexes: indexes.append(n)
        testing_items.append(indexes)

    # Generate testing subset
    testing_st = []
    for items in testing_items:
        testing_st.append(dataset.take(items, axis=0))
    testing_st = np.array(testing_st)

    # Generate training subset
    training_st = np.delete(dataset, [i for sublist in testing_items for i in sublist], axis=0)
    for i in range(1, len(divs)):
        divs[i] -= sum([len(item) for item in testing_items[0:i]])
    training_st = np.split(training_st, divs[1: len(divs)-1])


    # ***** Configure models *****
    models = []
    for _ in range(bag_itr):
        bagging_st = []
        for cl in training_st:
            indexes = [random.randint(0, cl.shape[0]-1) for _ in range(cl.shape[0])]
            bagging_st.append(cl.take(indexes, axis=0))
        models.append(get_model(bagging_st, ch_cols))


    # ***** Comparations *****
    # With training subset
    print("* Resultados para el subconjunto de entrenamiento")
    total_success = 0
    for cl_i, cl in enumerate(training_st):
        success = 0
        for e in cl:
            votes = {x : 0 for x in range(len(training_st))}
            for b in range(bag_itr):
                votes[classify(e, ch_cols, models[b][0], models[b][1])] += 1
            if max(zip(votes.values(), votes.keys()))[1] == cl_i: success += 1
        total_success += success

        print(f"· class <{cl[0][cl_col]}>: {success}/{cl.shape[0]}")
    print(f"Rendimiento total: {total_success*100/divs[-1]:.2f}%")
    print()

    # With testing subset
    print("* Resultados para el subconjunto de prueba")
    total_success = 0
    for cl_i, cl in enumerate(testing_st):
        success = 0
        for e in cl:
            votes = {x : 0 for x in range(len(testing_st))}
            for b in range(bag_itr):
                votes[classify(e, ch_cols, models[b][0], models[b][1])] += 1
            if max(zip(votes.values(), votes.keys()))[1] == cl_i: success += 1
        total_success += success

        print(f"· class <{cl[0][cl_col]}>: {success}/{cl.shape[0]}")
    print(f"Rendimiento total: {total_success*100/sum([len(elms) for elms in testing_st]):.2f}%")


if __name__ == "__main__":
    main()
