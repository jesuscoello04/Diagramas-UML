from modelo_producto import Producto

#Clase hija revista
class Revista(Producto):
    def __init__(self, precio, titulo, autor, editorial, año_de_creacion, preferencias, categoria):
        super().__init__(precio, titulo, autor, editorial, año_de_creacion, preferencias)

        self.categoria = categoria