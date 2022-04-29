from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

def plot_decisionFunction(X,y, clf): 
    plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)

    # plot the decision function
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # create grid to evaluate model
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = clf.decision_function(xy).reshape(XX.shape)

    # plot decision boundary and margins
    ax.contour(
        XX, YY, Z, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"]
    )
    # plot support vectors
    ax.scatter(
        clf.support_vectors_[:, 0],
        clf.support_vectors_[:, 1],
        s=100,
        linewidth=1,
        facecolors="none",
        edgecolors="k",
    )
    plt.show()


#Cargar dataset
#ds = load_breast_cancer()
#ds = load_iris()


#Caracteristicas a cargar
#feat = [3,29]
#feat = [2,3]

#Se seleccionan las clases no linealmente separables de iris plant
#X, y = ds.data[:,feat],ds.target 
#X, y = ds.data[50:150,feat], (ds.target[50:150]==1).astype(int)
X, y = make_moons(n_samples=100, noise=0.15)

#División de dataset iris plant en conjuntos de entrenamiento y prueba -estratificado-
X_tr, X_te, y_tr, y_te = train_test_split(X,y, test_size=0.1, stratify=y)

scaler = StandardScaler()
scaler.fit(X_tr)
tX_tr = scaler.transform(X_tr)
tX_te = scaler.transform(X_te)
C=5

svmLU = SVC(C=C, kernel="poly", degree=3, coef0=1)
svmLU.fit(X_tr, y_tr)
plot_decisionFunction(X_tr,y_tr,svmLU)
print(accuracy_score(y_tr,svmLU.predict(X_tr)))
print(accuracy_score(y_te,svmLU.predict(X_te)))

svmLS = SVC(C=C, kernel="poly", degree=3, coef0=1)
svmLS.fit(tX_tr, y_tr)
plot_decisionFunction(tX_tr,y_tr,svmLS)
print(accuracy_score(y_tr,svmLS.predict(tX_tr)))
print(accuracy_score(y_te,svmLS.predict(tX_te)))


