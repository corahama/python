lista = [1,2,3,4,5]
lista.append(6)
lista.clear()
print(lista)

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

print(["hola", "mundo", "mundo"].count("mundo"))
print(["hola", "mundo", "mundo"].index("hola"))

l = [5,10,15,25]
l.insert(-1,20)
print(l)

numeros = [10, 20, 30, 40, 50]
numeros.pop()
numeros.pop(0)
numeros.remove(30)
numeros.reverse()
print(numeros)

cadena = list("hola mundo")
cadena.reverse()
cadena_invertida = "".join(cadena)
print(cadena_invertida)

numeros = [5, -10, 20, -65, 30]
numeros.sort()
print(numeros)
numeros.sort(reverse = True)
print(numeros)
