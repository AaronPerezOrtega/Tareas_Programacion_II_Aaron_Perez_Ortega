import tkinter as tk
from vista.ventana_principal import Ventana_Principal
from controller.boletos_controller import Boletos_Controller

def main():
    root = tk.Tk()
    vista = Ventana_Principal(root)
    controller = Boletos_Controller(vista)
    
    vista.boton_comprar.config(command=controller.comprar)
    
    root.mainloop()
    
    
if __name__ == "__main__":
    main()