class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.obtener_precio()
        descuento = self._cliente.obtener_descuento()
        total = total - (total * descuento)
        return total

    def __str__(self):
        print(f"{self._cliente} pidio: ",)
        for i in self._productos:
            print(i)
        print(f"Su Total es de: ${self.calcular_total()}")
        return ""