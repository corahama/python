import math

import numpy as np


class SRM():
    def __init__(self) -> None:
        # self.tc = 0
        self.u = []
        self.spikeTrain = []
        self.V = 9 # mV -> best = {iris: 4, wine: 500, norm: 5}
        # Eta kernel parameters
        self.eta_0 = 22 # mV -> best = {iris: 22, wine: 20, norm: 5}
        self.tau_refr = 30 # ms -> best = {iris: 30, wine: 20, norm: 30}
        # Kappa kernel parameters
        # self.R = 36 #mOhms -> unused attribute
        self.tau_m = 4 # ms
        self.tau_rec = 30 # ms

    # Response to spike emission
    def kernel_eta(self, tc, lft) -> float:
        s = tc - lft

        return -self.eta_0 * math.exp(-s/self.tau_refr) * np.heaviside(s, 0)

    # Response to presynaptic spike incoming activity
    def kernel_epsilon(self, ft_j) -> float:
        return 0

    # Response to incoming external current
    def kernel_kappa(self, tc, lft) -> float:
        s = tc - lft

        return (1/self.tau_m) * (math.exp(1 - (s/self.tau_rec))) *  np.heaviside(s, 0)

    """Run the model within a interval time of 'ts' and return the firing rate"""
    def run(self, i_ext, iterations=500) -> int:
        self.u = []
        self.spikeTrain = []

        for tc in range(iterations):
            tmpU = 0

            for spike in self.spikeTrain:
                tmpU += self.kernel_eta(tc, spike)

            self.u.append(tmpU + i_ext)

            if self.u[-1] >= self.V:
                self.u[-1] = self.V
                self.spikeTrain.append(tc)

        return len(self.spikeTrain)-1

    def get_firing_trace(self, i_ext):
        self.run(i_ext)
        return np.array(self.spikeTrain[1:], dtype=np.float64)


def main():
    import time

    neuron = SRM()

    start = time.time()

    ini, end, step = 0, 26, .5
    frs = np.empty(int((end-ini)/step), dtype=np.float64)
    for i, i_ext in enumerate(np.arange(ini,end,step, dtype=np.float64)):
        frs[i] = neuron.run(i_ext)
        print(f'i_ext({i_ext}) = {frs[i]}')
    print('std: ', np.std(frs))

    end = time.time()

    print('Total time:', end-start)

if __name__ == '__main__':
    main()
