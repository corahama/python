#Método de Newton-Raphson.
#Rodríguez Corona Carlos Alberto.
#28-Abril-2021

import numpy as np
from sympy import *

#Ingreso
x = Symbol('x')
sfx = eval(input('Ingresa la funcion de x: '))
sdfx = sfx.diff(x)
fx = lambdify(x, sfx)
dfx = lambdify(x, sdfx)

x0=2
tolera=0.001

#Procedimiento
tabla=[]
tramo=abs(2*tolera)
xi=x0
while(tramo>=tolera):
    xnuevo=xi-fx(xi)/dfx(xi)
    tramo=abs(xnuevo-xi)
    tabla.append([xi,xnuevo,tramo])
    xi=xnuevo

#Convierte la lista en un arreglo
tabla=np.array(tabla)
n=len(tabla)

#Salida
print(["xi","xnuevo","tramo"])
np.set_printoptions(precision=4)
print(tabla)
print("raiz en:",xi)
print("con error de:",tramo)

#Gráfica
import matplotlib.pyplot as plt
xi=tabla[:,0]
yi=tabla[:,1]

#Ordena los puntos para la gráfica
orden=np.argsort(xi)
xi=xi[orden]
yi=yi[orden]
plt.plot(xi,yi)
plt.plot(xi,yi,"o")
plt.axhline(0,color="black")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Newton-Raphson en f(x)")
plt.grid()
plt.show()
