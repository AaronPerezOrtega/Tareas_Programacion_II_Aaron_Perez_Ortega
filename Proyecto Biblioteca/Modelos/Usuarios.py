from modelos.persona import persona

class Usuarios:
    def __init__(self,Nombre,Identificador,tipo_usuario):
        super().__init__(nombre,identificador)
        self.__tipo_usuario

    def getNombre(self):
        return self.__Nombre

    def getIdentificador(self):
        return self.__Identificador
    
    def __str__(self):
        return f"Usuario: {self.__Nombre} (ID: {self.__Identificador})"
