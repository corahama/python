"""Una persona invierte en un banco cierto capital y quiere saber cuanto obtendra
al cabo de un cierto tiempo. Si el dinero aumenta a tasa mensual, haga el calculo
del dinero final tomando en cuenta capital inicial, numero de mese y tasa mensual"""

x = int(input('Introduce el capital inicial:'))
m = int(input('Introduce el numero de meses:'))
t = int(input('Introduce la tasa mensual:'))
for l in range(0, m):
    if l == 0:
        pass
    else:
        x = x + x*t/100
        print(x)
