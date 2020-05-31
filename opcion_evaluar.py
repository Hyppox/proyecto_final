import tkinter as tk
import keyboard as kb 
import opcion_pacientes as op
from tkinter import messagebox as mb
from tkinter import ttk
import consultar as ct
import tkinter.font as font
import opcion_evaluar_no_agregar
import opcion_pacientes
import crear_carpeta as ccbd
import crear_basededatos as cbd
import sqlite3
from PIL import ImageTk,Image 
import sensores 
# pylint: disable=E1101
 

class Evaluar:
    def __init__(self):
        self.ingrese_CI = tk.Toplevel()
        self.ingrese_CI.configure(bg = "#ffffff")
        self.label=tk.Label(self.ingrese_CI,
                text="Ingrese CI del paciente:",
                bg='#ffffff')      
       
        self.ingrese_CI.geometry("+350+463")
        
        tamano_texto = font.Font(size=12 )

        self.label['font'] = tamano_texto
        self.label.grid(column=1, row=1)

        self.CI=tk.StringVar()
        self.entryCI=ttk.Entry(self.ingrese_CI, textvariable=self.CI    )
        self.entryCI.grid(column=2, row=1)
       

        self.vacio = tk.Label(self.ingrese_CI,
                 text= "\t",
                bg='#ffffff')
        self.vacio.grid(row=0,column=0)
        self.vacio2 = tk.Label(self.ingrese_CI,
                 text= "\t",
                bg='#ffffff')
        self.vacio2.grid(row=3,column=3)
        
       
        self.texto = tk.Label(self.ingrese_CI,
                 text= "\t",
                bg='#ffffff')
        self.texto.grid(row=0,column=0)


  

        self.boton1=tk.Button(self.ingrese_CI, text="Aceptar", command=self.aceptar,
                bg='#ffffff',
                fg='#000000')
        self.boton1['font'] = tamano_texto
        self.boton1.grid(column=1, row=2,columnspan = 2)  

        self.boton2=tk.Button(self.ingrese_CI, text="Agregar nuevo", command=self.nuevopaciente,
                bg='#ffffff',
                fg='#000000')
        self.boton2['font'] = tamano_texto
        self.boton2.grid(column=2, row=2,columnspan = 2) 
        self.ingrese_CI.resizable(False,False) 

    def aceptar(self):

        datos=(self.CI.get(), )
        self.respuesta=ct.Consultar.consulta(datos)
        
        if len(self.respuesta)>0 and datos[0]!='':

            lineas = ["Usuario registrado",self.respuesta[0][1]]
            mb.showinfo('Continuar...', "\n".join(lineas))
        else:

            mb.showinfo("Algo fue mal...","No existe usuario registrado con dicho número de CI \n \n Revise que los datos estén bien: \n  -Puede usar la lista de pacientes en ventana 'Pacientes'\n   -Puede agregar el paciente")
        
        if len(self.respuesta)>0 and datos[0]!='':
            
            self.nuevo = tk.Toplevel()
            self.nuevo.configure(bg = "#ffffff")
            self.nuevo.geometry("+480+610")
            self.nuevo.title("Evaluación del paciente")
            self.tamano_texto = font.Font(size=12 )

            self.labelframe1=tk.LabelFrame(self.nuevo,
            text="Usuario registrado: " )        
            self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
            self.labelframe1['font'] = self.tamano_texto

            self.boton4=tk.Button(self.labelframe1,
            text="Nueva evaluacion para "+self.respuesta[0][1],
            command= self.evaluar_paciente)
            self.boton4.grid(column=1, row=0, padx=4, pady=4)
            self.boton4['font'] = self.tamano_texto
            
            self.boton5=tk.Button(self.labelframe1,
            text="Ver registro de "+self.respuesta[0][1],
            command= print("registro"))
            self.boton5.grid(column=1, row=1, padx=4, pady=4)
            self.boton5['font'] = self.tamano_texto
            self.nuevo.resizable(False,False)

            
        else:
            pass
    def evaluar_paciente(self):
        self.ventana_evaluar = tk.Toplevel() 
        self.ventana_evaluar.configure(bg = "#ffffff")
        self.ventana_evaluar.geometry("+900+610")
        self.ventana_evaluar.title("Nueva evaluación")
        self.tamano_texto = font.Font(size=12 )

        self.indicaciones = tk.Label(self.ventana_evaluar, text ="Repita n veces los siguientes ejercicios: ")
        self.indicaciones.grid(row=0,column=0)

        self.imagen_ejercicios = tk.Label(self.ventana_evaluar, text ="Aqui va la imagen")
        self.imagen_ejercicios.grid(row=1,column=0)
        
        self.boton_evaluar = tk.Button(self.ventana_evaluar, text="Aceptar",
        command =sensores.Sensores )
        self.boton_evaluar.grid(row=3,column=0)
        
        self.vacio = tk.Label(self.ventana_evaluar,
                 text= "\t",
                bg='#ffffff')
        self.vacio.grid(row=2,column=0)

        self.boton_otros = tk.Button(self.ventana_evaluar, text= "Otros")
        self.boton_otros.grid(row=3,column=1)
        self.ventana_evaluar.resizable(False,False)

        
    def nuevopaciente(self):

        self.nuevo = tk.Toplevel()
        self.nuevo.configure(bg = "#ffffff")
        self.nuevo.geometry("+480+500")
        self.nuevo.title("Nuevo paciente")
        self.tamano_texto = font.Font(size=12 )

        self.labelframe1=tk.LabelFrame(self.nuevo,
         text="Paciente:" )        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.labelframe1['font'] = self.tamano_texto
        
        self.label1=ttk.Label(self.labelframe1,
         text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombrecarga=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1,
         textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
        self.label1['font'] = self.tamano_texto


        self.label2=tk.Label(self.labelframe1,
         text="CI:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cargarpaciente=tk.StringVar()
        self.entryCI=ttk.Entry(self.labelframe1,
         textvariable=self.cargarpaciente)
        self.entryCI.grid(column=1, row=1, padx=4, pady=4)
        self.label2['font'] = self.tamano_texto


        self.label2=ttk.Label(self.labelframe1,
         text="Edad:")        
        self.label2.grid(column=0, row=2, padx=4, pady=5)
        self.edadpaciente=tk.StringVar()
        self.entryedad=ttk.Entry(self.labelframe1,
         textvariable=self.edadpaciente)
        self.entryedad.grid(column=1, row=2, padx=4, pady=6)
        self.label2['font'] = self.tamano_texto

        self.label2=tk.Label(self.labelframe1,
         text="Sexo (H/M):")        
        self.label2.grid(column=0, row=3, padx=4, pady=5)
        self.sexopaciente=tk.StringVar()
        self.entrysexopaciente=ttk.Entry(self.labelframe1,
         textvariable=self.sexopaciente)
        self.entrysexopaciente.grid(column=1, row=3, padx=4, pady=6)
        self.label2['font'] = self.tamano_texto

        self.boton3=tk.Button(self.labelframe1,
         text="Confirmar",
          command= self.agregar)
        self.boton3.grid(column=1, row=4, padx=4, pady=4)
        self.boton3['font'] = self.tamano_texto
        self.nuevo.resizable(False,False)
    def agregar(self):
        datos=(self.nombrecarga.get(),
         self.cargarpaciente.get(),
         self.edadpaciente.get(),
         self.sexopaciente.get())

        self.alta(datos)

        mb.showinfo("Información", "Los datos fueron cargados \n Revise que estén correctos antes de continuar ")
        self.entrynombre.delete(0, 'end')
        self.entryCI.delete(0, 'end')
        self.entryedad.delete(0, 'end')
        self.entrysexopaciente.delete(0, 'end')
    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into pacientes(nombre,CI,edad,sexo) values (?,?,?,?)"
        self.creartablapaciente(datos[1])
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    
    def creartablapaciente(self,id):
            ruta = 'bases_de_datos/'+id+'.db'
            conexion=sqlite3.connect(ruta)
            try:
                conexion.execute("""create table id (
                                        codigo integer primary key AUTOINCREMENT,
                                        fecha text,
                                        datos real
                                    )""")
                print("s ")                        
            except sqlite3.OperationalError:
                print("La  ")                    
            conexion.close()  

    def abrir(self):
        try:
            ccbd.bases_de_datos
            cbd
            conexion=sqlite3.connect("bases_de_datos/pacientes.db")
            return conexion
        except:

            conexion=sqlite3.connect("bases_de_datos/pacientes.db")
            return(conexion)
 

    def consultar(self):

        datos=(self.CI.get(), )
        self.respuesta=ct.Consultar.consulta(datos)
        
        if len(self.respuesta)>0 and datos[0]!='':

            lineas = ["Usuario registrado",self.respuesta[0][1]]
            mb.showinfo('Continuar...', "\n".join(lineas))
            return self.respuesta
        else:
            command = opcion_pacientes.BDPaciente
            command
            mb.showinfo("Algo salió mal...","\n El usuario no está registrado")
            return self.respuesta
