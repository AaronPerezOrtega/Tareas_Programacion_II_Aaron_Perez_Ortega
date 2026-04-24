from modelos.figura import Figura

class Triangulo(Figura):
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura
        self.__lado = []
        
    def obtener_base(self):
        return self.__base
        
    def obtener_altura(self):
        return self.__altura
    
    def obtener_lado(self,i):
        return self.__lado[i]
    
    def lados(self,x):
        self.__lado.append(x)

    def area(self):
        res = (self.obtener_base()*self.obtener_altura())/2
        return res
    
    def perimetro(self):
        res = 0
        for i in range(len(self.__lado)):
            res += self.obtener_lado(i)
        res = res + self.obtener_base()
        return res