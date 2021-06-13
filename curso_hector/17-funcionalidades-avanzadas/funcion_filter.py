numeros = [2,5,10,23,50,33]

def multiple(numero):
    if numero % 5 == 0:
        return True

# print(list(filter(multiple, numeros)))

f = filter(multiple,numeros)
# print(next(f))

list(filter(lambda numero: numero % 5 == 0, numeros))
# print(list)

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

menores = filter(lambda persona: persona.edad < 18, personas)
print([persona.edad for persona in menores])
