import matplotlib.pylab as plt
import numpy as np

def animate(self, values, betters, velocities, b_values):
    self.evaluate()

    plt.clf()
    plt.title(f"Sample Graph iteration: {self.iterations}")
    plt.xlim(self.axis_limits)
    plt.ylim(self.axis_limits)
    plt.scatter([p[0] for p in b_values], [p[1] for p in b_values], 20, "k")
    self.iterations += 1

def main():
    values = np.random.randint(-100, 100, size=(10, 2))

    plt.scatter([p[0] for p in values], [p[1] for p in values], 20, "k")
    plt.title("Initial Sample Graph")
    plt.xlabel("X label")
    plt.ylabel("Y label")
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)

    ani = FuncAnimation(plt.gcf(), animate, fargs=(values), interval=100)

    plt.show()

if __name__ == "__main__":
    main()