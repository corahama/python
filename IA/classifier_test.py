from multiprocessing import Pool
import random

import pandas as pd
import numpy as np

from naive_bayes import get_model, classify


bag_itr = 1
# dataset = ""
# cl_col = 0

DATASET = pd.read_csv("datasets/iris.data", header=None).values
CL_COL = 4

# DATASET = pd.read_csv("datasets/wine.data", header=None).values
# cl_col = 0

# DATASET = pd.read_csv("datasets/balance-scale.data", header=None).sort_values(
#             by=cl_col, ignore_index=True).values
# cl_col = 0

# DATASET = pd.read_csv("datasets/glass.data", header=None).values
# cl_col = 9


# Multiprocessing function to calculate class divisions of chunks
def calc_divs(beginning, final):
    cs_name = DATASET[beginning][CL_COL]
    divs = []
    for i, e in enumerate(DATASET[beginning:final], start=beginning):
        if e[CL_COL] != cs_name:
            divs.append(i)
            cs_name = e[CL_COL]
    return divs

# Function to calculate dataset class divisions
def get_divs():
    ps = 4
    ds_len = len(DATASET)
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
    # global dataset, ch_cols, CL_COL, bag_itr

    # dataset_str = input("Introducce la ruta del dataset a trabajar: ")
    # CL_COL = int(input("Introduce el indice de la columna de las clases: "))
    # dataset = pd.read_csv(dataset_str, header=None).sort_values(
    #         by=CL_COL, ignore_index=True).values
    # bag_itr = int(input("Introduce el numero de muestras bagging: "))

    ch_cols = (1, DATASET.shape[1]) if CL_COL == 0 else (0, DATASET.shape[1]-1)
    divs = get_divs()


    # ***** Setting up training and testing subsets *****
    # Generate random indexes to extract the testing elements from dataset
    testing_item_idxs = []
    rng = np.random.default_rng()
    for i in range(len(divs)-1):
        indexes = rng.choice(np.arange(divs[i],divs[i+1]), int((divs[i+1]-divs[i])*.1), replace=False)
        testing_item_idxs.append(indexes)

    # Generate testing subset
    testing_st = []
    for indexes in testing_item_idxs:
        testing_st.append(DATASET[indexes, :])
    testing_st = np.array(testing_st)

    # Generate training subset
    training_st, sumation = np.delete(DATASET, np.concatenate(testing_item_idxs), axis=0), 0
    for i in range(len(divs)-1):
        sumation += testing_item_idxs[i].shape[0]
        divs[i+1] -= sumation
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
                votes[classify(e[ch_cols[0]:ch_cols[1]], models[b][0], models[b][1])] += 1
            if max(zip(votes.values(), votes.keys()))[1] == cl_i: success += 1
        total_success += success

        print(f"· class <{cl[0][CL_COL]}>: {success}/{cl.shape[0]}")
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
                votes[classify(e[ch_cols[0]:ch_cols[1]], models[b][0], models[b][1])] += 1
            if max(zip(votes.values(), votes.keys()))[1] == cl_i: success += 1
        total_success += success

        print(f"· class <{cl[0][CL_COL]}>: {success}/{cl.shape[0]}")
    print(f"Rendimiento total: {total_success*100/sum([len(elms) for elms in testing_st]):.2f}%")


if __name__ == "__main__":
    main()
