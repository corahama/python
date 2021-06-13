from collections import deque

pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)

pila.pop()
pila.pop()
print(pila)

cola = deque(['Hector', 'Juan', 'Miguel'])
cola.append('Maria')
cola.append('Arnaldo')
print(cola)

cola.popleft()
print(cola)
