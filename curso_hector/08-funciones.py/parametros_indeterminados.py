def indeterminados_posicion(*args):
    # print(args)
    for arg in args:
        print(arg)

indeterminados_posicion(5,"hola a todos", [1,2,4])


def indeterminados_nombre(**kwargs):
    # print(kwargs)
    for kwarg in kwargs:
        print("clave: {}, valor: {}".format(kwarg,kwargs[kwarg]))

indeterminados_nombre(n=5,c="hola a todos", l=[1,2,4])

def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print("Sumatorio indeterminado", t)

    for kwarg in kwargs:
        print("clave: {}, valor: {}".format(kwarg,kwargs[kwarg]))

super_funcion(10,50,-1,1.56, nombre="Hector",edad=22)
