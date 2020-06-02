import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext as st
import tkinter.font as font 
from tkinter import messagebox as mb
import time,sqlite3
import crear_bd_ejercicios as cbde

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
        command = self.grabar_datos )
        self.boton_configuracion.grid(row=2,
        column=0)

        self.ejercicio = tk.Label(self.pagina1,text="Ejercicio actual:")
        self.ejercicio.grid(row =1, column = 3)
    

        self.etiqueta_nombre = tk.Label(self.pagina1,text="NOMBRE DEL EJERCICIO")
        self.etiqueta_nombre.grid(row =2, column = 3)
    def abrir(self):
        try:
            cbde
            conexion=sqlite3.connect("bases_de_datos/ejercicios.db")
            return conexion
        except:

            conexion=sqlite3.connect("bases_de_datos/ejercicios.db")
            return(conexion)
            pass

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into ejercicios(nombre) values (?)"
        self.creartablapaciente(datos[1])
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    
    def nombre_ejercicio(self):
        cbde

        nombre = self.nomej.get()
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

    def devolver_nombre(self):
        nombre =self.nomej.get()
        print(nombre)
        return nombre

    def grabar_datos(self):
        self.label=tk.Label(self.ventana_aprender,
                text="Tiempo por ejercicio(s): ",
                bg='#ffffff')      
       
        #self.ventana_aprender.geometry("+850+265")
        
        tamano_texto = font.Font(size=11 )

        self.label['font'] = tamano_texto
        self.label.grid(column=0, row=1)
        
        self.label2=tk.Label(self.ventana_aprender,
                text="Número de repeticiones: ",
                bg='#ffffff')      
       
        self.label2['font'] = tamano_texto
        self.label2.grid(column=0, row=4)
      
        self.t_ejercicio=tk.StringVar()
        self.tiempo_ejercicio=ttk.Entry(self.ventana_aprender, textvariable=self.t_ejercicio    )
        self.tiempo_ejercicio.grid(column=1, row=1,
        padx=5,
        pady=5)

        self.n_rep=tk.StringVar()
        self.entrada_rep=ttk.Entry(self.ventana_aprender, textvariable=self.n_rep   )
        self.entrada_rep.grid(column=1, row=2)
        

  

        self.boton1=tk.Button(self.ventana_aprender,
         text="Aceptar",
         command=self.aceptar,
                bg='#ffffff',
                fg='#000000')
        self.boton1['font'] = tamano_texto
        self.boton1.grid(column=1, row=4,columnspan = 2,
        padx=10,
        pady=10)  


        self.etiqueta_nombre = tk.Label(self.ventana_aprender,text = "......")
        self.etiqueta_nombre.grid(row =4, column = 0)


        self.ventana_aprender.resizable(False,False) 
        self.num =0

    def comenzar(self):
        #mb.showinfo("Instrucciones...","Amarillo: espere \nVerde: Haga el ejercicio \nRojo: Fin")
        now = time.time() 
        repeticiones = str(int(self.entrada_rep.get())*2)
        limite = "after#"+ repeticiones
        t = int(self.tiempo_ejercicio.get())*1000
        if self.num == 0:
            self.num=1
            ahora = "Realice \n el movimiento"
            self.etiqueta_nombre.config(text = ahora,bg="green")
            ID =self.etiqueta_nombre.after(t, self.comenzar)
        
        else:
            self.num=0
            ahora = "ESPERE"
            self.etiqueta_nombre.config(text = ahora,bg="yellow")
            ID = self.etiqueta_nombre.after(1000, self.comenzar)

        print(type(ID))
        print(ID)
        print(time.time()-now)
        if limite == ID:
            self.etiqueta_nombre.after_cancel(ID)
            mb.showinfo("Fin","Grabación finalizada")
            self.ventana_aprender.destroy()
    def aceptar(self):
        tamano_texto = font.Font(size=12)
        self.tiempo = self.tiempo_ejercicio.get()
        self.repeticiones = self.entrada_rep.get()

        self.boton2=tk.Button(self.ventana_aprender, text="Comenzar a grabar", command=self.comenzar,
                bg='#ffffff',
                fg='#000000')
        self.boton2['font'] = tamano_texto
        self.boton2.grid(column=1, row=6,columnspan = 2)

        mb.showinfo("Confirmacón","Revise antes de comenzar a grabar: \nRepeticiones: "+self.repeticiones+" \nTiempo por ejercicio: "+self.tiempo+" segundo/s")
        print(self.tiempo+"-"+self.repeticiones)
        time.sleep(2)