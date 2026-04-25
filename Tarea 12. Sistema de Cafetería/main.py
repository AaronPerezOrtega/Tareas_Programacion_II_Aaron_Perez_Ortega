from modelos.cliente import Cliente
from modelos.cliente_frecuente import Cliente_Frecuente
from modelos.producto import Producto
from modelos.pedido import Pedido
from modelos.cafeteria import Cafeteria




def main():
    cafe = Cafeteria()

    # Clientes
    cliente1 = Cliente("Evan", "C_001")
    cliente2 = Cliente_Frecuente("Sairi", "c_002")
    
    # Productos
    producto1 = Producto("Malteada", 40)
    producto2 = Producto("Dona", 15)


    # Pedido 1
    pedido1 = Pedido(cliente1)
    pedido1.agregar_producto(producto1)
    pedido1.agregar_producto(producto2)

    # Pedido 2
    pedido2 = Pedido(cliente2)
    pedido2.agregar_producto(producto1)
    pedido2.agregar_producto(producto2)

    cafe.agregar_pedido(pedido1)
    cafe.agregar_pedido(pedido2)

    cafe.mostrar_pedidos()

if __name__ == "__main__":
    main()