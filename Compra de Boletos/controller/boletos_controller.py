from modelos.comprar_boleto import Comprar_Boleto
import tkinter as tk
from tkinter import messagebox

class Boletos_Controller:
    def __init__(self,vista):
        self.vista = vista
        
    def comprar(self):
        cliente = self.vista.entrada_cliente.get()
        concierto = self.vista.entrada_concierto.get()
        boletos = self.vista.entrada_boletos.get()
        
        if (cliente == "" or concierto == "" or boletos == ""):
            messagebox.showwarning("Error", "Los campos son obligatorios D:<")
            return
        
        #conciertos = self.vista.lista_de_eventos.get(0,tk.END)
        conciertos = ["Necry Talkie","Ado","Hatsune Miku","Kasane Teto"]
        
        if concierto not in conciertos:
            messagebox.showwarning("Error", "El concierto no esta disponible D:")
            self.vista.limpiar_concierto()
            return
            
        try:
            boletos = int(boletos)
        except ValueError:
            messagebox.showwarning("Error","La cantidad de boletos debe ser un numero D:")
            self.vista.limpiar_boletos()
            return
        
        compra = Comprar_Boleto(cliente, concierto, int(boletos))
        messagebox.showinfo("compra realizada :D", str(compra))
        self.vista.limpiar_campos()
        