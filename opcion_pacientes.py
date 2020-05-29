import tkinter as tk
import crear_carpeta as ccbd
import crear_basededatos as cbd
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import tkinter.font as font
import opcion_evaluar as oe
import sqlite3
from os import remove
# pylint: disable=E1101
class BDPaciente:
    def __init__(self):
        self.BDpacientes=Pacientes()
        self.ventana_pacientes=tk.Toplevel()
        self.ventana_pacientes.configure(bg = "#ffffff")
        self.tamano_texto = font.Font(size=12 )

        self.ventana_pacientes.title("Pacientes")
        self.cuaderno1 = ttk.Notebook(self.ventana_pacientes)

        #self.carga_pacientes() #Se está agregando los usuarios desde la opcion evaluar/agregar, desde aqui no carga variable sexopaciente


        self.consulta_por_CI()
        self.listado_completo()
        self.borrado()
        self.modificar()

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana_pacientes.geometry("+450+40")
  
        self.ventana_pacientes.resizable(False,False)
        self.ventana_pacientes.mainloop() 

    
    
    def abrirBD(self):

        self.ventana2= tk.Toplevel()
        self.ventana2.title("Datos del paciente "+self.CI)

    #checkpoint
    #Consulta para carga

    def revisar_entrada(self):

        entrada_sexo = str(self.sexopaciente.get())
        if entrada_sexo == "M" or entrada_sexo == "m" or entrada_sexo ==  "H"  or entrada_sexo == "h":
            pass
            self.agregar
        else:
            print(type(str(entrada_sexo)))
            print(entrada_sexo)
            lineas = ["Revise Celda: Sexo  ",""]
            mb.showinfo('Text', "\n".join(lineas))


    def carga_pacientes(self):
        #introducir datos
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Agregar pacientes")

        self.labelframe1=tk.LabelFrame(self.pagina1,
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

        self.boton1=tk.Button(self.labelframe1,
         text="Confirmar",
          command=self.agregar)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)
        self.boton1['font'] = self.tamano_texto

        
    def agregar(self):
        datos=(self.nombrecarga.get(),
         self.cargarpaciente.get(),
         self.edadpaciente.get(),
         self.sexopaciente.get())

        self.BDpacientes.alta(datos)

        mb.showinfo("Información", "Los datos fueron cargados")
        
        self.entrynombre.delete(0, 'end')
        self.entryCI.delete(0, 'end')
        self.entryedad.delete(0, 'end')
        self.entrysexopaciente.delete(0, 'end')
    def consulta_por_CI(self):

        self.pagina2 = ttk.Frame(self.cuaderno1)

        self.cuaderno1.add(self.pagina2, text="Consulta por CI")

        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Paciente")
        self.labelframe1.grid(column=0, row=0, padx=5   , pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="CI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.CI=tk.StringVar()
        self.consultaCI=ttk.Entry(self.labelframe1, textvariable=self.CI)
        self.consultaCI.grid(column=1, row=0, padx=4, pady=4)


        self.label2=ttk.Label(self.labelframe1, text="Nombre:")             
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.consultanombre=ttk.Entry(self.labelframe1,
         textvariable=self.nombre,
          state="readonly")
        self.consultanombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Edad:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.edad=tk.StringVar()
        self.consultaedad=ttk.Entry(self.labelframe1,
         textvariable=self.edad,
          state="readonly")
        self.consultaedad.grid(column=1, row=2, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Sexo (H/M):")        
        self.label2.grid(column=0, row=3, padx=4, pady=5)
        self.sexopaciente=tk.StringVar()
        self.consultasexo=ttk.Entry(self.labelframe1,
         textvariable=self.sexopaciente,
          state = "readonly")
        self.consultasexo.grid(column=1, row=3, padx=4, pady=6)


        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)
        

    


    def consultar(self):
        datos=(self.CI.get(), )
        respuesta=self.BDpacientes.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][1])
            self.CI.set(respuesta[0][0])
            self.edad.set(respuesta[0][2])
            self.sexopaciente.set(respuesta[0][3])
            return(respuesta)
        else:
            self.consultaCI.delete(0, 'end')
            self.consultanombre.delete(0, 'end')
            self.consultaedad.delete(0, 'end')
            self.consultasexo.delete(0, 'end')

            mb.showinfo("Información", "No existe un paciente con dicho CI")

    def listado_completo(self):

        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.labelframe1=ttk.LabelFrame(self.pagina3, text="Paciente")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe1, width=50, height=15)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):

        respuesta=self.BDpacientes.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "CI:"+str(fila[0])+
                                              "\nNombre:"+fila[1]+
                                              "\nEdad:"+str(fila[2])+
                                              "\nSexo:"+str(fila[3])+"\n\n")

    def borrado(self):

        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de pacientes")

        self.labelframe1=ttk.LabelFrame(self.pagina4, text="Paciente")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="CI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.CIborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.CIborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.CIborra.get(), )
        cantidad=self.BDpacientes.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el paciente con dicho CI")
        else:
            mb.showinfo("Información", "No existe un paciente con dicho CI")

    def modificar(self):

        #crea nueva pestaña
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar paciente")
        self.labelframe1=ttk.LabelFrame(self.pagina5, text="Paciente")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="CI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.CImod=tk.StringVar()
        self.entryCI=ttk.Entry(self.labelframe1, textvariable=self.CImod)
        self.entryCI.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nommod=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nommod)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Edad:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.edadmod=tk.StringVar()
        self.entryedad=ttk.Entry(self.labelframe1, textvariable=self.edadmod)
        self.entryedad.grid(column=1, row=2, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Sexo (H/M):")        
        self.label2.grid(column=0, row=3, padx=4, pady=5)
        self.sexomod=tk.StringVar()
        self.entrysexo=ttk.Entry(self.labelframe1,
         textvariable=self.sexomod,)
        self.entrysexo.grid(column=1, row=3, padx=4, pady=6)



        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def modifica(self):
        datos=(self.CImod.get(),self.nommod.get(), self.edadmod.get(),self.sexomod.get(),self.CImod.get())
        cantidad=self.BDpacientes.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el paciente")
        else:
            mb.showinfo("Información", "No existe un paciente con dicho CI")

    def consultar_mod(self):
        datos=(self.CImod.get(),)
        respuesta=self.BDpacientes.consulta(datos)
        if len(respuesta)>0:
            self.CImod.set(respuesta[0][0])
            self.nommod.set(respuesta[0][1])
            self.edadmod.set(respuesta[0][2])
            self.sexomod.set(respuesta[0][3])
        else:
            self.entrynombre.delete(0, 'end')
            self.entryedad.delete(0, 'end')
            self.entryCI.delete(0, 'end')
            self.entrysexo.delete(0, 'end')
            mb.showinfo("Información", "No existe un paciente con dicho CI")


class Pacientes:
    def __init__(self):
        self.abrir
    def abrir(self):
        try:
            ccbd.bases_de_datos
            cbd
            conexion=sqlite3.connect("bases_de_datos/pacientes.db")
            return conexion
        except:

            conexion=sqlite3.connect("bases_de_datos/pacientes.db")
            return(conexion)
            pass
    
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

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into pacientes(nombre,CI,edad,sexo) values (?,?,?,?)"
        self.creartablapaciente(datos[1])
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select CI, nombre,edad,sexo from pacientes where CI=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select CI, nombre,edad,sexo CI from pacientes"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from pacientes where CI=?"
            id=(datos[0])
            remove('bases_de_datos/'+id+'.db')
            cursor.execute(sql, datos)
            cone.commit()
            return  cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update pacientes set  CI=? , nombre=? , edad=? where CI=?"
            cursor.execute(sql, datos)
            cone.commit()
            return 1 # retornamos la cantidad de filas modificadas            
        except:
            cone.close()
 