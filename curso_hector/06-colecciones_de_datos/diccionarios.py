vacio = {}
print(type(vacio))

colores = {'amarillo':'yellow', 'azul':'blue', 'verde':'green'}
print(colores)
print(colores['azul'])

numeros = {10:'diez', 20:'veinte'}
print(numeros[10])


colores['amarillo'] = 'white'
print(colores)

del(colores['amarillo'])
print(colores)

edades = {'Hector':27, 'Juan':45, 'Maria':34}
print(edades)
edades['Hector'] += 1
print(edades)

for edad in edades:
    print(edad)

for clave in edades:
    print(edades[clave])

for clave,valor in edades.items():
    print(clave, valor)

personajes = []
p = {'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Humano'}
personajes.append(p)
p = {'Nombre':'Legolas', 'Clase':'Arquero', 'Raza':'Elfo'}
personajes.append(p)
print(personajes)

for p in personajes:
    print(p['Nombre'],p['Clase'],p['Raza'])
