from modelos.usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self,nombre,identificador):
        super().__init__(nombre,identificador,"Bibliotecario")
        
    def descripcion(self):
        return f"{self.getTipo_Usuario()}: {self.getNombre()}  {self.getIdentificador()}"
    
    def registrar_libro(self):
        print("El bibliotecario registra un libro")