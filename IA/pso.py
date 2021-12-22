import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class PSO():
    def __init__(self, dimentions, particles, fitness_function, max_iters=200, max_velocity=10):
        # Defining initial constants
        self.dimentions = dimentions
        self.particles = particles
        self.fitness_function = fitness_function
        self.max_velocity = max_velocity
        self.search_space = (-100, 100)
        self.max_iters = max_iters
        self.c1, self.c2 = 2.05, 2.05
        self.g_index = None

        # Definition of the initial random values and the initial better set
        self.values = np.random.randint(self.search_space[0], self.search_space[1],
            size=(self.particles, self.dimentions))
        self.betters = np.array([self.fitness_function(value) for value in self.values])
        self.velocities = np.random.rand(self.particles, self.dimentions)
        self.b_values = self.values.copy()

        if self.dimentions == 2:
            # Chart creation and styling
            plt.scatter([p[0] for p in self.b_values], [p[1] for p in self.b_values], 20, "k")
            plt.title("Initial PSO Algotithm")
            plt.xlabel("X label")
            plt.ylabel("Y label")
            plt.xlim(self.search_space)
            plt.ylim(self.search_space)

            # Setting the func animation function
            self.ani = FuncAnimation(plt.gcf(), self.animate, interval=100)
            plt.show()
        else:
            for i in range(max_iters):
                self.evaluate()
                print(f'iteracion {i+1}: {self.betters[self.g_index]}')
            print(f'{self.betters[self.g_index]} | {self.b_values[self.g_index]}')

    def evaluate(self):
        new_p_evaluated = np.array([self.fitness_function(value) for value in self.values])

        # evaluate current fitness vs best ones
        for i, e in enumerate(new_p_evaluated):
            if e < self.betters[i]:
                self.betters[i] = e
                self.b_values[i] = self.values[i]
        self.g_index = np.argmin(self.betters)

        # update velocity for each partcle
        for i, vel in enumerate(self.velocities):
            self.velocities[i] = vel + np.random.rand(self.dimentions)*self.c1*(
                    self.b_values[i]-self.values[i]) + np.random.rand(self.dimentions
                    )*self.c2*(self.b_values[self.g_index]-self.values[i])
            for j, vel_d in enumerate(self.velocities[i]):
                if vel_d > self.max_velocity:
                    vel[j] = self.max_velocity
                elif vel_d < -self.max_velocity:
                    vel[j] = -self.max_velocity

        # update position for each partcle
        for i, e in enumerate(self.values):
            self.values[i] = e + self.velocities[i]

    def animate(self, i):
        self.evaluate()

        plt.clf()
        plt.title(f"PSO Iteration: {i}")
        plt.xlim(self.search_space)
        plt.ylim(self.search_space)
        plt.scatter([p[0] for p in self.values], [p[1] for p in self.values], 20, "k")

        if i > self.max_iters:
            self.ani.event_source.stop()


def sphere_function(particle):
    return sum([coord**2 for coord in particle])

def rastrigin_function(particle):
    return 10*len(particle) + sum([coord**2-10*math.cos(2*math.pi*coord) for coord in particle])


def main():
    # 2 DIMENTIONS
    PSO(2, 1000, rastrigin_function)
    # 10 DIMENTIONS
    # PSO(10, 1000, rastrigin_function)
    # 50 DIMENTIONS
    # PSO(50, 100, sphere_function)
    # 100 DIMENTIONS
    # PSO(100, 100, sphere_function)


if __name__ == "__main__":
    main()
