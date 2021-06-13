import pickle

lista = [1,2,3,4,5]
fichero = open('lista.bin', 'wb')
pickle.dump(lista, fichero)
fichero.close()

fichero = open('lista.bin', 'rb')
l = pickle.load(fichero)
print(l)
fichero.close()


class Persona:

    def __init__(self, nombre, apellido, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.ocupacion = ocupacion

    def __str__(self):
        return "Nombre: {}\nApellido: {}\nOcupacion: {}\n".format(self.nombre, self.apellido, self.ocupacion)

nombres = [('Fernando', 'Contreras', 'Programador'), ('Laura', 'Gonzalez', 'Minas'), ('Carlos', 'Rodriguez', 'Ingeniero')]
personas = []

for n in nombres:
    p = Persona(n[0], n[1], n[2])
    personas.append(p)

fichero = open('lista.bin', 'wb')
pickle.dump(personas, fichero)

fichero = open('lista.bin', 'rb')
objeto = pickle.load(fichero)
print("")
for p in objeto:
    print(p)
fichero.close()
