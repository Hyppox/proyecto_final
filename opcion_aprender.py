import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext as st
import tkinter.font as font 
from tkinter import messagebox as mb

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

        self.ventana_aprender.resizable(False,False)
    def agregar_ejercicio(self):

        self.pagina1 = ttk.Frame(self.pestanas)

        self.pestanas.add(self.pagina1, text="Agregar")

        self.label1=ttk.Label(self.pagina1, text="Nombre del ejercicio:")
        self.label1.grid(column=0, row=0, padx=5, pady=5)

        self.nomej=tk.StringVar()
        self.entrada_ID=tk.Entry(self.pagina1, width=20,textvariable= self.nomej)
        self.entrada_ID.grid(column=1, row=0, padx=5, pady=5)
        self.entrada_ID.focus()


        self.boton_aceptar = tk.Button(self.pagina1,
        text="Aceptar",
        command = self.nombre_ejercicio)
        self.boton_aceptar.grid(row=1,
        column=0)

        self.boton_configuracion = tk.Button(self.pagina1,
        text="Comenzar aprendizaje",
        command = Grabar_dato )
        self.boton_configuracion.grid(row=2,
        column=0)

        self.ejercicio = tk.Label(self.pagina1,text="Ejercicio actual:")
        self.ejercicio.grid(row =1, column = 3)
    

        self.etiqueta_nombre = tk.Label(self.pagina1,text="NOMBRE DEL EJERCICIO")
        self.etiqueta_nombre.grid(row =2, column = 3)
    def comenzar(self):
        if self.etiqueta_nombre.cget("text") == "NOMBRE DEL EJERCICIO":
            #mb.showinfo("Información", "Ingrese nombre para el ejercicio ")
            print("no pasa nada")
        else:
            print("hello")
            self.grabar_dato
    def grabar_dato(self):
            Grabar_dato

    def nombre_ejercicio(self):
        nombre = self.nomej.get()
        print(nombre)
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
        self.label.grid(column=0, row=1)
        
        self.label2=tk.Label(self.ventana_grabar,
                text="Número de repeticiones: ",
                bg='#ffffff')      
       
        self.label2['font'] = tamano_texto
        self.label2.grid(column=0, row=2)
      
        self.nom_ejercicio=tk.StringVar()
        self.entrada_ejercicio=ttk.Entry(self.ventana_grabar, textvariable=self.nom_ejercicio    )
        self.entrada_ejercicio.grid(column=1, row=1)

        self.n_rep=tk.StringVar()
        self.entrada_num=ttk.Entry(self.ventana_grabar, textvariable=self.n_rep   )
        self.entrada_num.grid(column=1, row=2)
        

  

        self.boton1=tk.Button(self.ventana_grabar, text="Aceptar", command=print("aceptar"),
                bg='#ffffff',
                fg='#000000')
        self.boton1['font'] = tamano_texto
        self.boton1.grid(column=1, row=4,columnspan = 2)  

        self.vacio = tk.Label(self.ventana_grabar,
                 text= "\t",
                bg='#ffffff')
        self.vacio.grid(row=5,column=1)


        self.boton2=tk.Button(self.ventana_grabar, text="Comenzar a grabar", command=print("otro boton"),
                bg='#ffffff',
                fg='#000000')
        self.boton2['font'] = tamano_texto
        self.boton2.grid(column=1, row=6,columnspan = 2)
        
        self.vacio2 = tk.Label(self.ventana_grabar,
                 text= "\t",
                bg='#ffffff')
        self.vacio2.grid(row=7,column=3)


        self.ventana_grabar.resizable(False,False) 
