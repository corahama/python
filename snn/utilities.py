from multiprocessing import Pool, cpu_count
from math import ceil


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
