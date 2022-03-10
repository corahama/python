import math

import numpy as np


class SRM():
    def __init__(self) -> None:
        self.tc = 0
        self.u = []
        self.spikeTrain = []
        self.V = 6 # mV
        # Eta kernel parameters
        self.eta_0 = 22 # mV
        self.tau_refr = 30 # ms
        # Kappa kernel parameters
        self.R = 36 #mOhms
        self.tau_m = 4 # ms
        self.tau_rec = 30 # ms

    # Response to spike emission
    def kernel_eta(self, lft) -> float:
        s = self.tc - lft

        return -self.eta_0 * math.exp(-s/self.tau_refr) * np.heaviside(s, 0)

    # Response to presynaptic spike incoming activity
    def kernel_epsilon(self, ft_j) -> float:
        return 0

    # Response to incoming external current
    def kernel_kappa(self, lft) -> float:
        s = self.tc - lft

        return (1/self.tau_m) * (math.exp(1 - (s/self.tau_rec))) *  np.heaviside(s, 0)

    def simulate(self, i_ext) -> float:
        tmpU = 0

        for spike in self.spikeTrain:
            tmpU += self.kernel_eta(spike)

        self.u.append(tmpU + i_ext)

        if self.u[-1] >= self.V:
            self.u[-1] = self.V
            self.spikeTrain.append(self.tc)

        return self.u[-1]

    """Run the model within a interval time of 'ts' and return the firing rate"""
    def run(self, i_ext, iterations=500) -> int:
        self.u = []
        self.spikeTrain = []

        ts = np.arange(iterations)
        for i in ts:
            self.tc = i
            self.simulate(i_ext)

        return len(self.spikeTrain)-1

    """Run the model within a interval time of 'ts' and return the firing trace"""
    def get_firing_trace(self, i_ext, iterations=500):
        self.u = []
        self.spikeTrain = []

        ts = np.arange(iterations)
        for i in ts:
            self.tc = i
            self.simulate(i_ext)

        return np.array(self.spikeTrain[1:])


def main():
    import matplotlib.pylab as plt

    # neuron = SRM()

    # print(neuron.get_firing_trace(10.1))
    # print(neuron.run(10.1))
    # plt.plot(np.arange(1000), neuron.u)
    # plt.show()

    ini, end, step = 10, 20, .5
    frs = np.zeros(int((end-ini)/step), dtype='float')
    for i, i_ext in enumerate(np.arange(ini,end,step, dtype='float')):
        frs[i] = SRM().run(i_ext)
        print(f'i_ext({i_ext})={frs[i]}')
    print(np.std(frs))


if __name__ == '__main__':
    main()
