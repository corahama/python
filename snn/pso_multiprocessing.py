from multiprocessing import Pool, cpu_count

import numpy as np

from pso import PSO


class PSOMultiprocessing(PSO):
    def __init__(self, dataset, ch_clms, sn_model, iters=50, save_plot=False):
        super().__init__(dataset, ch_clms, sn_model, iters, save_plot, pc=cpu_count())

    """Function to set the initial best fitnesses"""
    def set_fitnesses(self):
        sw_best_fitnesses = np.empty(self.population, dtype=np.float64)

        pool = Pool(self.pc)
        results = [pool.apply_async(self.prll_fitness, args=(i,)) for i in range(self.pc)]
        pool.close()
        pool.join()

        for result in (r.get() for r in results):
            for i, p_fitness in result:
                sw_best_fitnesses[i] = p_fitness

        return sw_best_fitnesses

    """Function to compare fitnesses of the actual swarm population vs historically best ones"""
    def update_best_particles(self):
        # Configuring and executing pool
        pool = Pool(self.pc)
        results = [pool.apply_async(self.prll_fitness, args=(i,)) for i in range(self.pc)]
        pool.close()
        pool.join()

        # Compare actual swarm fitnesses vs best ones
        for result in (r.get() for r in results):
            for i, p_fitness in result:
                if p_fitness < self.sw_best_fitnesses[i]:
                    self.sw_best_fitnesses[i] = p_fitness
                    self.sw_best[i] = self.swarm[i]

        return

    """Function excecuted by each process in pool"""
    def prll_fitness(self, ini):
        return [(i, self.fit_func(self.swarm[i])) for i in range(ini, self.population, self.pc)]


def main():
    import pandas as pd
    import matplotlib.pyplot as plt

    from utilities import get_divs, norm_ch
    from bms import BMS
    from srm import SRM


    dataset = pd.read_csv('datasets/iris.data', header=None).values
    cl_clm = 4
    ch_clms = (1, dataset.shape[1]) if cl_clm == 0 else (0, dataset.shape[1]-1)
    norm_ch(dataset, ch_clms)

    cl_divs = get_divs(dataset, cl_clm)
    dataset = np.split(dataset, cl_divs[1: len(cl_divs)-1])

    sn_model = BMS()
    # sn_model = SRM()

    best, history = PSOMultiprocessing(dataset, ch_clms, sn_model).run()
    print('[', ', '.join(map(str, best)), ']')
    plt.plot(range(history.shape[0]), history, c='b')
    plt.show()


if __name__ == "__main__":
    main()
