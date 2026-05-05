from modelos.biblioteca import Biblioteca
from modelos.libro import Libro
import tkinter as tk


class Ventana_Principal:
    def __init__(self, root):

        self.root = root
        self.root = "Sistema de Biblioteca"

        #Titulo Principal
        tk.Label(root, text="Registro de Libros", font=("Arial",14)).pack(pady=10)

        #seccion de datos
        frame_datos = tk.Frame(root)
        frame_datos.pack(pady=5)

        #Titulo
        tk.Label(frame_datos, text = "Titulo del Libro").grid(row=0, column=0)
        self.entrada_titulo = tk.Entry(frame_datos)
        self.entrada_titulo.grid(row=0, column=1)

        #Autor
        tk.Label(frame_datos, text = "Autor").grid(row=1,column=0)
        self.entrada_autor = tk.Entry(frame_datos)
        self.entrada_autor.grid(row=1, column=1)

        #seccion de botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        #Botones
        self.boton_agregar_libros = tk.Button(frame_botones, text="Guardar libro")
        self.boton_agregar_libros.grid(row=0, column=0, padx=5)

        self.boton_listar_libros = tk.Button(frame_botones, text="Mostrar libros")
        self.boton_listar_libros.grid(row=0, column=1, padx=5)

        #Lista
        self.lista_libros = tk.Listbox(root, width=50)
        self.lista_libros.pack()

        #limpiar campos
    def limpiar_campos(self):
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_autor.delete(0, tk.END)

                