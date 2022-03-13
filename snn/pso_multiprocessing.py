import sys
from multiprocessing import Pool, cpu_count

import numpy as np
import matplotlib.pyplot as plt



class PSO():
    def __init__(self, dataset, ch_cols, sn_model, max_iters=50, max_vel=.2):
        # Defining initial constants
        self.dataset = dataset # n dimentional numpy array
        self.ch_cols = ch_cols # first and last characteristic columns
        self.ch_size = ch_cols[1] - ch_cols[0]
        # self.search_space = search_space
        self.max_iters = max_iters
        self.max_vel = max_vel
        self.population = 30
        self.c1, self.c2 = .0205, .0205

        # Processes
        self.proc = cpu_count()

        # SN Model
        self.sn_model = sn_model

        # Definition of the initial random values and the initial best set
        self.swarm = np.random.rand(self.population, self.ch_size)
        self.velocities = np.random.rand(self.population, self.ch_size)
        # for i in range(self.population):
        #     for j in range(0 if i%2 == 0 else 1, self.ch_size, 2):
        #         self.swarm[i,j] = -self.swarm[i,j]
        #         self.velocities[i,j] = -self.velocities[i,j]
        self.sw_best = self.swarm.copy()

        self.sw_best_fitnesses = np.zeros(self.population, dtype='float')
        pool = Pool(self.proc)
        results = [pool.apply_async(self.prll_fitness, args=(i,)) for i in range(self.proc)]
        pool.close()
        pool.join()
        for r in results:
            for i, p_fitness in r.get():
                self.sw_best_fitnesses[i] = p_fitness

        self.global_idx = 0

        # Array to track the algorithm evolution
        self.history = np.zeros(self.max_iters, dtype='float')

    """Runs the evolutive algorithm"""
    def run(self):
        for iteration in range(self.max_iters):
            # Configuring and executing pool
            pool = Pool(self.proc)
            results = [pool.apply_async(self.prll_fitness, args=(i,)) for i in range(self.proc)]
            pool.close()
            pool.join()

            # Evaluate actual swarm fitnesses vs best ones
            for r in results:
                for i, p_fitness in r.get():
                    if p_fitness < self.sw_best_fitnesses[i]:
                        self.sw_best_fitnesses[i] = p_fitness
                        self.sw_best[i] = self.swarm[i]
            self.global_idx = np.argmin(self.sw_best_fitnesses)

            # Update velocity and position for each particle
            for i, vel in enumerate(self.velocities):
                self.velocities[i] = vel + np.random.rand(self.ch_size)*self.c1*(
                        self.sw_best[i]-self.swarm[i]) + np.random.rand(self.ch_size)*self.c2*(
                        self.sw_best[self.global_idx]-self.swarm[i])
                for j, vel_dim in enumerate(self.velocities[i]):
                    if abs(vel_dim) > self.max_vel:
                        vel[j] = self.max_vel * vel_dim/abs(vel_dim)

                self.swarm[i] = self.swarm[i] + self.velocities[i]

            self.history[iteration] = self.sw_best_fitnesses[self.global_idx]
            print(f'iteration {iteration+1}: {self.sw_best_fitnesses[self.global_idx]}')

        plt.plot(range(self.max_iters), self.history)
        plt.savefig('w_evolution_history.png')

        return self.sw_best[self.global_idx], self.history

    """Function excecuted by each process in pool"""
    def prll_fitness(self, ini):
        return [(i, self.fitness_func(self.swarm[i])) for i in range(ini, self.population, self.proc)]

    """Objective function for evolutive process"""
    def fitness_func(self, values):
        afr = np.zeros(len(self.dataset), dtype='float')
        sdfr = np.zeros(len(self.dataset), dtype='float')

        # For each class
        for cl_idx, cl in enumerate(self.dataset):
            firing_rates = np.zeros(cl.shape[0], dtype='float')

            # For each element
            for i, e in enumerate(cl):
                firing_rates[i] = self.sn_model.run(np.dot(e[self.ch_cols[0]:self.ch_cols[1]], values))

            afr[cl_idx] = np.mean(firing_rates)
            sdfr[cl_idx] = np.std(firing_rates)

        # Calculate dist(AFR)
        dis_afr = 0.0
        for i in range(afr.shape[0]):
            for j in range(i, afr.shape[0]):
                dis_afr += abs(afr[j]-afr[i])

        return sys.maxsize if dis_afr == 0 else 1/dis_afr + sum(sdfr)


def main():
    import pandas as pd
    import matplotlib.pyplot as plt

    from pr_neuron import get_divs
    from bms import BMS
    from srm import SRM


    dataset = pd.read_csv('datasets/iris.data', header=None).values
    cl_clm = 4
    ch_clms = (1, dataset.shape[1]) if cl_clm == 0 else (0, dataset.shape[1]-1)
    cl_divs = get_divs(dataset, cl_clm)
    dataset = np.split(dataset, cl_divs[1: len(cl_divs)-1])

    sn_model = BMS()
    # sn_model = SRM()

    best, history = PSO(dataset, ch_clms, sn_model).run()
    print('[', ', '.join(map(str, best)), ']')
    plt.plot(range(history.shape[0]), history, c='b')
    plt.show()


if __name__ == "__main__":
    main()
