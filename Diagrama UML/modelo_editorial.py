#Clase editorial
class Editorial():
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        print(f"La editorial {self.nombre} realiza la venta de un producto")