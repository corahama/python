def hola():

    def bienvenido():
        print("hola!")

    return bienvenido

# hola()()

def mensaje():
    return "Este es un mensaje"

def test(function):
    print(mensaje())

test(mensaje)
