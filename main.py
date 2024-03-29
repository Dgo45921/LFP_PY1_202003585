import os
import tkinter
from tkinter import *
import tkinter.font as font
from tkinter import filedialog, messagebox

import FileWriter
from Analizador import Analizador
import Crea_Form

nuevo_analizador = Analizador()
texto_archivo = ""
lista_opciones = ["Manual de usuario", "Manual técnico", "Reporte de tokens", "Reporte de errores"]
texto_analizado = False


def carga_archivo():
    ruta = filedialog.askopenfilename(title="Selecciona un archivo", initialdir="/",
                                      filetypes=(("form files", "*.form"), ("", "")))
    archivo = open(ruta, "r")
    texto_archivo = archivo.read()
    archivo.close()
    area_texto.delete(1.0, END)
    area_texto.insert(END, texto_archivo)


def opcion_seleccionada():
    global texto_analizado
    print(valor_seleccionado.get())
    if valor_seleccionado.get() == "Manual de usuario":
        #print("se imprime manual de usuario")
        os.system('firefox Documentación/user.pdf')
        return
    if valor_seleccionado.get() == "Manual técnico":
        #print("se imprime manual tecnico")
        os.system('firefox Documentación/tecnico.pdf')
        return
    if valor_seleccionado.get() == "Reporte de tokens" and texto_analizado or valor_seleccionado.get() == "Reporte de errores" and texto_analizado:
        if valor_seleccionado.get() == "Reporte de tokens":
            FileWriter.reporte_tokens(nuevo_analizador.listaTokens)
        else:
            FileWriter.reporte_errores(nuevo_analizador.listaErrores)

    else:
        messagebox.showinfo(title="Error", message="Ingrese un texto a analizar antes de generar un reporte")


def analizar():
    global texto_archivo, nuevo_analizador, texto_analizado
    texto_archivo = area_texto.get(1.0, END)
    # print(area_texto.get(1.0, END))
    Crea_Form.texto_archivo = texto_archivo
    nuevo_analizador.analizar(area_texto.get(1.0, END))
    # nuevo_analizador.imprimir_tokens()
    # nuevo_analizador.imprimir_errores()
    Crea_Form.hallar_elemento(nuevo_analizador.listaTokens)
    texto_analizado = True


# Info sobre la ventana
Ventana_principal = Tk()
Ventana_principal.title("Analizador léxico")
Ventana_principal.configure(width=1000, height=800)
Ventana_principal.resizable(False, False)
# Ventana_principal.eval('tk::PlaceWindow %s center' % Ventana_principal.winfo_pathname(Ventana_principal.winfo_id()))
Ventana_principal.eval('tk::PlaceWindow . center')
# Creando botones
mi_fuente = font.Font(family='Helvetica', size=15)

# boton de cargar archivo
boton_cargar = Button(Ventana_principal, text="Cargar data", command=carga_archivo)
boton_cargar.configure(width=10, height=3, bg="#213dec", fg="white")
boton_cargar['font'] = mi_fuente
boton_cargar.place(x=10, y=30)

# boton de analizar texto
boton_analizar = Button(Ventana_principal, text="Analizar data")
boton_analizar.configure(width=10, height=3, bg="#213dec", fg="white", command=analizar)
boton_analizar['font'] = mi_fuente
boton_analizar.place(x=800, y=680)

# creando area de texto
area_texto = Text(Ventana_principal, height=30, width=120)
area_texto.place(x=10, y=130)

# menu drop
valor_seleccionado = tkinter.StringVar(Ventana_principal)
valor_seleccionado.set("Seleccione un reporte")
menu_drop = OptionMenu(Ventana_principal, valor_seleccionado, *lista_opciones)
menu_drop.place(x=780, y=30)
menu_drop.configure(height=3, bg="white")

# boton de generar reporte
boton_generar = Button(Ventana_principal, text="Generar reporte", command=opcion_seleccionada)
boton_generar.configure(width=12, height=3, bg="#213dec", fg="white")
boton_generar['font'] = mi_fuente
boton_generar.place(x=550, y=30)

Ventana_principal.mainloop()
