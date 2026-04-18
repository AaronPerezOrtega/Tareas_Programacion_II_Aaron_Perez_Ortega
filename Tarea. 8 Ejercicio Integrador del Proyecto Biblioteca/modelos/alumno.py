from modelos.usuario import Usuario

class Alumno(Usuario):
    def __init__(self,nombre,identificador):
        super().__init__(nombre,identificador,"Alumno")
        
    def descripcion(self):
        return f"{self.getTipo_Usuario()}: {self.getNombre()}  {self.getIdentificador()}"
    
    def pedir_libro(self):
         print("El alumno solicita un libro")