def doblar_valor(numero):
    numero *= 2
n = 10
doblar_valor(n)
print(n)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,20,50]
doblar_valores(ns)
print(ns)

def doblar_valor1(numero):
    return numero * 2
s = 10
s = doblar_valor1(s)
print(s)

def doblar_valores1(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ls = [10,20,50]
doblar_valores1(ls[:])
print(ls)
