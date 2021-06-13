def revisar(function):
    def test():
        print("Se esta ejecutando la fucnion {}".format(function.__name__))
        function()
        print("Se acaba de ejecutar la fucnion {}".format(function.__name__))

    return test

def revisar_args(function):
    def test(*args, **kwargs):
        print("Se esta ejecutando la fucnion {}".format(function.__name__))
        function(*args, **kwargs)
        print("Se acaba de ejecutar la fucnion {}".format(function.__name__))

    return test


@revisar_args
def hola(nombre):
    print("Hola {}!".format(nombre))

@revisar_args
def adios(nombre):
    print("Adios! {}".format(nombre))


hola("Fernando")
print("")
adios("Contreras")
