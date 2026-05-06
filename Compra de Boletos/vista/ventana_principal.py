import tkinter as tk
from modelos.comprar_boleto import Comprar_Boleto

class Ventana_Principal:
    def __init__(self,root):
        
        self.root = root
        self.root = "Compra de Boletos"
        
        tk.Label(root, text="Saickets", font=("Times New Roman",30)).pack(pady=(10,0))
        tk.Label(root, text="(Boletos al Menor Precio)", font=("Arial",10)).pack(pady=(0,10))
        tk.Label(root, text="Comprar Boletos:", font=("Arial",12)).pack(pady=(25,5))
        
        frame_datos = tk.Frame(root)
        frame_datos.pack(pady=5)
        
        tk.Label(frame_datos, text = "Nombre del Cliente:").grid(row=0, column=0)
        self.entrada_cliente = tk.Entry(frame_datos)
        self.entrada_cliente.grid(row=1, column=0)
        
        tk.Label(frame_datos, text = "Concierto:").grid(row=2, column=0)
        self.entrada_concierto = tk.Entry(frame_datos)
        self.entrada_concierto.grid(row=3, column=0)
        
        tk.Label(frame_datos, text = "Cantidad de Boletos:").grid(row=4, column=0)
        self.entrada_boletos = tk.Entry(frame_datos)
        self.entrada_boletos.grid(row=5, column=0,pady=(0,20))
        
        self.boton_comprar = tk.Button(frame_datos, text="Comprar")
        self.boton_comprar.grid(row=6, pady=10)
        
        tk.Label(frame_datos, text = "Conciertos Disponibles:", font=("Arial",14)).grid(row=7, column=0, pady=10)
        self.lista_de_eventos = tk.Listbox(root, width=22,font=("Arial",14))
        self.lista_de_eventos.pack(pady=0)
        
        self.lista_de_eventos.insert(tk.END,"Necry Talkie           12/05/26")
        self.lista_de_eventos.insert(tk.END,"Ado                         15/07/26")
        self.lista_de_eventos.insert(tk.END,"Hatsune Miku          17/07/26")
        self.lista_de_eventos.insert(tk.END,"Kasane Teto           18/07/26")
        #self.lista_de_eventos.insert(tk.END,"Necry Talkie")
        #self.lista_de_eventos.insert(tk.END,"Ado")
        #self.lista_de_eventos.insert(tk.END,"Hatsune Miku")
        #self.lista_de_eventos.insert(tk.END,"Kasane Teto")
    
    def limpiar_campos(self):
        self.entrada_cliente.delete(0, tk.END)
        self.entrada_concierto.delete(0, tk.END)
        self.entrada_boletos.delete(0, tk.END)
    
    def limpiar_concierto(self):
        self.entrada_concierto.delete(0, tk.END)

    def limpiar_boletos(self):
        self.entrada_boletos.delete(0, tk.END)
