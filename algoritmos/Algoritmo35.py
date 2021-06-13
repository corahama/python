"""Haga un programa que calcule la suma de los numeros pares comprendidos
entre 10 y 50"""

x = 0
for l in range(10,50):
    if l % 2 == 0:
        x = x + l
        print (x)
    else:
        pass
print(x)
