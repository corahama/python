import pandas as pd
import numpy as np

from utils import get_divs, norm_features


DATASET = pd.read_csv('datasets/iris.data', header=None).values
CL_CLM = 4

# DATASET = pd.read_csv('datasets/wine.data', header=None).values
# CL_CLM = 0

FE_CLMS = (1, DATASET.shape[1]) if CL_CLM == 0 else (0, DATASET.shape[1]-1)
DIVS = get_divs(DATASET, CL_CLM)


"""Function to compute feature means by class, and the summation of them"""
def compute_fe_means():
    summation_list = []
    for i in range(len(DIVS)-1):
        summation = 0
        print(f'Results for class \'{DATASET[DIVS[i], CL_CLM]}\': ', end='')
        for j in range(*FE_CLMS):
            mean = DATASET[DIVS[i]:DIVS[i+1], j].mean()
            summation += mean
            print(f'{mean:.2f}-', end='')
        summation_list.append(summation)
        print(f'Total: {summation:.2f}')

    return summation_list

"""Function to compute weights of feature means in global summation"""
def compute_weights(summation_list):
    for i, s in zip(range(len(DIVS)-1), summation_list):
        print(','.join(f'{(DATASET[DIVS[i]:DIVS[i+1], j].mean()/s):.3f}' for j
            in range(*FE_CLMS)))


def main():
    summation_list = compute_fe_means()
    compute_weights(summation_list)

    norm_features(DATASET, FE_CLMS)
    summation_list = compute_fe_means()
    compute_weights(summation_list)

    # norm_features(DATASET, FE_CLMS)
    # for i in range(len(DIVS)-1):
    #     print(f'class: {DATASET[DIVS[i]][CL_CLM]}')
    #     for e in (DATASET[e_idx] for e_idx in range(DIVS[i], DIVS[i+1])):
    #         print(np.dot(e[FE_CLMS[0]:FE_CLMS[1]], [1]*(FE_CLMS[1]-FE_CLMS[0])))


if __name__ == '__main__':
    main()
