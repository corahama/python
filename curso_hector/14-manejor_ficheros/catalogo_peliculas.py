from io import open
import pickle

class Pelicula:

    def __init__(self, pelicula, duracion, lanzamiento):
        self.pelicula = pelicula
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelicula: ', self.pelicula)

    def __str__(self):
        return '{} {}'.format(self.pelicula, self.lanzamiento)


class Catalogo:

    peliculas = []

    def __init__(self):
        self.cargar()

    def agregar(self, p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catalogo esta vacio")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print('No se encontraron pelicula')
        finally:
            fichero.close()
            print("se han cargado {} peliculas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open('catalogo.bin', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()

    # def __del__(self):
        # self.guardar()

c = Catalogo()
c.mostrar()
c.agregar(Pelicula("El lobo de wall street", 150, 2013))
c.agregar(Pelicula("El hombre araña", 120, 2012))
c.mostrar()
