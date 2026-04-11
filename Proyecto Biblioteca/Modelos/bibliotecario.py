from modelos.usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self,nombre,identificador,tipo_usuario):
        super().__init__(nombre,identificador,tipo_usuario)
        
    def RegistraLibro(self):
         print("El bibliotecario registra un libro")