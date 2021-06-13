class Pelicula():
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = titulo
        self.lanzamiento = lanzamiento
        print('Se a creado la pelicula', self.titulo)

    def __del__(self):
        print('Se ha borrado la pelicula', self.titulo)

    def __str__(self):
        return '{} lanzada en {} con una duracion de {} minutos'.format(self.titulo, self.lanzamiento, self.duracion)

class Catalogo():
    def __init__(self):
        self.peliculas = []

    def agregar(self, p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)

pelicula1 = Pelicula("El padrino", 175, 1972)
pelicula2 = Pelicula("El lobo de WallStreet", 190, 2013)
pelicula3 = Pelicula("Amazing Spider-Man", 135, 2012)

catalogo = Catalogo()
catalogo.agregar(pelicula1)
catalogo.agregar(pelicula2)
catalogo.agregar(pelicula3)
catalogo.mostrar()
