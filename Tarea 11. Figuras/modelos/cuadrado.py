from modelos.figura import Figura

class Cuadrado(Figura):
    def __init__(self,lado):
        self.__lado = lado
        
    def obtener_lado(self):
        return self.__lado

    def area(self):
        res =  self.obtener_lado() * self.obtener_lado()
        return res
    
    def perimetro(self):
        res = self.obtener_lado() * 4
        return res