class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self,libro):
        self.libros.append(libro)

    def obtener_listado_de_libros(self):
        return self.libros
    
    def eliminar_primer_libro(self):
        if len(self.libros) > 0:
            self.libros.pop(0)
            return True
        return False
    
    def eliminar_por_titulo(self,titulo):
        for libro in self.libros:
            if libro.obtener_titulo() == titulo:
                self.libros.remove(libro)
                return True
        return False
    
    def eliminar_ultimo_libro(self):
        if len(self.libros) > 0:
            self.libros.pop()
            return True
        return False
