class Comprar_Boleto:
    def __init__(self,cliente,concierto,boletos):
        self.__cliente = cliente
        self.__concierto = concierto
        self.__boletos = boletos
        
    def obtener_cliente(self):
        return self.__cliente
    
    def obtener_concierto(self):
        return self.__concierto

    def obtener_boletos(self):
        return self.__boletos
    
    def  __str__(self):
        return f"{self.__cliente}\nCompro: {self.__boletos} boletos\nPara el concierto de: {self.__concierto}"