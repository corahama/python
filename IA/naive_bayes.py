import math

import numpy as np


# Function to construct model
def get_model(training_st, ch_cols):
    model = []
    cl_probs = []
    total_elms = sum([len(st) for st in training_st])

    # Define dimensions means and standard deviations per class
    for cl in training_st:
        col = []
        for i in ch_cols:
            di = {}
            di["m"] = np.mean(cl[:, i])
            di["d"] = np.std(cl[:, i])
            col.append(di)
        model.append(col)

        # Define a priori probability per class
        cl_probs.append(cl.shape[0]/total_elms)

    return model, cl_probs


# Function to classify an element
def classify(e, ch_cols, model, cl_probs):
    probs = []
    for c in range(len(model)):
        prt = 1
        for jm, j in enumerate(ch_cols):
            prt *= (math.pow(math.e, -.5*((e[j]-model[c][jm]["m"])/model[c][jm]["d"])**2)/
                    math.sqrt(2*math.pi*model[c][jm]["d"]))
        probs.append(prt*cl_probs[c])

    return probs.index(max(probs))
