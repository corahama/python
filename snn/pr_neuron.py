from datetime import datetime
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# from pso import PSO
from pso_multiprocessing import PSO
from utilities import get_divs, norm_ch, save, get_path
from bms import BMS
from srm import SRM


# Global variables
PATH = 'datasets/iris.data'
CL_CLM = 4

# PATH = 'datasets/wine.data'
# CL_CLM = 0


def main(save_results=False):
    if save_results:
        start_time = datetime.now().strftime('%H:%M:%S')

    # global PATH, CL_CLM
    # PATH = input("Introducce la ruta del dataset a trabajar: ")
    # CL_CLM = int(input("Introduce el indice de la columna de clases: "))
    dataset = pd.read_csv(PATH, header=None).sort_values(by=CL_CLM, ignore_index=True).values

    ch_clms = (1, dataset.shape[1]) if CL_CLM == 0 else (0, dataset.shape[1]-1)
    divs = get_divs(dataset, CL_CLM)

    # norm_ch(dataset, ch_clms)

    sn_model = BMS()
    # sn_model = SRM()

    assert 'get_firing_trace' in dir(sn_model), 'La clase para el modelo neuronal tiene que \
implementar el metodo \'get_firing_trace\''
    assert 'run' in dir(sn_model), 'La clase para el modelo neuronal tiene que implementar \
el metodo \'run\''

    # ***** Setting up training and testing subsets *****
    # Generate random indeces to extract the testing elements from dataset
    testing_item_idcs = []
    for i in range(len(divs)-1):
        idcs = np.random.choice(np.arange(divs[i],divs[i+1]), int((divs[i+1]-divs[i])*.1), False)
        testing_item_idcs.append(idcs)

    # Generate testing subset
    testing_st = []
    for idcs in testing_item_idcs:
        testing_st.append(dataset[idcs, :])
    testing_st = np.array(testing_st, dtype='object')

    # Generate training subset
    training_st, summation = np.delete(dataset, np.concatenate(testing_item_idcs), axis=0), 0
    for i in range(len(divs)-1):
        summation += testing_item_idcs[i].shape[0]
        divs[i+1] -= summation
    training_st = np.split(training_st, divs[1: len(divs)-1])

    del testing_item_idcs, idcs, summation, divs


    # ***** Configure model *****
    weights, _ = PSO(training_st, ch_clms, sn_model, save_plot=save_results).run()
    # weights = [0.3037256,  0.10523379, 0.69746353, 0.8838105 ] # iris
    # weights = [1.03399134, 0.73495792, 0.86025217, 1.71217792, 0.69568314, 0.3161272,
    # 1.37551808, 0.91079394, 0.69921659, 1.00514106, 0.40010956, 1.26970743, 0.8569052] # wine
    print('weights =', weights, end=' - ')

    afr = np.empty(len(training_st), dtype=np.float64)

    if save_results:
        cl_track = 1
        colors = ['red', 'blue', 'green', 'black', 'orange', 'brown', 'yellow']
        plt.clf()
        # Compute average firing rates and plot firing trace
        for cl_idx, cl in enumerate(training_st):
            firing_rates = np.empty(cl.shape[0], dtype=np.float64)

            # For each element
            for i, e in enumerate(cl):
                fi_trace = sn_model.get_firing_trace(np.dot(e[ch_clms[0]:ch_clms[1]], weights))
                firing_rates[i] = fi_trace.shape[0]

                # Graph firing trace
                plt.scatter(fi_trace, np.full(fi_trace.shape[0], cl_track+i, dtype=np.int16),
                            c=colors[cl_idx%len(colors)], s=2)

            cl_track += cl.shape[0]
            afr[cl_idx] = np.mean(firing_rates)

        plt.savefig(get_path('firing_trace.png'))

        del cl_track, fi_trace, colors

    else:
        # Compute average firing rates
        for cl_idx, cl in enumerate(training_st):
            firing_rates = np.empty(cl.shape[0], dtype=np.float64)

            # For each element
            for i, e in enumerate(cl):
                firing_rates[i] = sn_model.run(np.dot(e[ch_clms[0]:ch_clms[1]], weights))

            afr[cl_idx] = np.mean(firing_rates)

    print('afr =', afr)

    del firing_rates


    # ***** Comparations *****
    # With training subset
    tr_results_str = '\n****Training Subset Results****'
    total_accuracy = 0
    for cl_idx, cl in enumerate(training_st):
        accuracy = 0

        for e in cl:
            # fr = sn_model.run(np.dot(e[ch_cols[0]:ch_cols[1]], weights))
            np_dot = np.dot(e[ch_clms[0]:ch_clms[1]], weights)
            fr = sn_model.run(np_dot)

            arg_min_idx, dis = 0, abs(afr[0]-fr)
            for i in range(1, afr.shape[0]):
                if abs(afr[i]-fr) < dis:
                    arg_min_idx = i
                    dis = abs(afr[i]-fr)

            if arg_min_idx == cl_idx: accuracy += 1

        total_accuracy += accuracy
        tr_results_str += f'\n· Class \'{e[CL_CLM]}\': {accuracy}/{cl.shape[0]}'
    tr_results_str += f'\nTotal accuracy: \
                        {100*total_accuracy/sum([cl.shape[0] for cl in training_st]):.2f}%'
    print(tr_results_str, end="")

    # With testing subset
    te_results_str = '\n****Testing Subset Results****'
    total_accuracy = 0
    for cl_idx, cl in enumerate(testing_st):
        accuracy = 0

        for e in cl:
            fr = sn_model.run(np.dot(e[ch_clms[0]:ch_clms[1]], weights))

            arg_min_idx, dis = 0, abs(afr[0]-fr)
            for i in range(1, afr.shape[0]):
                if abs(afr[i]-fr) < dis:
                    arg_min_idx = i
                    dis = abs(afr[i]-fr)

            if arg_min_idx == cl_idx: accuracy += 1

        total_accuracy += accuracy
        te_results_str += f'\n· Class \'{e[CL_CLM]}\': {accuracy}/{cl.shape[0]}'
    te_results_str += f'\nTotal accuracy: \
                        {100*total_accuracy/sum([cl.shape[0] for cl in testing_st]):.2f}%'
    print(te_results_str)

    if save_results:
        save(start_time=start_time, dataset=re.search(r'/(\S+\.\S+$)', PATH).group(1),
            sn_model=sn_model.__class__.__name__, weights=weights, afr=afr,
            training_results=tr_results_str, testing_results=te_results_str,
            finish_time=datetime.now().strftime('%H:%M:%S'))

    return


if __name__ == '__main__':
    main(save_results=False)
