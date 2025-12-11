class Usuario():
    def __init__(self, nombre, apellido, nro_documento, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.nro_documento = nro_documento
        self.login = login
        self.password = password
        
    def enviar_sugerencia(self, sugerencia):
        print(f"El usuario {self.nombre} {self.apellido} envia una sugerencia")
        sugerencia = input()