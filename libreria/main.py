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
    vista.boton_eliminar_primer_libro.config(command= controller.eliminar_primer_libro)
    vista.boton_eliminar_por_titulo.config(command= controller.eliminar_por_titulo)
    vista.boton_eliminar_ultimo_libro.config(command= controller.eliminar_ultimo_libro)

    
    root.mainloop()

if __name__ == "__main__":
    main()