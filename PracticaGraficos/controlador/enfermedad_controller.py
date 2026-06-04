import flet as ft
import matplotlib.pyplot as plt
from modelo.enfermedad_model import (EnfermedadModel)

class EnfermedadController:
    def __init__(self,vista):
        self.vista = vista
        self.modelo =  EnfermedadModel()
        
    #Estadisticas
    
    def mostrar_estadisticas(self, e):
        total = (self.modelo.total_pacientes())
        glucosa = (self.modelo.promedio_glucosa())
        bmi = (self.modelo.promedio_bmi())
        diabetes = (self.modelo.pacientes_diabetes())
        sanos = (self.modelo.pacientes_sanos())
        
        self.vista.resultado.value = f"""
Total pacientes: 
{total}
        
Promedio glucosa:
{glucosa:.2f}

Promedio BMI:
{bmi:.2f}

Pacientes con diabetes:
{diabetes}

Pacientes sanos:
{sanos}
"""

        self.vista.page.update()
        
        #Grafica    
        
        datos = [diabetes,sanos]
        etiquetas = ["Diabetes","Sanos"]
        
        plt.pie(datos,labels = etiquetas,autopct = "%1.1f%%")   
        plt.title("Paciente con y sin diabetes")
        plt.show()
        
    def mostrar_estadisticas_barras(self, e):
        total = (self.modelo.total_pacientes())
        glucosa = (self.modelo.promedio_glucosa())
        bmi = (self.modelo.promedio_bmi())
        diabetes = (self.modelo.pacientes_diabetes())
        sanos = (self.modelo.pacientes_sanos())
        
        self.vista.resultado.value = f"""
Total pacientes: 
{total}
        
Promedio glucosa:
{glucosa:.2f}

Promedio BMI:
{bmi:.2f}

Pacientes con diabetes:
{diabetes}

Pacientes sanos:
{sanos}
"""
        self.vista.page.update()
        
        #Grafica
        
        datos = [diabetes,sanos]
        etiquetas = ["Diabetes","Sanos"]
        
        plt.bar(etiquetas,datos)   
        plt.title("Paciente con y sin diabetes")
        plt.xlabel("Tipo de personas")
        plt.ylabel("Cantidades")
        plt.show()
        
    def mostrar_riesgo(self, e):
        self.vista.tabla.rows.clear()
        datos = (self.modelo.pacientes_riesgo())
        
        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells = [
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Glucose"]
                                )
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["BMI"]
                                )
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Age"]
                                )
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Outcome"]
                                )
                            )
                        )
                    ]
                )
            )
            
        self.vista.page.update()
        
    #Tabla Pacientes Mayores
    
    def mostrar_mayores(self, e):
        self.vista.tabla.rows.clear()
        datos = (
            self.modelo.pacientes_mayores()
        )
        
        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells = [
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Glucose"]
                                )
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["BMI"]
                                )
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Age"]
                                )
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                str(
                                    fila["Outcome"]
                                )
                            )
                        )
                    ]
                )
            )
        self.vista.page.update()