
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

    
def coverage_plot(models, X, y, Neg, Pos, labels, normalized = False):
    sy = np.repeat(0.0, len(labels))
    sx = np.repeat(0.0, len(labels))

    for m in range(len(models)):
        _, fp, _, tp = confusion_matrix(y, models[m].predict(X)).ravel()
        sy[m] = tp / (Pos if normalized else 1)
        sx[m] = fp / (Neg if normalized else 1)
        
    sns.set_style("darkgrid")        
    sns.scatterplot('x', 'y', data=pd.DataFrame(dict(x=sx, y = sy, model = labels)), hue='model')
    plt.ylim(-0.5,Pos / (Pos if normalized else 1) + 0.5)
    plt.xlim(-0.5,Neg / (Neg if normalized else 1) + 0.5)
    plt.xlabel('Neg (FP)')
    plt.ylabel('Pos (TP)')
    plt.title('Coverage Plot')
    plt.show()


#Cargar dataset
iris = load_iris()

#Caracteristicas a cargar
feat = [2,3]

#Se seleccionan las clases no linealmente separables de iris plant
X, y = iris.data[50:150,feat], (iris.target[50:150]==1).astype(int)

#División de dataset iris plant en conjuntos de entrenamiento y prueba -estratificado-
X_tr, X_te, y_tr, y_te = train_test_split(X,y, test_size=0.1, stratify=y)

#Se crean modelos
svm = Pipeline([('scaler', StandardScaler()), ('model', LinearSVC())])
per = Pipeline([('scaler', StandardScaler()), ('model', Perceptron())])

svm.fit(X_tr, y_tr)
per.fit(X_tr, y_tr)

coverage_plot([svm, per], X_tr, y_tr, len(y_tr[y_tr==0]), len(y_tr[y_tr==1]), ['LSVC','Perceptron'], normalized=False)
coverage_plot([svm, per], X_te, y_te, len(y_te[y_te==0]), len(y_te[y_te==1]), ['LSVC','Perceptron'], normalized=False)

