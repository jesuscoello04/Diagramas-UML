from modelo_producto import Producto

#Clase hija libro
class Libro(Producto):
    def __init__(self, precio, titulo, autor, editorial, año_de_creacion, preferencias, genero):
        super().__init__(precio, titulo, autor, editorial, año_de_creacion, preferencias)

        self.genero = genero