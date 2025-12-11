from modelo_producto import Producto

class Articulo_segunda_mano(Producto):
     def __init__(self, precio, titulo, autor, editorial, año_de_creacion, preferencias, clasificacion, tema, vendedor):
          super().__init__(precio, titulo, autor, editorial, año_de_creacion, preferencias)
          
          self.clasificacion = clasificacion
          self.tema = tema
          self.vendedor = vendedor