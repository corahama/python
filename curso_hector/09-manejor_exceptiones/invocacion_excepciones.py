def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error, tienes que introducr una cadena")
    except:
        print("Error, no se permite un valor nulo")

mi_funcion()
