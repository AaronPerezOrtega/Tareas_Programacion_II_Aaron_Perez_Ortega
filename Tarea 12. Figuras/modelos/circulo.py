import math
from modelos.figura import Figura

class Circulo(Figura):
    def __init__(self,radio):
        self.__radio = radio
        
    def obtener_radio(self):
        return self.__radio

    def area(self):
        res = math.pi*(self.obtener_radio()**2)
        return res
    
    def perimetro(self):
        res = math.pi*(self.obtener_radio()*2)
        return res