list = [letra for letra in 'casa']
print(list)

lista2 = [numero**2 for numero in range(1,11)]
print(lista2)

# lista2 = []
# for numero in range(0,11):
#     if numero % 2 == 0:
#         lista2.append(numero)

lista2 = [numero for numero in range(0,11) if numero % 2 == 0]
print(lista2)

lista3 = [numero for numero in [numero2**2 for numero2 in range(0,11)] if numero % 2 == 0]
print(lista3)
