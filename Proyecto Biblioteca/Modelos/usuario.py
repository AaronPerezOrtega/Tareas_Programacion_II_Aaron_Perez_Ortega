from modelos.persona import Persona

class Usuario(Persona):
    def __init__(self,nombre,identificador,tipo_usuario):
        super().__init__(nombre,identificador)
        self.__tipo_usuario = tipo_usuario

    def getTipoUsuario(self):
        return self.__tipo_usuario
    
    def __str__(self):
        return f"{super().__str__()} - {self.__tipo_usuario}"
