from modelos.cliente import Cliente

class Cliente_Frecuente(Cliente):
    def __init__(self, nombre, id):
        super().__init__(nombre, id)
        self._descuento = 0.15

    def obtener_descuento(self):
        return self._descuento

    def __str__(self):
        return f"Cliente: {self._nombre} - {self._id} es cliente frecuente entonces tiene {self._descuento*100:.0f}% de descuento"