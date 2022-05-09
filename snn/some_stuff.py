import pandas as pd

from utilities import get_divs, norm_ch


def main():
    dataset = pd.read_csv('datasets/iris.data', header=None).values
    cl_clm = 4

    # dataset = pd.read_csv('datasets/wine.data', header=None).values
    # cl_clm = 0

    ch_clms = (1, dataset.shape[1]) if cl_clm == 0 else (0, dataset.shape[1]-1)
    divs = get_divs(dataset, cl_clm)

    summation_list = []
    for i in range(len(divs)-1):
        summation = 0
        print(f'Results for class \'{dataset[divs[i], cl_clm]}\': ', end='')
        for j in range(*ch_clms):
            mean = dataset[divs[i]:divs[i+1], j].mean()
            summation += mean
            print(f'{mean:.2f}-', end='')
        summation_list.append(summation)
        print(f'Total: {summation:.2f}')

    for i in range(len(divs)-1):
        print(','.join(f'{(dataset[divs[i]:divs[i+1], j].mean()/summation_list[i]):.3f}' for j
            in range(*ch_clms)))

    norm_ch(dataset, ch_clms)

    summation_list = []
    for i in range(len(divs)-1):
        summation = 0
        print(f'Results for class \'{dataset[divs[i], cl_clm]}\': ', end='')
        for j in range(*ch_clms):
            mean = dataset[divs[i]:divs[i+1], j].mean()
            summation += mean
            print(f'{mean:.2f}-', end='')
        summation_list.append(summation)
        print(f'Total: {summation:.2f}')

    for i in range(len(divs)-1):
        print(','.join(f'{(dataset[divs[i]:divs[i+1], j].mean()/summation_list[i]):.3f}' for j
            in range(*ch_clms)))


if __name__ == '__main__':
    main()
