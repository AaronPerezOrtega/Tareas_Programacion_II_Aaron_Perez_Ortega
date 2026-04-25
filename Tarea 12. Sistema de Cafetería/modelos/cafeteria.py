class Cafeteria:
    def __init__(self):
        self._clientes = []
        self._productos = []
        self._pedidos = []

    def agregar_cliente(self, cliente):
        self._clientes.append(cliente)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def agregar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def mostrar_pedidos(self):
        for pedido in self._pedidos:
            print(pedido)