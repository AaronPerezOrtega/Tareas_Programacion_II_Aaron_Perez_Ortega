import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class Cafeteria(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cafetería")
        self.setGeometry(100, 100, 300, 350)

        layout = QVBoxLayout()

        self.cliente = QLineEdit()
        self.cliente.setPlaceholderText("Nombre del cliente")

        self.pedido = QLineEdit()
        self.pedido.setPlaceholderText("Pedido")

        self.cantidad = QLineEdit()
        self.cantidad.setPlaceholderText("Cantidad")

        self.boton = QPushButton("Agregar")
        self.boton.clicked.connect(self.agregar)

        self.lista = QListWidget()

        layout.addWidget(self.cliente)
        layout.addWidget(self.pedido)
        layout.addWidget(self.cantidad)
        layout.addWidget(self.boton)
        layout.addWidget(self.lista)

        self.setLayout(layout)

    def agregar(self):
        c = self.cliente.text()
        p = self.pedido.text()
        q = self.cantidad.text()

        if c and p and q:
            self.lista.addItem(c + " - " + p + " x " + q)
            self.cliente.clear()
            self.pedido.clear()
            self.cantidad.clear()

app = QApplication(sys.argv)
ventana = Cafeteria()
ventana.show()
sys.exit(app.exec())