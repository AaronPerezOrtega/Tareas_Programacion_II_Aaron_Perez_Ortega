import flet as ft

def main(page: ft.Page):
    page.title = "Cartas Pokémon"

    nombre = ft.TextField(label="Nombre carta")
    tipo = ft.TextField(label="Tipo")
    cantidad = ft.TextField(label="Cantidad")

    lista = ft.Column()

    def agregar(e):
        if nombre.value and tipo.value and cantidad.value:
            lista.controls.append(
                ft.Text(f"{nombre.value} - {tipo.value} x{cantidad.value}")
            )
            nombre.value = ""
            tipo.value = ""
            cantidad.value = ""
            page.update()

    btn = ft.ElevatedButton("Agregar", on_click=agregar)

    page.add(nombre, tipo, cantidad, btn, lista)

ft.app(target=main)