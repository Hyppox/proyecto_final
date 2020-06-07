import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext as st
import tkinter.font as font 
from tkinter import messagebox as mb
import time,sqlite3
import crear_bd_ejercicios as cbde
import toma_de_datos as tdd
import serial

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
        text="Continuar \n ...",
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
    def boton_confirmar(self):
        
        self.boton_configuracion = tk.Button(self.pagina1,
        text="Confirmar \n Tiempo y repeticiones",
        command = self.grabar_datos )
        self.boton_configuracion.grid(row=2,
        column=0)

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
        self.label=tk.Label(self.pagina1,
                text="Tiempo por ejercicio(s): ",
                bg='#ffffff')      
       
        #self.ventana_aprender.geometry("+850+265")
        
        tamano_texto = font.Font(size=11 )

        self.label['font'] = tamano_texto
        self.label.grid(column=0, row=4)
        
        self.label2=tk.Label(self.pagina1,
                text="Número de repeticiones: ",
                bg='#ffffff')      
       
        self.label2['font'] = tamano_texto
        self.label2.grid(column=0, row=5)
      
        self.t_ejercicio=tk.StringVar()
        self.contador =self.t_ejercicio.get()
        self.tiempo_ejercicio=ttk.Entry(self.pagina1, textvariable=self.t_ejercicio    )
        self.tiempo_ejercicio.grid(column=1, row=4,
        padx=5,
        pady=5)

        self.n_rep=tk.StringVar()
        self.entrada_rep=ttk.Entry(self.pagina1, textvariable=self.n_rep   )
        self.entrada_rep.grid(column=1, row=5)
        
        print(type(self.n_rep.get()))
  

        self.boton1=tk.Button(self.pagina1,
         text="Aceptar",
         command=self.aceptar,
                bg='#ffffff',
                fg='#000000')
        self.boton1['font'] = tamano_texto
        self.boton1.grid(column=1, row=6,columnspan = 2,
        padx=10,
        pady=10)  


        #self.etiqueta_nombre = tk.Label(self.pagina1,text = "......")
        #self.etiqueta_nombre.grid(row =4, column = 0)


        self.ventana_aprender.resizable(False,False) 
        self.num =0

    def comenzar(self):
        #mb.showinfo("Instrucciones...","Amarillo: espere \nVerde: Haga el ejercicio \nRojo: Fin")
        datos = tdd.aprendizaje(int(self.tiempo_ejercicio.get()),int(self.entrada_rep.get()))
        #print(datos)
        now = time.time() 
        repeticiones = str(int(self.entrada_rep.get())*2)
        limite = "after#"+ repeticiones
        t = int(self.tiempo_ejercicio.get())*1000
        self.etiqueta_grabar = tk.Label(self.ventana_aprender, text="Comienza")
        self.etiqueta_grabar.grid(row=1,column=1)
        if self.num == 0:
            self.num=1
            ahora = "Realice \n el movimiento"
            self.etiqueta_grabar.config(text = ahora,bg="green")
            ID =self.etiqueta_grabar.after(t, self.comenzar)
        
        else:
            self.num=0
            ahora = "ESPERE"
            self.etiqueta_grabar.config(text = ahora,bg="yellow")
            self.etiqueta_grabar.config()
            ID = self.etiqueta_grabar.after(2000, self.comenzar)

        if limite == ID:
            self.etiqueta_nombre.after_cancel(ID)
            mb.showinfo("Fin","Grabación finalizada")
            self.ventana_aprender.destroy()
    
    def cuenta_atras(self):
            # change text in label     

        self.etiqueta_grabar['text'] = self.contador
        if self.contador > 0:
        # call countdown again after 1000ms (1s)
            self.ventana_aprender.after(1000, self.cuenta_atras, int(self.contador)-1)





    def aceptar(self):

        tamano_texto = font.Font(size=12)
        self.tiempo = self.tiempo_ejercicio.get()
        self.repeticiones = self.entrada_rep.get()

        self.boton2=tk.Button(self.ventana_aprender, text="Comenzar a grabar",
         command=self.aprendizaje,
                bg='#ffffff',
                fg='#000000')
        self.boton2['font'] = tamano_texto
        self.boton2.grid(column=1, row=0,columnspan = 2)

        mb.showinfo("Confirmacón","Revise antes de comenzar a grabar: \nRepeticiones: "+self.repeticiones+" \nTiempo por ejercicio: "+self.tiempo+" segundo/s")
        print(self.tiempo+"-"+self.repeticiones)

    def aprendizaje(self):  
        try:
            tamano_texto = font.Font(size=12,
            weight = "bold" )

            # set up the serial line
            ser = serial.Serial('COM3', 115200)
            time.sleep(1)
            # Read and record the data
            #t = int(input("Ingrese tiempo de toma de datos: "))
            #n = int(input("ingrese el número de repeticiones: "))
            data =[]                       # empty list to store the data

            contador = 0
            num = int(self.n_rep.get())
            while contador < int(self.n_rep.get()):
                inicio = time.time()
                ahora = time.time()    
                print("comienza!")
                while (ahora-inicio) < int(self.t_ejercicio.get()):

                    b = ser.readline()         # read a byte string
                    string_n = b.decode()  # decode byte string into Unicode  
                    string = string_n.rstrip() # remove \n and \r

                    #print(string)
                    data.append(str(time.time())+","+string)           # add to the end of data list
                    time.sleep(0.1)            # wait (sleep) 0.1 seconds
                    ahora = time.time()
                #marcador = "----------" # -*10
                #data.append(marcador)
                contador +=1
                fin = time.time()
                print("La vuelta ",contador," duró: ",round(fin-inicio,2), "s")
                print("descanso 1.5s")
                time.sleep(1.5)
            for line in data:
                    
                print(line)
            ser.close()
            self.ver_datos = tk.Button(self.ventana_aprender,
            text = "Ver datos",
            command = self.ver_datos)
            self.ver_datos.grid(row=2, column=2)
            self.ver_datos['font'] = tamano_texto
            self.datos_grabados= data

            self.guardar_datos = tk.Button(self.ventana_aprender,
            text = "Guardar datos",
            command = self.registrar_datos)
            self.guardar_datos.grid(row=3, column=2)
            self.guardar_datos['font'] = tamano_texto
        except:
            mb.showinfo("ERROR...","No se detecta dispositivo \n de entrada")    
    def ver_datos(self):
        self.ventana_ver_datos =tk.Toplevel()
        self.ventana_ver_datos.title("Datos grabados")
        self.registrar_datos
       
        self.scrolledtext1=st.ScrolledText(self.ventana_ver_datos, width=50, height=15)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

        self.scrolledtext1.delete("1.0", tk.END) 
        self.scrolledtext1.insert(tk.END,  "EJERCICIO \n")    
        self.scrolledtext1.insert(tk.END, self.nomej.get()+ "\n")     
        for i in range(len(self.datos_grabados)):
            self.scrolledtext1.insert(tk.END, self.datos_grabados[i]+ "\n")
        
    def registrar_datos(self):
        self.ver_datos.grid_forget()
        self.guardar_datos.grid_forget()
        self.boton2.grid_forget()
        registro = open('registro_de_ejercicios.txt','a')
        registro.write(self.nomej.get()+"\n")
        for linea in self.datos_grabados:
            registro.write(self.nomej.get()+","+linea+'\n')
        registro.close()    

