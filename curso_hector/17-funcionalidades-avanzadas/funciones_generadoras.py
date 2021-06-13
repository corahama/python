def pares(n):
    for numero in  range(0,n+1):
        if numero % 2 == 0:
            yield numero

lista = [numero for numero in pares(10)]
# print(lista)

pares = pares(3)
# print(next(pares))
# print(next(pares))

lista = [1,2,3,4,5]
lista_iterable = iter(lista)
print(next(lista_iterable))
print(next(lista_iterable))
