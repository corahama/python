from multiprocessing import Pool, cpu_count
from math import ceil
from os.path import exists
from os import mkdir
from datetime import date


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


"""Function to normalize characteristics in dataset"""
def norm_ch(dataset, ch_clms):
    for j in range(*ch_clms):
        min_val, max_val = min(dataset[:, j]), max(dataset[:, j])
        diff = max_val - min_val
        for i in range(dataset.shape[0]):
            dataset[i][j] = (dataset[i][j]-min_val)*10/diff


"""Function to generate path for result files"""
def get_path(filename):
    if not exists('results/'):
        mkdir('results/')

    num = 1
    today = date.today()
    file_path = lambda: f'results/{today.strftime("%m-%d-%y")}\
{f"({num})" if num > 1 else ""} {filename}'

    while exists(file_path()):
        num += 1

    return file_path()

"""Function to save results into a file"""
def save(**kwargs):

    with open(get_path('data.txt'), 'w', encoding='utf-8') as f:
        for key, value in kwargs.items():
            f.write(f'{key}: {value}\n\n')

    return


if __name__ == '__main__':
    import pandas as pd

    name = 'fernando'
    age = 25
    hobbies = ['programming', 'read', 'gym']

    di = {'degree': 'IT', 'languages': ['python', 'js', 'java']}

    save(name=name, age=age, hobbies=hobbies, **di)


    # dataset = pd.read_csv('datasets/iris.data', header=None).values
    # cl_clm = 4

    # ch_clms = (1, dataset.shape[1]) if cl_clm == 0 else (0, dataset.shape[1]-1)

    # norm_ch(dataset, ch_clms)
