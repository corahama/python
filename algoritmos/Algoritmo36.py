"""Dados N numeros entreos como datos, haga un diagrama de flujo que:
a)Obtenga cunantos numeros leidos son mayores a 0
b)Calcule el promedio de los numeros positivos
c)Obtenga el promedio de todos los numeros
"""

N = int(input('Introduce el valor de los datos N:'))
x1, s, st = 0

for l in range(0,N):
    x = int(input('Introduce un valor:'))
    if x > 0:
        x1 = x1 + 1
        s = s + x
    else:
        pass
    st= st + x
p = s / x1, pt = st / N
print('La cantidad de numeros leidos mayores a cero es:', x1)
print('El promedio de los numeros positivos es:', p)
print('El promedio de todos los numeros es:', pt)
