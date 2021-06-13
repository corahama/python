"""Escriba un diagrama de flujo tal que dado N numeros enteros como datos,
calcule cual es el mayor y el menor de estos numeros"""

x1, x2 = 0
N = int(input('Cual es la longitud del vector que va a introducir?'))
for l in range(0,N):
    x = int(input('ingresa un numero:'))
    if l == 0:
        x1, x2 = x
    else:
        if x > x1:
            x1 = x
        elif x < x2:
            x2 = x
print ('El numero mas alto es:', x1)
print ('El numero mas bajo es:', x2)
