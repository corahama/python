class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
referencia:\t {}
nombre:\t\t {}
pvp:\t\t {}
descripcion:\t {}\n""".format(self.referencia, self.nombre, self.pvp, self.descripcion)

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
referencia:\t {}
nombre:\t\t {}
pvp:\t\t {}
descripcion:\t {}
productor\t {}
distribuidor:\t {}\n""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)

class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
referencia:\t {}
nombre:\t\t {}
pvp:\t\t {}
descripcion:\t {}
isbn:\t\t {}
autor:\t\t {}\n""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)


adorno = Adorno("000A", "Vasija", 15, "Esta bonita")
alimento = Alimento("111A", "Carne", 20, "Sabe rica")
alimento.productor = "costeña"
alimento.distribuidor = "un carro"
libro = Libro("222A", "Los juegos del hambre", 35, "Esta chido")
libro.isbn = "1234"
libro.autor = "Collins"

print(adorno)
print(alimento)
print(libro)
