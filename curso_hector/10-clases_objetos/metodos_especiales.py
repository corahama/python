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

pelicula = Pelicula("El padrino", 175, 1972)
print(str(pelicula))
