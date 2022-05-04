from multiprocessing import Pool, cpu_count
from functools import reduce

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# parallel function
def compute_clusters(ds, means):
    m_avgs = [[0]*len(ds[0])]*len(means)
    counts = [0]*len(means)

    for e in ds:
        arg_min = np.argmin(tuple(np.linalg.norm(e-mean) for mean in means))
        m_avgs[arg_min] = tuple(map(lambda ch, d_sum: d_sum+ch, e, m_avgs[arg_min]))
        counts[arg_min] += 1

    return m_avgs, counts


def run(dataset, k, plot=False):
    pc = cpu_count()

    means = dataset[np.random.choice(range(0, dataset.shape[0]), size=k, replace=False), :]

    # run algorithm
    last_means, do = [], True
    iterations = 0
    while do or not (last_means == means).all():
        last_means = means.copy()

        with Pool(pc) as pool:
            results = [pool.apply_async(compute_clusters, args=(tuple(map(lambda ft_i:
                dataset[ft_i], range(i, dataset.shape[0], pc))), last_means)) for i in range(pc)]
            pool.close()
            pool.join()

        # for r in (result.get()[0] for result in results):
        #     print(', '.join(map(lambda t: '(' + ', '.join(f'{v:.2f}' for v in t) + ')', r)))

        means = reduce(lambda r_1, r_2: tuple(tuple(map(lambda a, b: a+b, t_1, t_2))
                    for t_1, t_2 in zip(r_1, r_2)), map(lambda r: r.get()[0], results))
        counts = reduce(lambda r_1, r_2: tuple(map(lambda a,b: a+b, r_1, r_2)),
                    map(lambda r: r.get()[1], results))
        means = np.array(tuple(tuple(map(lambda d_m: d_m/c, m)) for m, c in zip(means, counts)))

        iterations += 1
        do = False

    print('Itereaciones antes de la convergencia: ', iterations)

    if plot and dataset.shape[1] == 2:
        colors = ['green', 'blue', 'red', 'black', 'orange', 'purple']

        clusters = [([],[]) for _ in range(k)]
        for e in dataset:
            arg_min = np.argmin(tuple(np.linalg.norm(e-mean) for mean in means))
            clusters[arg_min][0].append(e[0])
            clusters[arg_min][1].append(e[1])

        for i, cluster in enumerate(clusters):
            plt.scatter(cluster[0], cluster[1], color=colors[i%len(colors)], alpha=0.5)
        plt.show()

    return means


if __name__ == '__main__':
    k = 6
    path = 'multithreading/data/wine.data'
    clms = [1,2]
    dataset = pd.read_csv(path, header=None).values[:, clms]

    run(dataset, k, True)
