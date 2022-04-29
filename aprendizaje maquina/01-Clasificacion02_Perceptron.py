from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def evaluate_perceptron_rule(X_set, y, W):
    tmp = (np.dot(W, np.transpose(X_set)) >= 0).astype(int)
    tmp = (tmp == y).astype(int)            
    tmp = sum(tmp)

    return tmp

def perceptron_algorithm (Xtr_set, ytr, epoch = 100, learning_rate = 1.0, W = None):
    n_samp = np.size(Xtr_set,0)
    n_feat = np.size(Xtr_set,1)
    W = np.random.uniform(-0.5, 0.5, size = n_feat) if W is None else np.copy(W)    
    e = 0
    Wchange = 0

    for e in range(epoch):
        Wchange = 0
        rnd_order = np.random.permutation(n_samp)
        for index in rnd_order:
            y_out = 1 if np.dot(Xtr_set[index], W) >= 0 else 0            
            deltaW = learning_rate * (ytr[index] - y_out) * Xtr_set[index]            
            W += deltaW
            Wchange = Wchange + 1 if ytr[index] != y_out else Wchange                
        #plot_hyperplane(Xtr_set, ytr, W[0:2], W[2])
        if Wchange == 0:
            break

    return True if Wchange == 0 else False, e, W 

def pocket_algorithm (Xtr_set, ytr, epoch = 100, learning_rate = 1.0, W = None):
    n_samp = np.size(Xtr_set,0)
    n_feat = np.size(Xtr_set,1)
    W = np.random.uniform(-0.5, 0.5, size = n_feat) if W is None else np.copy(W)    
    Ws = W
    hs = 0
    e = 0

    for e in range(epoch):        
        rnd_order = np.random.permutation(n_samp)    
        for index in rnd_order:
            y_out = 1 if np.dot(Xtr_set[index], W) >= 0 else 0            
            deltaW = learning_rate * (ytr[index] - y_out) * Xtr_set[index]            
            W += deltaW   
            if y_out != ytr[index]:
                tmp = evaluate_perceptron_rule(Xtr_set,ytr,W)
                if tmp > hs:
                    hs = tmp
                    Ws = np.copy(W)
            if hs == n_samp:
                break
        #plot_hyperplane(Xtr_set, ytr, W[0:2], W[2])                         

    return True if hs == n_samp else False, e, Ws     

def plot_hyperplane(X, y, W, b):
    slope = - W[0]/W[1]
    intercept = - b/W[1]
    x_hyperplane = np.linspace(min(X[:,0]),max(X[:,0]),10)
    y_hyperplane = slope * x_hyperplane + intercept
    plt.figure(figsize=(8,6))
    plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Spectral)
    plt.plot(x_hyperplane, y_hyperplane, '-')
    plt.title("Dataset and fitted decision hyperplane")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()    

#Cargar dataset
iris = load_iris()

#Caracteristicas a cargar
feat = [2,3]

#Se seleccionan las clases no linealmente separables de iris plant
X, y = iris.data[50:150,feat], (iris.target[50:150]==1).astype(int)

#División de dataset iris plant en conjuntos de entrenamiento y prueba -estratificado-
X_tr, X_te, y_tr, y_te = train_test_split(X,y, test_size=0.1, stratify=y)

#Extendiendo vector
X_tr = np.append(X_tr, np.repeat(np.array([np.array([1])]), np.size(X_tr,0), axis=0), 1)
X_te = np.append(X_te, np.repeat(np.array([np.array([1])]), np.size(X_te,0), axis=0), 1)

#Peso Inicial
tmpW = np.random.uniform(-0.5, 0.5, size = np.size(X_tr,1))

c, e, W = perceptron_algorithm(X_tr,y_tr, W=tmpW, learning_rate=0.25)
plot_hyperplane(X_tr,y_tr,W[0:2], W[2])
tr_acc = evaluate_perceptron_rule(X_tr, y_tr, W)
te_acc = evaluate_perceptron_rule(X_te, y_te, W)
print(f'Perceptron Algorithm: Converge [{c}], Epocas [{e}], Pesos [{W}] Tr_corr [{tr_acc}], Te_corr[{te_acc}]')

c, e, W = pocket_algorithm(X_tr,y_tr, W=tmpW, learning_rate=0.25)
plot_hyperplane(X_tr,y_tr,W[0:2], W[2])
tr_acc = evaluate_perceptron_rule(X_tr, y_tr, W)
te_acc = evaluate_perceptron_rule(X_te, y_te, W)
print(f'Pocket Algorithm: Converge [{c}], Epocas [{e}], Pesos [{W}] Tr_corr [{tr_acc}], Te_corr[{te_acc}]')
