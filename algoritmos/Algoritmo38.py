"""Un vendedor ha hecho una serie de ventas y desea saber cuantas de estas fueron
de $200 o menos, cuantas fueron mayores a $200 y menores a $400, y cunatas
de $400 o superiores a tal cantidad.
"""
x1, x2, x3=0
N = int(input('Cuantas ventas hizo el señor?:'))
for l in range(0,N):
    x = int(input('Introduce el valor de la venta:'))
    if x <= 200:
        x1 = x1 +1
    elif x > 200 and x <= 400:
        x2 = x2 +1
    else:
        x3 = x3+1
print (x1)
print (x2)
print (x3)
