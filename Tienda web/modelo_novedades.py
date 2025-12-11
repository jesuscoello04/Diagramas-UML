from modelo_producto import Producto

class Novedades(Producto):
    def __init__(self, precio, titulo, autor, editorial, año_de_creacion, preferencias, clasificacion, tema):
        super().__init__(precio, titulo, autor, editorial, año_de_creacion, preferencias)
        
        self.clasificacion = clasificacion
        self.tema = tema
        
    def cambiar_clasificacion(self):
        print(f"se cambia la clasificacion del libro {self.titulo} a {self.clasificacion}")