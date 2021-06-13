from io import open

texto = "Una linea con texto\nOtra linea con texto"
fichero = open('fichero.txt', 'w')
fichero.write(texto)
fichero.close()

fichero = open('fichero.txt', 'r')
texto_leido = fichero.read()
fichero.close()
print(texto_leido)

fichero = open('fichero.txt', 'r')
lineas = fichero.readlines()
print(lineas)
print(lineas[0])
fichero.close()

fichero = open('fichero.txt', 'a')
fichero.write('\nTercera linea del fichero')
fichero.close()
fichero = open('fichero.txt', 'r')
lineas = fichero.readlines()
print(lineas)
fichero.close()

fichero = open('fichero_inventado.txt', 'a')
fichero = open('fichero_inventado.txt', 'r')
l = fichero.readline()
print(l)
l = fichero.readline()
print(l)
fichero.close()

with open('fichero_inventado', 'r') as fichero:
    for linea in fichero:
        print(linea)
