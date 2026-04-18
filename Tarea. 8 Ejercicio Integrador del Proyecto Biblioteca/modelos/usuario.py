from modelos.persona import Persona
from abc import ABC, abstractmethod

class Usuario(Persona,ABC): 
    def __init__(self,nombre,identificador,tipo_usuario):
        super().__init__(nombre,identificador)
        self.__tipo_usuario = tipo_usuario
        
    def getTipo_Usuario(self):
        return self.__tipo_usuario
    
    @abstractmethod
    def descripcion(self):
        pass
    
    def __str__(self):
        return f"Usuario: {self.getNombre()} ID: {self.getIdentificador()}"