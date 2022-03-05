from multiprocessing import Pool

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pso import PSO
from bms import BMS
# from srm import SRM

# Global variables
DATASET = pd.read_csv('datasets/iris.data', header=None).values
CL_COL = 4


"""Multiprocessing function to calculate class divisions in pool chunks"""
def calc_divs(beginning, ck_size):
    divs = []
    cs_name = DATASET[beginning, CL_COL]
    for i, e in enumerate(DATASET[beginning:beginning+ck_size], start=beginning):
        if e[CL_COL] != cs_name:
            divs.append(i)
            cs_name = e[CL_COL]

    return divs

"""Function to calculate dataset class divisions"""
def get_divs():
    ps = 4
    ds_len = len(DATASET)
    ck_size = int(ds_len/ps) + 1

    with Pool(ps) as pool:
        results = [pool.apply_async(calc_divs, args=(i*ck_size, ck_size if (i+1)*ck_size <= ds_len
                    else ds_len%ck_size)) for i in range(ps)]
        pool.close()
        pool.join()

    divs = [0]
    for r in results:
        divs += r.get()
    divs.append(ds_len)

    return divs


def main():
    # global DATASET
    # dataset_str = input("Introducce la ruta del dataset a trabajar: ")
    # cl_col = int(input("Introduce el indice de la columna de clases: "))
    # DATASET = pd.read_csv(dataset_str, header=None).sort_values(by=cl_col, ignore_index=True).values

    ch_cols = (1, DATASET.shape[1]) if CL_COL == 0 else (0, DATASET.shape[1]-1)
    divs = get_divs()
    sn_model = BMS()
    # sn_model = SRM()


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
    training_st = np.delete(DATASET, np.concatenate(testing_item_idxs), axis=0)
    sumation = 0
    for i in range(len(divs)-1):
        sumation += testing_item_idxs[i].shape[0]
        divs[i+1] -= sumation
    training_st = np.split(training_st, divs[1: len(divs)-1])


    # ***** Configure model *****
    weights, history = PSO(training_st, ch_cols).run()
    # weights = [0.46156209, 0.74311844, 0.75337077, 0.33797425]
    afr = np.zeros(len(training_st), dtype='float')

    # For each class
    cl_track = 1
    colors = ['red', 'blue', 'green', 'black', 'orange', 'brown', 'yellow']
    for cl_idx, cl in enumerate(training_st):
        firing_rates = np.zeros(cl.shape[0], dtype='float')

        # For each element
        for i, e in enumerate(cl):
            firing_trace = sn_model.get_firing_trace(np.dot(e[ch_cols[0]:ch_cols[1]], weights))
            firing_rates[i] = firing_trace.shape[0]

            # Graph firing track
            plt.scatter(firing_trace, np.full(firing_trace.shape[0], cl_track+i, dtype='int'),
                        c=colors[cl_idx%len(colors)], s=10)

        cl_track += cl.shape[0]
        afr[cl_idx] = np.mean(firing_rates)

    # plt.show()

    # ***** Comparations *****
    # With training subset
    print('\n****Training Subset Results****')
    total_accuracy = 0
    for cl_idx, cl in enumerate(training_st):
        accuracy = 0

        for e in cl:
            fr = sn_model.run(np.dot(e[ch_cols[0]:ch_cols[1]], weights))

            arg_min_idx, dis = 0, abs(afr[0]-fr)
            for i in range(1, afr.shape[0]):
                if abs(afr[i]-fr) < dis: 
                    arg_min_idx = i
                    dis = afr[i]-fr

            if arg_min_idx == cl_idx: accuracy += 1

        total_accuracy += accuracy
        print(f'· Class \'{e[CL_COL]}\': {accuracy}/{cl.shape[0]}')
    print(f'Total accuracy: {total_accuracy/sum([cl.shape[0] for cl in training_st]):.2f}%')

    # With testing subset
    print('\n****Testing Subset Results****')
    total_accuracy = 0
    for cl_idx, cl in enumerate(testing_st):
        accuracy = 0

        for e in cl:
            fr = sn_model.run(np.dot(e[ch_cols[0]:ch_cols[1]], weights))

            arg_min_idx, dis = 0, abs(afr[0]-fr)
            for i in range(1, afr.shape[0]):
                if abs(afr[i]-fr) < dis:
                    arg_min_idx = i
                    dis = afr[i]-fr


            if arg_min_idx == cl_idx: accuracy += 1

        print(f'· Class \'{e[CL_COL]}\': {accuracy}/{cl.shape[0]}')
        total_accuracy += accuracy
    print(f'Total accuracy: {total_accuracy/sum([cl.shape[0] for cl in testing_st]):.2f}%')

    return 0


if __name__ == '__main__':
    main()
