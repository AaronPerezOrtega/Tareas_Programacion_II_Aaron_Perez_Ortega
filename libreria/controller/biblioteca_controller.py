from modelos.biblioteca import Biblioteca
from modelos.libro import Libro
from tkinter import messagebox

class Biblioteca_Controller:
    def __init__(self,vista):
        self.vista = vista
        self.biblioteca = Biblioteca()

    def agregar_libro(self):
        titulo = self.vista.entrada_titulo.get()
        autor = self.vista.entrada_autor.get()

        if (titulo == "" or autor == ""):
            messagebox.showwarning("Error", "Los campos son obligatorios")
        else:
            libro = Libro(titulo, autor)
            self.biblioteca.agregar_libro(libro)

            messagebox.showinfo("Exito", "Libro agregado :D")

            self.vista.limpiar_campos()

    def mostrar_libros(self):
        self.vista.lista_libros.delete(0, "end")
        for libro in self.biblioteca.obtener_listado_de_libros():
            self.vista.lista_libros.insert("end", str(libro))
