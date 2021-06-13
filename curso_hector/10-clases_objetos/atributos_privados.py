class Ejemplo():
    __atributo = "Soy un atributo privado"
    public_atributo = "Soy un atributo publico"

    def get_atributo(self):
        print(self.__atributo)

    def __metodo_privado(self):
        print("Soy un metodo privado")

    def get_metodo(self):
        self.__metodo_privado()

iteracion = Ejemplo()
# iteracion.__atributo
print(iteracion.public_atributo)
iteracion.get_atributo()
iteracion.get_metodo()
