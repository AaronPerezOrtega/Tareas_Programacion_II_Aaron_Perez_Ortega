import tkinter as tk
from vista.ventana_principal import Ventana_Principal
from controller.biblioteca_controller import Biblioteca_Controller

def main():

    root = tk.Tk()
    vista = Ventana_Principal(root)
    controller = Biblioteca_Controller(vista)

    #conectar eventos
    vista.boton_agregar_libros.config(command= controller.agregar_libro)
    vista.boton_listar_libros.config(command= controller.mostrar_libros)

    root.mainloop()

if __name__ == "__main__":
    main()