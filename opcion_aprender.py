import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext as st
import tkinter.font as font 

class Aprender:

    def __init__(self):
        tamano_texto = font.Font(size=12, weight = "bold" )

        self.ventana_aprender = tk.Toplevel()

        self.ventana_aprender.title("Agregar nuevo ejercicio")
        self.ventana_aprender.geometry("+850+40")
        self.pestanas = ttk.Notebook(self.ventana_aprender)


        self.agregar_ejercicio()
        self.eliminar_ejercicio()

        self.pestanas.grid(column=0, row=0)


    def agregar_ejercicio(self):

        self.pagina1 = ttk.Frame(self.pestanas)

        self.pestanas.add(self.pagina1, text="Agregar")

        self.label1=ttk.Label(self.pagina1, text="Nombre del ejercicio:")
        self.label1.grid(column=0, row=0, padx=5, pady=5)


        self.entrada_ID=tk.Entry(self.pagina1, width=20)
        self.entrada_ID.grid(column=1, row=0, padx=5, pady=5)
        self.entrada_ID.focus()
        self.boton_aceptar = tk.Button(self.pagina1,
        text="Aceptar",
        command = self.nombre_ejercicio)
        self.boton_aceptar.grid(row=1,
        column=0)

        self.boton_configuracion = tk.Button(self.pagina1,
        text="Configuración",
        command = Grabar_dato)
        self.boton_configuracion.grid(row=2,
        column=0)

        self.etiqueta_nombre = tk.Label(self.ventana_aprender,text="")
    
    
    def nombre_ejercicio(self):
        nombre = self.entrada_ID.get()
        self.etiqueta_nombre.config(text=nombre)
        self.entrada_ID.delete(0,tk.END)
 

    def eliminar_ejercicio(self):

        self.pagina2 = ttk.Frame(self.pestanas)
        self.pestanas.add(self.pagina2, text="Eliminar")

        self.label1=ttk.Label(self.pagina2, text="ID del ejercicio:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.ID=tk.StringVar()
        self.entrada_ID=ttk.Entry(self.pagina2, textvariable=self.ID)
        self.entrada_ID.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.pagina2, text="Listado completo",command = print("Listar"))
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.pagina2, width=30, height=5)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)


class Grabar_dato:

    def __init__(self):

        self.ventana_grabar = tk.Toplevel()
        self.ventana_grabar.configure(bg = "#ffffff")
        self.label=tk.Label(self.ventana_grabar,
                text="Tiempo por ejercicio(s): ",
                bg='#ffffff')      
       
        self.ventana_grabar.geometry("+850+265")
        
        tamano_texto = font.Font(size=11 )

        self.label['font'] = tamano_texto
        self.label.grid(column=0, row=0)

        self.CI=tk.StringVar()
        self.entryCI=ttk.Entry(self.ventana_grabar, textvariable=self.CI    )
        self.entryCI.grid(column=1, row=0)
       

  

        self.boton1=tk.Button(self.ventana_grabar, text="Aceptar", command=print("aceptar"),
                bg='#ffffff',
                fg='#000000')
        self.boton1['font'] = tamano_texto
        self.boton1.grid(column=1, row=3,columnspan = 2)  

        self.vacio = tk.Label(self.ventana_grabar,
                 text= "\t",
                bg='#ffffff')
        self.vacio.grid(row=4,column=1)


        self.boton2=tk.Button(self.ventana_grabar, text="Comenzar a grabar", command=print("otro boton"),
                bg='#ffffff',
                fg='#000000')
        self.boton2['font'] = tamano_texto
        self.boton2.grid(column=1, row=5,columnspan = 2)
        
        self.vacio2 = tk.Label(self.ventana_grabar,
                 text= "\t",
                bg='#ffffff')
        self.vacio2.grid(row=6,column=3)


        self.ventana_grabar.resizable(False,False) 
