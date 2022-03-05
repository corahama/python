import math

import numpy as np
import matplotlib.pylab as plt
from sklearn.metrics import det_curve

from timer_clock import TimerClock


class SRM:
    def __init__(self, tc) -> None:
        self.tc = tc
        self.u = []
        self.spikeTrain = []
        self.V = 10 # mV
        # Eta kernel parameters
        self.eta_0 = 22 # mV
        self.tau_refr = 30 # ms
        # Kappa kernel parameters
        self.R = 36 #mOhms
        self.tau_m = 4 # ms
        self.tau_rec = 30 # ms

    # Response to spike emission
    def kernel_eta(self, lft) -> float:
        s = self.tc() - lft

        return -self.eta_0 * math.exp(-s/self.tau_refr) * np.heaviside(s, 0)

    # Response to presynaptic spike incoming activity
    def kernel_epsilon(self, ft_j) -> float:
        return 0

    # Response to incoming external current
    def kernel_kappa(self, lft) -> float:
        s = self.tc() - lft

        return (1/self.tau_m) * (math.exp(1 - (s/self.tau_rec))) *  np.heaviside(s, 0)

    def simulate(self, i_ext) -> float:
        tmpU = 0

        for spike in self.spikeTrain:
            tmpU += self.kernel_eta(spike)

        self.u.append(tmpU + i_ext)

        if self.u[-1] >= self.V:
            self.u[-1] = self.V
            self.spikeTrain.append(self.tc())

        return self.u[-1]


def external_input(t_ini=0, t_end=1000, delta_t=1) -> float:
    tmp = t_ini

    while tmp < t_end:
        v = 10.1 if tmp >= 0 and tmp < 1000 else 0
        yield v
        tmp += delta_t


def main():
    timsim = TimerClock()
    neuron = SRM(timsim.get_t)

    mv = []
    ts = []
    for i, ext in zip(timsim.timming(), external_input()):
        ts.append(i)
        neuron.simulate(ext)

    print(neuron.spikeTrain)
    plt.plot(ts, neuron.u)
    plt.show()


if __name__ == '__main__':
    main()
