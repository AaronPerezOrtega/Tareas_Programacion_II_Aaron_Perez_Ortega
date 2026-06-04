import flet as ft

class EnfermedadView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = ("Dashboard Enfermedades")
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.scroll = "auto"

        #Botones

        self.btn_estadisticas = (
            ft.ElevatedButton(
                "Estadísticas Grafica de Pastel"
            )
        )
        
        self.btn_estadisticas_barras = (
            ft.ElevatedButton(
                "Estadísticas Grafica de Barras"
            )
        )

        self.btn_riesgo = (
            ft.ElevatedButton(
                "Pacientes Riesgo"
            )
        )

        self.btn_mayores = (
            ft.ElevatedButton(
                "Pacientes Mayores"
            )
        )
        
        #Resultados

        self.resultado = ft.Text(
            size=18
        )

        #Tabla
        self.tabla = ft.DataTable(

            columns=[
                ft.DataColumn(
                    ft.Text("Glucosa")
                ),
                ft.DataColumn(
                    ft.Text("BMI")
                ),
                ft.DataColumn(
                    ft.Text("Edad")
                ),
                ft.DataColumn(
                    ft.Text("Resultado")
                )
            ],
            rows=[]
        )

    #Interfaz

    def construir(self):
        return ft.Column(
            controls=[
                ft.Text(
                    "Sistema de Visualización",
                    size=32,
                    weight="bold"
                ),
                ft.Row(
                    controls=[
                        self.btn_estadisticas,
                        self.btn_estadisticas_barras,
                        self.btn_riesgo,
                        self.btn_mayores
                        
                    ]
                ),
                ft.Divider(),
                self.resultado,
                self.tabla
            ],
            spacing=20
        )