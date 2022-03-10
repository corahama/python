import numpy as np


"""Function to construct model"""
def get_model(training_st, ch_clms):
    model = []
    cl_probs = []
    total_elms = sum(map(lambda e: e.shape[0], training_st))

    # Define dimensions means and standard deviations per class
    for cl in training_st:
        col = []
        for ch_clm in (cl[:, i] for i in range(*ch_clms)):
            di = {'m': np.mean(ch_clm), 'std': np.std(ch_clm)}
            col.append(di)
        model.append(col)

        # Define a priori probability per class
        cl_probs.append(cl.shape[0]/total_elms)

    return model, cl_probs


"""Function to classify an element"""
def classify(e, model, cl_probs):
    probs = []
    for cl_measures, prior in zip(model, cl_probs):
        prt = 1
        for ch_measure, ch in zip(cl_measures, e):
            prt *= (np.exp(-.5*((ch-ch_measure['m'])/ch_measure['std'])**2)/
                    np.sqrt(2*np.pi*ch_measure['std']))
        probs.append(prt*prior)

    return probs.index(max(probs))
