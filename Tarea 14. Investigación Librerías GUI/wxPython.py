import wx

class App(wx.App):
    def OnInit(self):
        self.frame = Ventana()
        self.frame.Show()
        return True

class Ventana(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Cartas Pokémon", size=(350, 400))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.nombre = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.nombre.SetHint("Nombre carta")

        self.tipo = wx.TextCtrl(panel)
        self.tipo.SetHint("Tipo")

        self.cantidad = wx.TextCtrl(panel)
        self.cantidad.SetHint("Cantidad")

        self.lista = wx.ListBox(panel)

        btn = wx.Button(panel, label="Agregar")
        btn.Bind(wx.EVT_BUTTON, self.agregar)

        vbox.Add(self.nombre, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.tipo, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.cantidad, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(btn, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(self.lista, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        panel.SetSizer(vbox)

    def agregar(self, event):
        n = self.nombre.GetValue()
        t = self.tipo.GetValue()
        c = self.cantidad.GetValue()

        if n and t and c:
            self.lista.Append(f"{n} - {t} x{c}")
            self.nombre.SetValue("")
            self.tipo.SetValue("")
            self.cantidad.SetValue("")

app = App()
app.MainLoop()