import pandas as pd

from pr_neuron import get_divs


def main():
    # dataset = pd.read_csv('datasets/iris.data', header=None).values
    # cl_clm = 4

    dataset = pd.read_csv('datasets/wine.data', header=None).values
    cl_clm = 0

    ch_clms = (1, dataset.shape[1]) if cl_clm == 0 else (0, dataset.shape[1]-1)

    divs = get_divs(dataset, cl_clm)

    # for i in range(len(divs)-1):
    #     print(f'Results for class \'{dataset[divs[i], -1]}\': ', end='')
    #     print('-'.join(f'{dataset[divs[i]:divs[i+1], j].mean():.2f}' for j in range(dataset.shape[1]-1)))


    for i in range(len(divs)-1):
        summation = 0
        print(f'Results for class \'{dataset[divs[i], cl_clm]}\': ', end='')
        for j in range(*ch_clms):
            mean = dataset[divs[i]:divs[i+1], j].mean()
            summation += mean
            print(f'{mean:.2f}-', end='')
        print(f'{summation:.2f}')



if __name__ == '__main__':
    main()
