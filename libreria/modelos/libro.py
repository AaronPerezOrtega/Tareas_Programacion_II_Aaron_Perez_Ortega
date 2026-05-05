class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def obtener_titulo(self):
        return self.titulo
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"