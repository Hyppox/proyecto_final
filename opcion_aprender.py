import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext as st

class Aprender:

    def __init__(self):

        self.ventana_aprender = tk.Toplevel()

        self.ventana_aprender.title("Agregar nuevo ejercicio")
        self.ventana_aprender.geometry("+850+40")
        self.pestanas = ttk.Notebook(self.ventana_aprender)


        self.agregar_ejercicio()
        self.eliminar_ejercicio()

        self.pestanas.grid(column=0, row=0, padx=10, pady=10)
        self.ventana_aprender.mainloop()


    def agregar_ejercicio(self):

        self.pagina1 = ttk.Frame(self.pestanas)

        self.pestanas.add(self.pagina1, text="Agregar")

        self.marco=ttk.LabelFrame(self.pagina1, text="Ejercicio")
        self.marco.grid(column=0, row=0, padx=5   , pady=10)
        
        self.label1=ttk.Label(self.marco, text="ID del ejercicio:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.ID=tk.StringVar()
        self.entrada_ID=ttk.Entry(self.marco, textvariable=self.ID)
        self.entrada_ID.grid(column=1, row=0, padx=4, pady=4)

        self.boton_aceptar = tk.Button(self.marco,text="Aceptar",command = print("Aceptar"))

    def eliminar_ejercicio(self):

        self.pagina2 = ttk.Frame(self.pestanas)
        self.pestanas.add(self.pagina2, text="Eliminar")

        self.marco=ttk.LabelFrame(self.pagina2, text="Ejercicios aprendidos")
        self.marco.grid(column=0, row=0, padx=5   , pady=10)
        
        self.label1=ttk.Label(self.marco, text="ID del ejercicio:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.ID=tk.StringVar()
        self.entrada_ID=ttk.Entry(self.marco, textvariable=self.ID)
        self.entrada_ID.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.marco, text="Listado completo",command = print("Listar"))
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.marco, width=30, height=15)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
