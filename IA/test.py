import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# iris = pd.read_csv('/home/fernando/Documents/ai/iris.data', header=None)

# print(iris)

def f(x,y):
    return y + x

b = np.fromfunction(f, (3,3), dtype=int)
print(b[2,2])
