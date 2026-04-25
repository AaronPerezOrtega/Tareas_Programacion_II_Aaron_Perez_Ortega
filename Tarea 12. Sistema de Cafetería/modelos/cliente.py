class Cliente:
    def __init__(self,nombre,id):
        self._nombre = nombre
        self._id = id
        
    def obtener_nombre(self):
        return self._nombre 
    
    def obtener_id(self):
        return self._id
    
    def obtener_descuento(self):
        return 0
    
    def __str__(self):
        return f"Cliente: {self._nombre} - {self._id}"