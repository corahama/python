conjunto = set()
print(conjunto)

conjunto = {1,2,3}

conjunto.add(4)
conjunto.add(0)
conjunto.add('H')
conjunto.add('A')
conjunto.add('Z')
print(conjunto)

grupo = {'Hector', 'Juan', 'Mario'}
print('Hector' in grupo)

test = {'Hector', 'Hector', 'Hector'}
print(test)

# CASTEO
l = [1,2,3,3,2,1]
c = set(l)
print(c)

l = [1,2,3,3,2,1]
l = list(set(l))
print(l)
