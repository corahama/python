from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

#Funcion para obtener las metricas de clasificacion
def get_classification_metrics (y_true, y_predict):
    #Matriz de confusion    
    #conf_mat = confusion_matrix(y_true,y_predict)
    #tn, fp, fn, tp = conf_mat.ravel()
    #print(f'Matriz de confusion [[tn fp],[fn tp]]: \n{conf_mat}')
    #print(f'tp: {tp}, fn: {fn}, fp: {fp}, tn: {tn}')
    #ConfusionMatrixDisplay.from_predictions(y_true,y_predict)
    #plt.show()
    #Exactitud
    #print(f'Exactitud: {accuracy_score(y_true, y_predict, normalize=False)}')
    #print(f'Exactitud Normalizada: {accuracy_score(y_true, y_predict)}')
    #Precision
    #print(f'Precision: {precision_score(y_true, y_predict)}')
    #Sensibilidad
    #print(f'Sensibilidad: {recall_score(y_true, y_predict)}')
    #Puntaje F1
    #print(f'Puntaje F1: {f1_score(y_true, y_predict)}')
    #Reporte de clasificacion
    print(f'Reporte de clasificacion: \n{classification_report(y_true,y_predict)}')
    print('\n')


#Cargar dataset
iris = load_iris()

#Mostrar descripcion
#print(f'{iris.DESCR}\n\n')

#Mostrar grafica de dispersion a pares (pairs plot)
#sns.pairplot(pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target']), hue="target")               
#plt.show()

#Caracteristicas a cargar
feat = [2,3]

#Definir clasificadores a usar
classifier1 = KNeighborsClassifier(n_neighbors=3)#Perceptron(max_iter=1500, eta0=0.5, random_state=10)
classifier2 = KNeighborsClassifier(n_neighbors=1)


#Vectores de caracteristicas bidimensionales para grafica de dispersion
#X, y = iris.data[0:100,feat], iris.target[0:100] #Caso linealmente separable -biclase- -clases balancedas-
#X, y = iris.data[50:150,feat], (iris.target[50:150]==2) #Caso inseparable -biclase- -clases balancedas-
#X, y = iris.data[50:120,feat], (iris.target[50:120]==2) #Caso clases desbalanceadas -biclase-
X, y = iris.data[:,feat], iris.target #Caso 1 clase linealmente separable de 2 clases inseparable -multiclase- -clases balancedas- El Perceptron no funciona en este caso

#Entrenamiento con todos los datos disponibles, ¡no es recomendable!
#classifier1.fit(X,y)
#classifier2.fit(X,y)
#predictions = classifier1.predict(X)
#print('Rendimiento en todo el Conjunto [Perceptron]')
#get_classification_metrics(y, predictions)
#predictions = classifier2.predict(X)
#print('Rendimiento en todo el Conjunto [1NN]')
#get_classification_metrics(y, predictions)


#División de dataset iris plant en conjuntos de entrenamiento y prueba -estratificado-
X_tr, X_te, y_tr, y_te = train_test_split(X,y, test_size=0.1, random_state=10, stratify=y)

#Grafica que muestra conjunto de entrenamiento y conjunto de prueba
Xg = np.concatenate((X_tr,X_te))
yg = np.concatenate((y_tr, np.repeat(-1,np.size(y_te,0))))

plt.scatter(Xg[:,0],Xg[:,1], c=yg)
plt.xlabel(iris.feature_names[feat[0]])
plt.ylabel(iris.feature_names[feat[1]])
plt.title("Iris Plant [Entrenamiento y Prueba]")
plt.show()

#Desempeno clasificadores en conjunto de entrenamiento
classifier1.fit(X_tr,y_tr)
predictions = classifier1.predict(X_tr)
print('Rendimiento en Datos de entrenamiento [Perceptron]')
get_classification_metrics(y_tr, predictions)

classifier2.fit(X_tr,y_tr)
predictions = classifier2.predict(X_tr)
print('Rendimiento en Datos de entrenamiento [1NN]')
get_classification_metrics(y_tr, predictions)


#Desempeno clasificadores en conjunto de prueba
predictions = classifier1.predict(X_te)
print('Rendimiento en Datos de prueba [Perceptron]')
get_classification_metrics(y_te, predictions)

predictions = classifier2.predict(X_te)
print('Rendimiento en Datos de prueba [1NN]')
get_classification_metrics(y_te, predictions)