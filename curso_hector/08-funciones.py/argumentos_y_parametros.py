def resta(a=None, b=None):
    if a == None or b == None:
        return "Error debes introducir los dos parametros"
    else:
        return a-b

print(resta(3, 4))
