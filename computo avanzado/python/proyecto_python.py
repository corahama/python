import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

class pso_algorithm():
    def __init__(self, dimentions, particles, fitness_function, max_velocity=10):
        # DEFINING INITIAL CONSTANTS
        self.dimentions = dimentions
        self.particles = particles
        self.fitness_function = fitness_function
        self.max_velocity = max_velocity
        self.p_space = (-100, 100)
        self.axis_limits = (-100, 100)
        self.iterations = 0
        self.c1, self.c2 = 2.05, 2.05
        self.g = None

        # DEFINITION OF THE INITIAL RANDOM VALUES AND THE INITIAL BETTER SET
        self.values = np.random.randint(self.p_space[0], self.p_space[1], size=(self.particles, self.dimentions))
        self.betters = np.array([self.fitness_function(value) for value in self.values])
        self.velocities = np.random.rand(self.particles, self.dimentions)
        self.b_values = self.values.copy()

        if self.dimentions == 2:
            # CREATION AND STYLING OF THE CHART
            plt.scatter([p[0] for p in self.b_values], [p[1] for p in self.b_values], 20, "k")
            plt.title("Initial PSO Algotithm")
            plt.xlabel("X label")
            plt.ylabel("Y label")
            plt.xlim(self.axis_limits)
            plt.ylim(self.axis_limits)

            # SETING  THE FUNC ANIMATION FUNCTION
            self.ani = FuncAnimation(plt.gcf(), self.animate, interval=100)
            plt.show()
        else:
            for _ in range(self.dimentions*1000):
                self.evaluate()
                print(f'iteracion {self.iterations}: {self.betters[self.g]}')
                self.iterations += 1
            print(f'{self.betters[self.g]} | {self.b_values[self.g]}')


    def animate(self, i):
        self.evaluate()

        plt.clf()
        plt.title(f"PSO Iteration: {i}")
        plt.xlim(self.axis_limits)
        plt.ylim(self.axis_limits)
        plt.scatter([p[0] for p in self.b_values], [p[1] for p in self.b_values], 20, "k")

        if np.max(self.b_values) - np.min(self.b_values) == 0:
            self.ani.event_source.stop()


    def evaluate(self):
        newp_evaluated = np.array([self.fitness_function(value) for value in self.values])

        for i in range(len(newp_evaluated)):
            if newp_evaluated[i] < self.betters[i]:
                self.betters[i] = newp_evaluated[i]
                self.b_values[i] = self.values[i]
        self.g = np.argmin(self.betters)

        for i in range(len(self.velocities)):
            self.velocities[i] = self.velocities[i] + np.random.rand(self.dimentions)*self.c1*(self.b_values[i]-self.values[i]) + np.random.rand(self.dimentions)*self.c2*(self.b_values[self.g]-self.values[i])
            for e in range(self.velocities.shape[1]):
                if abs(self.velocities[i][e]) > self.max_velocity:
                    self.velocities[i][e] = 0

        for i in range(len(self.values)):
            self.values[i] = self.values[i] + self.velocities[i]


def fitness_function(particle):
    return sum([coord**2 for coord in particle])

def main():
    # 2 DIMENTIONS
    pso1 = pso_algorithm(2, 1000, fitness_function, max_velocity=20)
    # 10 DIMENTIONS
    # pso2 = pso_algorithm(10, 1000, fitness_function)
    # 50 DIMENTIONS
    # ps3 = pso_algorithm(50, 100, fitness_function)
    # 100 DIMENTIONS
    # pso4 = pso_algorithm(100, 100, fitness_function)

if __name__ == "__main__":
    main()
