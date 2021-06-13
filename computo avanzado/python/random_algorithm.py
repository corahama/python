import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import math

# FITNESS FUNCTION
# f(x,y) = x^2+y^y

axis_limits = (-100, 100)
max_velocity = 1
iterations = 0
c1, c2 = 2.05, 2.05

def fitness_function(particle):
    p_evaluated = 0
    for coord in particle:
        p_evaluated += coord**2
    print(f'{particle} | {p_evaluated}')
    return p_evaluated


def evaluate():
    global values
    newp_evaluated = np.array([fitness_function(value) for value in values])

    global b_values
    for i in range(len(newp_evaluated)):
        if newp_evaluated[i] < betters[i]:
            betters[i] = newp_evaluated[i]
            b_values[i] = values[i]

    global g
    g = np.argmin(betters)

    global velocities
    for i in range(len(velocities)):
        velocities[i] = velocities[i] + np.random.rand(2)*c1*(
            b_values[i]-values[i]) + np.random.rand(2)*c2*(b_values[g]-values[i])

        print(velocities[i])

        for e in range(velocities.shape[1]):
            if abs(velocities[i][e]) > 20:
                velocities[i][e] = 0
                print('special', velocities[i])

    for i in range(len(values)):
        values[i] = values[i] + velocities[i]

    print('')


def animate(i):
    evaluate()

    global iterations
    plt.clf()
    plt.title(f"Sample Graph iteration: {iterations}")
    plt.xlim(axis_limits)
    plt.ylim(axis_limits)
    plt.scatter([p[0] for p in b_values], [p[1] for p in b_values], 20, "k")
    iterations += 1


def main():
    # DEFINITION OF THE INITIAL RANDOM VALUES AND THE INITIAL BETTER SET
    global values
    values = np.random.randint(-100, 100, size=(50, 2))
    global betters
    betters = np.array([fitness_function(value) for value in values])
    global velocities
    velocities = np.random.rand(50, 2)
    global b_values
    b_values = values.copy()

    # CREATION AND STYLING OF THE CHART
    plt.scatter([p[0] for p in b_values], [p[1] for p in b_values], 20, "k")
    plt.title("Initial Sample Graph")
    plt.xlabel("X label")
    plt.ylabel("Y label")
    plt.xlim(axis_limits)
    plt.ylim(axis_limits)
    # plt.savefig(f"image")

    # SETING  THE FUNCANIMATION FUNTCION
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()


if __name__ == "__main__":
    main()


# def evaluate():
#     new_values = get_values()

#     index = 0
#     for i in range(new_values.shape[1]):
#         if (new_values[0][i]**2+new_values[1][i]**2) < betters[index]:
#             values[0][i], values[1][i] = new_values[0][i], new_values[1][i]
#         index += 1

#     set_betters()
#     better_index = np.argmin(betters)
