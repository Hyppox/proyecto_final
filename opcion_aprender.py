import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext as st
import tkinter.font as font 
from tkinter import messagebox as mb
import time

class Aprender:

    def __init__(self):

        tamano_texto = font.Font(size=12,
         weight = "bold" )

        self.ventana_aprender = tk.Toplevel()

        self.ventana_aprender.title("Agregar nuevo ejercicio")
        self.ventana_aprender.geometry("+850+40")
        self.pestanas = ttk.Notebook(self.ventana_aprender)


        self.agregar_ejercicio()
        self.eliminar_ejercicio()

        self.pestanas.grid(column=0,
         row=0)

        self.ventana_aprender.resizable(False,False)

    def agregar_ejercicio(self):

        self.pagina1 = ttk.Frame(self.pestanas)

        self.pestanas.add(self.pagina1,
         text="Agregar")

        self.label1=ttk.Label(self.pagina1,
         text="Nombre del ejercicio:")

        self.label1.grid(column=0,
         row=0,
          padx=10, pady=10)

        self.nomej=tk.StringVar()
        self.entrada_ID=tk.Entry(self.pagina1, width=20,textvariable= self.nomej)
        self.entrada_ID.grid(column=1, row=0, padx=5, pady=5)
        self.entrada_ID.focus()


        self.boton_aceptar = tk.Button(self.pagina1,
        text="Aceptar",
        command = self.nombre_ejercicio)
        self.boton_aceptar.grid(row=1,
        column=0,
        padx = 10,
        pady = 10)

        self.boton_configuracion = tk.Button(self.pagina1,
        text="Comenzar aprendizaje",
        command = Grabar_dato )
        self.boton_configuracion.grid(row=2,
        column=0)

        self.ejercicio = tk.Label(self.pagina1,text="Ejercicio actual:")
        self.ejercicio.grid(row =1, column = 3)
    

        self.etiqueta_nombre = tk.Label(self.pagina1,text="NOMBRE DEL EJERCICIO")
        self.etiqueta_nombre.grid(row =2, column = 3)

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
        self.col = 0

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
      
        self.t_ejercicio=tk.StringVar()
        self.tiempo_ejercicio=ttk.Entry(self.ventana_grabar, textvariable=self.t_ejercicio    )
        self.tiempo_ejercicio.grid(column=1, row=1,
        padx=5,
        pady=5)

        self.n_rep=tk.StringVar()
        self.entrada_num=ttk.Entry(self.ventana_grabar, textvariable=self.n_rep   )
        self.entrada_num.grid(column=1, row=2)
        

  

        self.boton1=tk.Button(self.ventana_grabar,
         text="Aceptar",
         command=self.aceptar,
                bg='#ffffff',
                fg='#000000')
        self.boton1['font'] = tamano_texto
        self.boton1.grid(column=1, row=4,columnspan = 2,
        padx=10,
        pady=10)  


        self.vacio2 = tk.Label(self.ventana_grabar,
                 text= "\t",
                bg='#ffffff')
        self.vacio2.grid(row=7,column=3)

        self.etiqueta_nombre = tk.Label(self.ventana_grabar,text = "......")
        self.etiqueta_nombre.grid(row =4, column = 0)


        self.ventana_grabar.resizable(False,False) 

    def comenzar(self):
        #mb.showinfo("Instrucciones...","Amarillo: espere \nVerde: Haga el ejercicio \nRojo: Fin")
        
        if self.col == 0:
            self.col = 1
        else:
            self.col = 1

        self.etiqueta_nombre.config(text = self.col)
        self.etiqueta_nombre.after(1000, self.comenzar)

    def aceptar(self):
        tamano_texto = font.Font(size=12)
        self.tiempo = self.tiempo_ejercicio.get()
        self.repeticiones = self.entrada_num.get()

        self.boton2=tk.Button(self.ventana_grabar, text="Comenzar a grabar", command=self.comenzar,
                bg='#ffffff',
                fg='#000000')
        self.boton2['font'] = tamano_texto
        self.boton2.grid(column=1, row=6,columnspan = 2)

        mb.showinfo("Confirmacón","Revise antes de comenzar a grabar: \nRepeticiones: "+self.repeticiones+" \nTiempo por ejercicio: "+self.tiempo+" segundo/s")
        print(self.tiempo+"-"+self.repeticiones)