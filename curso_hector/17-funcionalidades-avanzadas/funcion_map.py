a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [11,12,13,14,15]

# print(list(map(lambda x,y,z: x*y*z, a,b,c)))

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años.".format(self.nombre, self.edad)

personas = (
    Persona("Fernando", 22),
    Persona("Laura", 21),
    Persona("Axel", 17),
    Persona("Angel", 14)
)

print(list(map(lambda persona:Persona(persona.nombre,persona.edad+1), personas)))
