while(True):
    try:
        n = float(input("Introduce un numero: "))
        m = 10
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce un numero")
    else:
        print("Todo a ocurrido correctamente")
        break
    finally:
        print("Fin de la iteracion")
