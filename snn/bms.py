from numpy import array as np_array
from numpy import arange

class BMS():
    # Optimal parameters: gamma=.68, theta=7
    def __init__(self, gamma=0.7, theta=10):
        self.gamma = gamma
        self.theta = theta

    def run(self, i_ext):
        fr = -1
        vt = 0
        for _ in range(100):
            vt = self.gamma*vt*(1-(0 if vt < self.theta else 1)) + i_ext
            if vt == i_ext:
                fr += 1

        return fr

    def get_firing_trace(self, i_ext):
        fires_raster = []
        vt = 0
        for t in range(100):
            vt = self.gamma*vt*(1-(0 if vt < self.theta else 1)) + i_ext
            if vt == i_ext:
                fires_raster.append(t)

        fires_raster = np_array(fires_raster[1:])
        return fires_raster

    def get_voltage_trace(self, i_ext):
        vt_trace = arange(100, dtype='float')

        vt = 0
        for t in range(100):
            vt_trace[t] = vt
            vt = self.gamma*vt*(1-(0 if vt < self.theta else 1)) + i_ext

        return vt_trace                


# i_ext > (1-gamma)*theta
def main():
    import numpy as np

    frs = np.zeros(12, dtype='float')

    for i, i_ext in enumerate(np.arange(4,10,.5, dtype='float')):
        frs[i] = BMS().run(i_ext)
        print(f'i_ext({i_ext})={frs[i]}')

    print('standar deviation:', np.std(frs))


def graph_bms():
    import matplotlib.pyplot as plt
    import numpy as np

    v = BMS().get_voltage_trace(3.1)
    t = np.arange(1, v.shape[0]+1)

    plt.plot(t, v)
    plt.show()


if __name__ == '__main__':
    # main()
    graph_bms()