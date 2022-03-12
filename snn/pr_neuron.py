from multiprocessing import Pool, cpu_count
from math import ceil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pso_multiprocessing import PSO
from bms import BMS
from srm import SRM

# Global variables
# DATASET = pd.read_csv('datasets/iris.data', header=None).values
# CL_CLM = 4

DATASET = pd.read_csv('datasets/wine.data', header=None).values
CL_CLM = 0


"""Function excecuted by each process in pool to calculate class divisions"""
def calc_divs(ds, cl_clm, beginning, ck_size):
    divs = []
    cl_name = ds[beginning, cl_clm]
    for i, e in enumerate(ds[beginning:beginning+ck_size], start=beginning):
        if e[cl_clm] != cl_name:
            divs.append(i)
            cl_name = e[cl_clm]

    return divs

"""Function to calculate dataset class divisions"""
def get_divs(ds, cl_clm):
    ps = cpu_count()
    ds_len = len(ds)
    ck_size = ceil(ds_len/ps)

    with Pool(ps) as pool:
        results = [pool.apply_async(calc_divs, args=(ds, cl_clm, i*ck_size, ck_size 
                    if (i+1)*ck_size <= ds_len else ds_len%ck_size)) for i in range(ps)]
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
    # CL_CLM = int(input("Introduce el indice de la columna de clases: "))
    # DATASET = pd.read_csv(dataset_str, header=None).sort_values(by=CL_CLM, ignore_index=True).values

    ch_cols = (1, DATASET.shape[1]) if CL_CLM == 0 else (0, DATASET.shape[1]-1)
    divs = get_divs(DATASET, CL_CLM)
    # sn_model = BMS()
    sn_model = SRM()

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
    testing_st = np.array(testing_st, dtype='object')

    # Generate training subset
    training_st, summation = np.delete(DATASET, np.concatenate(testing_item_idxs), axis=0), 0
    for i in range(len(divs)-1):
        summation += testing_item_idxs[i].shape[0]
        divs[i+1] -= summation
    training_st = np.split(training_st, divs[1: len(divs)-1])

    del testing_item_idxs, indexes, rng, summation, divs


    # ***** Configure model *****
    weights, _ = PSO(training_st, ch_cols, sn_model).run()
    print(weights)
    # weights = [0.3037256,  0.10523379, 0.69746353, 0.8838105 ] # iris
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

            # Graph firing trace
            plt.scatter(firing_trace, np.full(firing_trace.shape[0], cl_track+i, dtype='int'),
                        c=colors[cl_idx%len(colors)], s=10)

        cl_track += cl.shape[0]
        afr[cl_idx] = np.mean(firing_rates)
    # plt.show()
    plt.savefig('firing_trace.png')

    del cl_track, firing_trace, colors, firing_rates


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
                    dis = abs(afr[i]-fr)

            if arg_min_idx == cl_idx: accuracy += 1

        total_accuracy += accuracy
        print(f'· Class \'{e[CL_CLM]}\': {accuracy}/{cl.shape[0]}')
    print(f'Total accuracy: {100*total_accuracy/sum([cl.shape[0] for cl in training_st]):.2f}%')

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
                    dis = abs(afr[i]-fr)


            if arg_min_idx == cl_idx: accuracy += 1

        print(f'· Class \'{e[CL_CLM]}\': {accuracy}/{cl.shape[0]}')
        total_accuracy += accuracy
    print(f'Total accuracy: {100*total_accuracy/sum([cl.shape[0] for cl in testing_st]):.2f}%')

    return


if __name__ == '__main__':
    main()
