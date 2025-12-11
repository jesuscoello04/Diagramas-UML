from modelo_producto import Producto

class Articulo_online(Producto):
    def __init__(self, precio, titulo, autor, editorial, año_de_creacion, preferencias, tema):
        super().__init__(precio, titulo, autor, editorial, año_de_creacion, preferencias)
        
        self.tema = tema
        
    def publicar(self):
        print (f"Se realiza la publicación del libro {self.titulo} sobre el tema de {self.tema}")