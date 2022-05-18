from sys import maxsize

import numpy as np
import matplotlib.pyplot as plt

from utilities import get_path


class PSO():
    def __init__(self, dataset, ch_clms, sn_model, iters=50, save_plot=False, **kwargs):
        # Defining initial constants
        self.dataset = dataset # n dimentional numpy array
        self.ch_clms = ch_clms # first and last characteristic columns
        self.ch_size = ch_clms[1] - ch_clms[0]
        # self.search_space = search_space
        self.iters = iters
        self.max_vel = .2
        self.population = 50
        self.c1, self.c2 = .0205, .0205
        self.save_plot = save_plot

        # SN Model
        self.sn_model = sn_model

        # Update instance attributes with passed kwargs
        self.__dict__.update(kwargs)

        # Definition of the initial random values and the initial best set
        self.swarm = np.random.rand(self.population, self.ch_size)
        self.velocities = np.random.rand(self.population, self.ch_size)
        # for i in range(self.population):
        #     for j in range(0 if i%2 == 0 else 1, self.ch_size, 2):
        #         self.swarm[i,j], self.velocities[i,j] = -self.swarm[i,j], -self.velocities[i,j]
        self.sw_best = self.swarm.copy()
        self.sw_best_fitnesses = np.array([self.fit_func(p) for p in self.swarm]
            ) if not hasattr(self, 'set_fitnesses') else self.set_fitnesses()
        self.global_idx = 0

        # Array to track the evolution of the algorithm
        self.history = np.empty(self.iters, dtype=np.float64)

    """Runs the evolutive algorithm"""
    def run(self):
        for iteration in range(self.iters):
            # Compare actual swarm fitnesses vs best ones
            self.update_best_particles()

            # Update best global
            self.global_idx = np.argmin(self.sw_best_fitnesses)

            # Update velocity and position for each particle
            for i, vel in enumerate(self.velocities):
                self.velocities[i] = vel + np.random.rand(self.ch_size)*self.c1*(
                        self.sw_best[i]-self.swarm[i]) + np.random.rand(self.ch_size)*self.c2*(
                        self.sw_best[self.global_idx]-self.swarm[i])
                for j, vel_dim in enumerate(self.velocities[i]):
                    if abs(vel_dim) > self.max_vel:
                        vel[j] = self.max_vel * vel_dim/abs(vel_dim)

                position = self.swarm[i] + self.velocities[i]
                # for j, pos_dim in enumerate(position):
                #     if pos_dim > 1:
                #         position[j] = 1
                #     elif pos_dim < 0:
                #         position[j] = 0
                self.swarm[i] = position

            self.history[iteration] = self.sw_best_fitnesses[self.global_idx]
            print(f'iteration {iteration+1}: {self.sw_best_fitnesses[self.global_idx]}')

        if self.save_plot:
            plt.plot(range(self.iters), self.history)
            plt.savefig(get_path('w_evolution_history.png'))

        return self.sw_best[self.global_idx], self.history

    """Function to compare fitnesses of the actual swarm population vs historically best ones"""
    def update_best_particles(self):
        for i, p in enumerate(self.swarm):
            p_fitness = self.fit_func(p)
            if p_fitness < self.sw_best_fitnesses[i]:
                self.sw_best_fitnesses[i] = p_fitness
                self.sw_best[i] = p

        return

    """Objective function for evolutive process"""
    def fit_func(self, vals):
        afr = np.empty(len(self.dataset), dtype=np.float64)
        sdfr = np.empty(len(self.dataset), dtype=np.float64)

        # For each class
        for cl_idx, cl in enumerate(self.dataset):
            fi_rates = np.empty(cl.shape[0], dtype=np.float64)

            # For each element
            for i, e in enumerate(cl):
                fi_rates[i] = self.sn_model.run(np.dot(e[self.ch_clms[0]:self.ch_clms[1]], vals))

            afr[cl_idx] = np.mean(fi_rates)
            sdfr[cl_idx] = np.std(fi_rates)

        # Calculate dist(AFR)
        afr = np.sort(afr)
        dis_afr = 0.0
        for i in range(afr.shape[0]-1):
            dis_afr += afr[i+1]-afr[i]

        return maxsize if dis_afr == 0 else 1/dis_afr + sum(sdfr)


def main():
    import pandas as pd
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

    best, history = PSO(dataset, ch_clms, sn_model).run()
    print('[', ', '.join(map(str, best)), ']')
    plt.plot(range(history.shape[0]), history, c='b')
    plt.show()


if __name__ == "__main__":
    main()
