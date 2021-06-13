numeros = [1, 2, 4, 5, 6, 7, 8, 9, 10]
indice = 0
while (indice < len(numeros)):
    print(numeros[indice])
    indice += 1

print("\n")

for numero in numeros:
    print(numero)

print("\n")

numeros = [1, 2, 4, 5, 6, 7, 8, 9, 10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)

print("\n")

for i in range(10):
    print(i)

print(list(range(10)))
