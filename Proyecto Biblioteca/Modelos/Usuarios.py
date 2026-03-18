class Usuarios:
    def __init__(self,Nombre,Identificador):
        self.__Nombre = Nombre
        self.__Identificador = Identificador

    def getNombre(self):
        return self.__Nombre

    def getIdentificador(self):
        return self.__Identificador
    
    def __str__(self):
        return f"Usuario: {self.__Nombre} (ID: {self.__Identificador})"
