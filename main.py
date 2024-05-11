import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Traductor de sistemas numericos")))
    def add_clicked(e):       
        new_task.value = ""
        new_task.focus()
        new_task.update()
    new_task = ft.TextField(hint_text="Ingrese el digito", width=300)
    new_task2 = ft.TextField(hint_text="", width=300)
    page.add(ft.Row([new_task,new_task2, ft.ElevatedButton("Convertir", on_click=add_clicked)]))
    

ft.app(target=main)



ft.app(main)
