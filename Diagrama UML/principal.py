from modelo_usuario import Usuario
from modelo_libro import Libro
from modelo_revista import Revista
from modelo_articulo_online import Articulo_online
from modelo_articulo_segunda_mano import Articulo_segunda_mano
from modelo_novedades import Novedades
from modelo_editorial import Editorial
from modelo_servidor import Servidor
from modelo_procesador import Procesador

#Instancia de un usuario
objUsuario = Usuario("Juan", "Pérez", "12345678", "juanperez", "pass123")
print(f"\nUsuario: {objUsuario.nombre} {objUsuario.apellido}")

#Instancia de la editorial
objEditorial = Editorial("Editorial Planeta", "Calle 123", "555-1234")
print(f"Editorial: {objEditorial.nombre}\n")

#Instancia de la clase hija libro
objLibro = Libro(45000, "Cien Años de Soledad", "García Márquez", "Planeta", 1967, "Ficción", "Realismo Mágico")

#Instancia de la clase hija revista
objRevista = Revista(15000, "National Geographic", "Varios", "Nat Geo", 2024, "Ciencia", "Naturaleza")

#Instancia de la clase hija articulo online
objArticuloOnline = Articulo_online(0, "Introducción a Python", "John Doe", "Tech Pub", 2024, "Programación", "Tecnología")

#Instancia de la clase hija novedades
objNovedad = Novedades(55000, "Nuevo Bestseller", "Autor Famoso", "Nova", 2024, "Ficción", "Lanzamiento", "Thriller")

#Probar los metodos de las clases
objLibro.comprar()
objLibro.vender()
objRevista.ver_catalogo()
objArticuloOnline.publicar()
objNovedad.cambiar_clasificacion()
objEditorial.vender()
objServidor = Servidor()
objServidor.muestra_pagina()
objProcesador = Procesador()
objProcesador.realizar_cobro()