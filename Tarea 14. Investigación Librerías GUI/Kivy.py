#usar python 3.11 :3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.pantalla = TextInput(font_size=32, readonly=True, halign="right")
        self.add_widget(self.pantalla)

        grid = GridLayout(cols=4)

        botones = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for b in botones:
            btn = Button(text=b, font_size=24)
            btn.bind(on_press=self.presionar)
            grid.add_widget(btn)

        self.add_widget(grid)

    def presionar(self, instance):
        texto = instance.text

        if texto == "C":
            self.pantalla.text = ""
        elif texto == "=":
            try:
                self.pantalla.text = str(eval(self.pantalla.text))
            except:
                self.pantalla.text = "Error"
        else:
            self.pantalla.text += texto

class AppCalc(App):
    def build(self):
        return Calculadora()

AppCalc().run()