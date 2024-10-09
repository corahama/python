import numpy as np
import matplotlib.pyplot as plt

from copy import *


class UMDAc:
    def __init__(self, N, a, f, NI, n):
        self.finish = False
        self.hist = []
        self.N = N
        self.a = a
        self.f = f
        self.NI = NI
        self.n = n
        self.P = np.array([self.randI() for i in range(N)])
        self.P = np.array(sorted(self.P, key=f))

    def randI(self, min=-100, max=100):
        return min + max * np.random.rand(self.n)

    def nrandP(self, md, de):
        return np.random.normal(md, de, size=(self.N))

    def media(self, i):
        md = np.sum(self.P[:,i])
        md /= self.N
        return md

    def desv_est(self, i):
        md = self.media(i)
        de = np.sum((self.P[:,i]-md)**2)
        de /= self.N
        return np.sqrt(de)

    def run(self):
        if self.finish:
            return deepcopy(self.hist)
        self.hist.append(np.copy(self.P[0]))
        for n in range(self.NI):
            for i in range(self.n):
                md, de = self.media(i), self.desv_est(i) # + 1/(n+1)
                self.P[self.a:,i] = self.nrandP(md, de)[self.a:]
            self.P = np.array(sorted(self.P, key=f))
            self.hist.append(np.copy(self.P[0]))
        self.finish = True
        return np.array(deepcopy(self.hist))


N = 100
a = 20
n = 3
NI = 100

def f(I):
    return np.sum(I**2)

umdac = UMDAc(N, a, f, NI, n)
hist = umdac.run()
plt.plot(range(len(hist)), hist)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.axes.set_xlim3d([-5.12,5.12])
ax.axes.set_ylim3d([-5.12,5.12])
ax.axes.set_zlim3d([-5.12,5.12])
ax.scatter(hist[:,0], hist[:,1], hist[:,2], c=range(len(hist)))
ax.plot3D(hist[:,0], hist[:,1], hist[:,2])
plt.show()

