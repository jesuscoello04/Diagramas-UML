class Producto():
    def __init__(self, precio, titulo, autor, editorial, año_de_creacion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_de_creacion = año_de_creacion
        self.preferencias = preferencias
        
    def vender(self):
        print(f"Se realiza la venta del libro {self.titulo} de la editorial {self.editorial} a un precio ${self.precio}")
        
    def comprar(self):
        print(f"Se realiza la compra del libro {self.titulo} del escritor {self.autor} a un precio de {self.precio}")
        
    def ver_catalogo(self):
        print(f"Se realiza la vista del catalogo por medio de preferencias {self.preferencias}")