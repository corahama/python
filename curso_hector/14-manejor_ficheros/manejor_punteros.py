fichero = open('fichero.txt', 'w')
fichero.write('Una linea\nOtra linea\nOtra linea mas\nUna ultima linea')

fichero = open('fichero.txt', 'r')
fichero.seek(10) #10 CARACTERES
print(fichero.read())
fichero.seek(0)
print("\n{}".format(fichero.read()))

fichero = open('fichero.txt', 'r')
fichero.seek(len(fichero.read())/2) #POSICIONAR EL PUNTERO A LA MITAD
print("\n{}".format(fichero.read()))
fichero.seek(0)
fichero.seek(len(fichero.readline()))
print("\n{}".format(fichero.read()))
fichero.close()

fichero = open('fichero.txt', 'r+')
texto = fichero.readlines()
texto[2] = 'linea modificada\n'
fichero.seek(0)
fichero.writelines(texto)
fichero.seek(0)
print("\n{}".format(fichero.read()))
fichero.close()
