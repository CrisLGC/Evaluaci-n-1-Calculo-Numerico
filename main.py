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
        return "0"
    else:
        return hex(n).replace("0x", "")

def hexdec(n):
    return int(n, 16)

def decter(n):
    if n == 0:
        return "0"
    else:
        tern = ""
        while n > 0:
            tern = str(n % 3) + tern
            n = n // 3
        return tern

def terdec(n):
    return int(n, 3)

def deccua(n):
    if n == 0:
        return "0"
    else:
        cuate = ""
        while n > 0:
            cuate = str(n % 4) + cuate
            n = n // 4
        return cuate

def cuadec(n):
    return int(n, 4)
def binoct(n):
    return decoct(bindec(n))
def octbin(n):
    return decbin(octdec(n))
def binhex(n):
    return dechex(bindec(n))
def hexbin(n):
    return decbin(hexdec(n))
def binter(n):
    return decter(bindec(n))
def terbin(n):
    return decbin(terdec(n))
def bincua(n):
    return deccua(bindec(n))
def cuabin(n):
    return decbin(cuadec(n))
def octhex(n):
    return dechex(octdec(n))
def hexoct(n):
    return decoct(hexdec(n))
def octter(n):
    return decter(octdec(n))
def teroct(n):
    return decoct(terdec(n))
def octcua(n):
    return deccua(octdec(n))
def cuaoct(n):
    return decoct(cuadec(n))
def hexter(n):
    return decter(hexdec(n))
def terhex(n):
    return dechex(terdec(n))
def cuater(n):
    return decter(cuadec(n))
def tercua(n):
    return deccua(terdec(n))
def hexcua(n):
    return deccua(hexdec(n))
def cuahex(n):
    return dechex(cuadec(n))
    
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
        elif dd.value=="Decimal a Ternario":
            new_task2.value = decter(int(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Ternario a Decimal":
            new_task2.value = str(terdec(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Decimal a Cuaternario":
            new_task2.value = deccua(int(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Cuaternario a Decimal":
            new_task2.value = str(cuadec(new_task.value))
            new_task.focus()
            new_task2.update()
        
        elif dd.value=="Binario a Octal":
            new_task2.value = binoct(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Octal a Binario":
            new_task2.value = str(octbin(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Binario a Hexadecimal":
            new_task2.value = binhex(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Hexadecimal a Binario":
            new_task2.value = str(hexbin(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Binario a Ternario":
            new_task2.value = binter(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Ternario a Binario":
            new_task2.value = str(terbin(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Binario a Cuaternario":
            new_task2.value = bincua(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Cuaternario a Binario":
            new_task2.value = str(cuabin(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Octal a Hexadecimal":
            new_task2.value = octhex(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Hexadecimal a Octal":
            new_task2.value = str(hexoct(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Octal a Ternario":
            new_task2.value = octter(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Ternario a Octal":
            new_task2.value = str(teroct(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Octal a Cuaternario":
            new_task2.value = octcua(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Cuaternario a Octal":
            new_task2.value = str(cuaoct(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Hexadecimal a Ternario":
            new_task2.value = hexter(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Ternario a Hexadecimal":
            new_task2.value = str(terhex(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Cuaternario a Ternario":
            new_task2.value = cuater(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Ternario a Cuaternario":
            new_task2.value = str(tercua(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Hexadecimal a Cuaternario":
            new_task2.value = hexcua(str(new_task.value))
            new_task.focus()
            new_task2.update()
        elif dd.value=="Cuaternario a Hexadecimal":
            new_task2.value = str(cuahex(new_task.value))
            new_task.focus()
            new_task2.update()

    def aleatorio_clicked(e):
        new_task2.value=""
        new_task2.update()
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
        elif dd.value=="Decimal a Ternario":
            new_task.value=rd.randint(0, 1000000)
            new_task.update()    
        elif dd.value=="Ternario a Decimal":
            new_task.value= decter(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Decimal a Cuaternario":
            new_task.value=rd.randint(0, 1000000)
            new_task.update()         
        elif dd.value=="Cuaternario a Decimal":
            new_task.value= deccua(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Binario a Octal":
            new_task.value= decbin(rd.randint(0, 1000000))
            new_task.update()   
        elif dd.value=="Octal a Binario":
            new_task.value= decoct(rd.randint(0, 1000000))
            new_task.update() 
        elif dd.value=="Binario a Hexadecimal":
            new_task.value= decbin(rd.randint(0, 1000000))
            new_task.update()   
        elif dd.value=="Hexadecimal a Binario":
            new_task.value= dechex(rd.randint(0, 1000000))
            new_task.update() 
        elif dd.value=="Binario a Ternario":
            new_task.value= decbin(rd.randint(0, 1000000))
            new_task.update()  
        elif dd.value=="Ternario a Binario":
            new_task.value= decter(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Binario a Cuaternario":
            new_task.value= decbin(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Cuaternario a Binario":
            new_task.value= deccua(rd.randint(0, 1000000))
            new_task.update()            
        elif dd.value=="Octal a Hexadecimal":
            new_task.value= decoct(rd.randint(0, 1000000))
            new_task.update()       
        elif dd.value=="Hexadecimal a Octal":
            new_task.value= dechex(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Octal a Ternario":
            new_task.value= decoct(rd.randint(0, 1000000))
            new_task.update()    
        elif dd.value=="Ternario a Octal":
            new_task.value= decter(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Octal a Cuaternario":
            new_task.value= decoct(rd.randint(0, 1000000))
            new_task.update() 
        elif dd.value=="Cuaternario a Octal":
            new_task.value= deccua(rd.randint(0, 1000000))
            new_task.update() 
        elif dd.value=="Hexadecimal a Ternario":
            new_task.value= dechex(rd.randint(0, 1000000))
            new_task.update()       
        elif dd.value=="Ternario a Hexadecimal":
            new_task.value= decter(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Cuaternario a Ternario":
            new_task.value= deccua(rd.randint(0, 1000000))
            new_task.update()           
        elif dd.value=="Ternario a Cuaternario":
            new_task.value= decter(rd.randint(0, 1000000))
            new_task.update()         
        elif dd.value=="Hexadecimal a Cuaternario":
            new_task.value= dechex(rd.randint(0, 1000000))
            new_task.update()
        elif dd.value=="Cuaternario a Hexadecimal":
            new_task.value= deccua(rd.randint(0, 1000000))
            new_task.update()
               
    def elegirop(e):

        new_task.value=""
        new_task2.value=""
        new_task.focus()
        new_task2.update()
        new_task.update()

    new_task = ft.TextField(hint_text="Ingrese el digito", width=300,input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9, a, b, c, d, e, f]", replacement_string=""))
    new_task2 = ft.TextField(label="", read_only=True,hint_text="", width=300)
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
            ft.dropdown.Option("Decimal a Ternario",on_click=elegirop),
            ft.dropdown.Option("Ternario a Decimal",on_click=elegirop),
            ft.dropdown.Option("Decimal a Cuaternario",on_click=elegirop),
            ft.dropdown.Option("Cuaternario a Decimal",on_click=elegirop),
            ft.dropdown.Option("Binario a Octal",on_click=elegirop),
            ft.dropdown.Option("Octal a Binario",on_click=elegirop),
            ft.dropdown.Option("Binario a Hexadecimal",on_click=elegirop),
            ft.dropdown.Option("Hexadecimal a Binario",on_click=elegirop),
            ft.dropdown.Option("Binario a Ternario",on_click=elegirop),
            ft.dropdown.Option("Ternario a Binario",on_click=elegirop),
            ft.dropdown.Option("Binario a Cuaternario",on_click=elegirop),
            ft.dropdown.Option("Cuaternario a Binario",on_click=elegirop),
            ft.dropdown.Option("Octal a Hexadecimal",on_click=elegirop),
            ft.dropdown.Option("Hexadecimal a Octal",on_click=elegirop),
            ft.dropdown.Option("Octal a Ternario",on_click=elegirop),
            ft.dropdown.Option("Ternario a Octal",on_click=elegirop),
            ft.dropdown.Option("Octal a Cuaternario",on_click=elegirop),
            ft.dropdown.Option("Cuaternario a Octal",on_click=elegirop),
            ft.dropdown.Option("Hexadecimal a Ternario",on_click=elegirop),
            ft.dropdown.Option("Ternario a Hexadecimal",on_click=elegirop),
            ft.dropdown.Option("Cuaternario a Ternario",on_click=elegirop),
            ft.dropdown.Option("Ternario a Cuaternario",on_click=elegirop),
            ft.dropdown.Option("Hexadecimal a Cuaternario",on_click=elegirop),
            ft.dropdown.Option("Cuaternario a Hexadecimal",on_click=elegirop),

        ],
    )
    page.add(dd)

ft.app(target=main)



ft.app(main)
