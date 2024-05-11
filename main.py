import flet as ft
import random as rd

def decbin(n):
    if n == 0:
        return "0"
    else:
        return bin(n).replace("0b", "")
def bindec(n):
    return int(n, 2)

def decoct(n):
    if n == 0:
        return "0"
    else:
        return oct(n).replace("0o", "")
    
def octdec(n):
    return int(n, 8)

def dechex(n):
    if n == 0:
        return '0'
    else:
        return hex(n).replace("0x", "")

def hexdec(n):
    return int(n, 16)








    
def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Traductor de sistemas numericos")))
    def convertir_clicked(e):
        if dd.value=="Decimal a Binario":
            new_task2.value = decbin(int(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Binario a Decimal":
            new_task2.value = str(bindec(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Decimal a Octal":
            new_task2.value = decoct(int(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Octal a Decimal":
            new_task2.value = str(octdec(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Decimal a Hexadecimal":
            new_task2.value = dechex(int(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Hexadecimal a Decimal":
            new_task2.value = str(hexdec(new_task.value))
            new_task.focus()
            new_task2.update()
    def aleatorio_clicked(e):
        if dd.value=="Decimal a Binario":
            new_task.value=rd.randint(0, 1000000)
            new_task.update()
        elif dd.value=="Binario a Decimal":
            new_task.value= decbin(rd.randint(0, 1000000))
            new_task.update()
          
        elif dd.value=="Decimal a Octal":
            new_task.value=rd.randint(0, 1000000)
            new_task.update()
           
        elif dd.value=="Octal a Decimal":
            new_task.value= decoct(rd.randint(0, 1000000))
            new_task.update()
          
        elif dd.value=="Decimal a Hexadecimal":
            new_task.value=rd.randint(0, 1000000)
            new_task.update()
           
        elif dd.value=="Hexadecimal a Decimal":
            new_task.value= dechex(rd.randint(0, 1000000))
            new_task.update()
            
        
        
  
    def elegirop(e):
        new_task.value=""
        new_task2.value=""
        new_task.focus()
        new_task2.update()
        new_task.update()


    new_task = ft.TextField(hint_text="Ingrese el digito", width=300)
    new_task2 = ft.TextField(hint_text="", width=300)
    page.add(ft.Row([new_task,new_task2, ft.ElevatedButton("Convertir", on_click=convertir_clicked), ft.ElevatedButton("Aleatorio", on_click=aleatorio_clicked)]))
   
    dd = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Decimal a Binario", on_click=elegirop),
            ft.dropdown.Option("Binario a Decimal", on_click=elegirop),
            ft.dropdown.Option("Decimal a Octal",on_click=elegirop),
            ft.dropdown.Option("Octal a Decimal",on_click=elegirop),
            ft.dropdown.Option("Decimal a Hexadecimal",on_click=elegirop),
            ft.dropdown.Option("Hexadecimal a Decimal",on_click=elegirop),

        ],
    )
    page.add(dd)

ft.app(target=main)



ft.app(main)
