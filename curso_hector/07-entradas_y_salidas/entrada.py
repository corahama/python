import sys

if len(sys.argv) == 3:
    mensaje = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for i in range(repeticiones):
        print(mensaje)

else:
    print("Numero de argumentos incorrecto")
