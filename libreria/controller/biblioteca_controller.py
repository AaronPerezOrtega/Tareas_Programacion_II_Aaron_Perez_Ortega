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
            
    def eliminar_primer_libro(self):
        if self.biblioteca.eliminar_primer_libro():
            self.mostrar_libros()
            messagebox.showinfo("Exito","Se elimino el primer libro exitosamente")
        else:
            messagebox.showwarning("Error","No hay libros guardados D:")
            
    def eliminar_por_titulo(self):
        titulo = titulo = self.vista.entrada_titulo.get()
        if titulo == "":
            messagebox.showwarning("Error","No hay libros guardados D:")
            return
        
        if self.biblioteca.eliminar_por_titulo(titulo):
            self.mostrar_libros()
            messagebox.showinfo("Exito","Se elimino el libro exitosamente")
            self.vista.limpiar_campos()
        else:
            messagebox.showwarning("Error","Libro no encontrado D:")
            self.vista.limpiar_campos()
            
    def eliminar_ultimo_libro(self):
        if self.biblioteca.eliminar_ultimo_libro():
            self.mostrar_libros()
            messagebox.showinfo("Exito","Se elimino el ultimo libro exitosamente")
        else:
        
        

