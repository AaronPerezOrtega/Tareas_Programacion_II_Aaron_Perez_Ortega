import tkinter as tk
from tkinter import messagebox

alumnos = []

def registrar_alumno():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    if nombre == "" or edad == "":
        messagebox.showwarning("Error", "Completa todos los campos")
        return

    if not edad.isdigit():
        messagebox.showwarning("Error", "La edad debe ser un número")
        return

    alumno = f"{nombre} - {edad} años"
    alumnos.append(alumno)

    lista_alumnos.insert(tk.END, alumno)

    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)



ventana = tk.Tk()
ventana.title("Registro de Alumnos")
ventana.geometry("300x350")


tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()


tk.Button(ventana, text="Registrar alumno", command=registrar_alumno).pack(pady=10)


lista_alumnos = tk.Listbox(ventana, width=40)
lista_alumnos.pack(pady=10)

ventana.mainloop()