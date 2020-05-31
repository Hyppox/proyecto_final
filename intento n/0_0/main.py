import sqlite3,keyboard,time, serial,sys,os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from PIL import ImageTk, Image
from vpython import*
import numpy as np
from os import remove


try:
    os.mkdir('bases_de_datos')
except:
    pass


class Principal:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Rehab 1.0")
        self.ventana.geometry('300x100')
        self.botones()
        self.ventana.resizable(False,False)

        self.ventana.mainloop()
    def salir(self):
        self.ventana.destroy()
    def botones(self):
        v1 = tk.Label(self.ventana,text="\t")
        v1.grid(row=0,column=5)
        v2 = tk.Label(self.ventana,text="\t \t")
        v2.grid(row=0,column=1)
        self.botonPacientes = ttk.Button(self.ventana,  text = "Pacientes" , command= BDPaciente)
        self.botonPacientes.grid(row=1,column=2)
        self.botoninfo =  ttk.Button(self.ventana,  text = "info" , command= print("hola"))
        self.botoninfo.grid(row=2,column=2)
        self.botoncerrar = ttk.Button(self.ventana, text = "Cerrar", command = self.salir)
        self.botoncerrar.grid(row=3,column=2)

class BDPaciente:
    def __init__(self):
        self.articulo1=Pacientes()
        self.ventana_pacientes=tk.Toplevel()
        self.ventana_pacientes.title("Rehab 1.0")
        self.cuaderno1 = ttk.Notebook(self.ventana_pacientes)
        self.sensores = Sensores                
        self.carga_pacientes()
        self.consulta_por_CI()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.aplicacion()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana_pacientes.resizable(False,False)
        self.ventana_pacientes.mainloop() 
    
    
    #PENDIENTE
    def crear_ventana_pacientes(self):
        self.ventana_pacientes=tk.Tk()
        self.ventana_pacientes.title("Rehab 1.0")
        self.cuaderno1 = ttk.Notebook(self.ventana_pacientes)
        self.sensores = Sensores                
        self.carga_pacientes()
        self.consulta_por_CI()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.aplicacion()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana_pacientes.resizable(False,False)
    def abrirBD(self):
        self.ventana2= tk.Toplevel()
        self.ventana2.title("Datos del paciente "+self.CI)

    #checkpoint
    #Consulta para carga
    
    def grabardatos(self):
        datos=(self.cargarpaciente.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.datos = respuesta
        else:
            self.datos =('','','')
            self.nombrecarga.set('')
            self.cargarpaciente.set('')
            self.edadpaciente.set('')
            mb.showinfo("Información", "No existe un paciente con dicho CI")
   
    def carga_pacientes(self):
        #introducir datos
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Agregar pacientes")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Paciente: ")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombrecarga=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="CI:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cargarpaciente=tk.StringVar()
        self.entryCI=ttk.Entry(self.labelframe1, textvariable=self.cargarpaciente)
        self.entryCI.grid(column=1, row=1, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Edad:")        
        self.label2.grid(column=0, row=2, padx=4, pady=5)
        self.edadpaciente=tk.StringVar()
        self.entryedad=ttk.Entry(self.labelframe1, textvariable=self.edadpaciente)
        self.entryedad.grid(column=1, row=2, padx=4, pady=6)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        
    def agregar(self):
        datos=(self.nombrecarga.get(), self.cargarpaciente.get(),self.edadpaciente.get())
        self.articulo1.alta(datos)

        mb.showinfo("Información", "Los datos fueron cargados")
        
        self.nombre.set("")
        self.CI.set("")
        self.edad.set("")

    def consulta_por_CI(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por CI")
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Paciente")
        self.labelframe1.grid(column=0, row=0, padx=5   , pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="CI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.CI=tk.StringVar()
        self.entryCI=ttk.Entry(self.labelframe1, textvariable=self.CI)
        self.entryCI.grid(column=1, row=0, padx=4, pady=4)


        self.label2=ttk.Label(self.labelframe1, text="Nombre:")             
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Edad:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.edad=tk.StringVar()
        self.entryedad=ttk.Entry(self.labelframe1, textvariable=self.edad, state="readonly")
        self.entryedad.grid(column=1, row=2, padx=4, pady=4)


        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        
        self.grabar = ttk.LabelFrame(self.pagina1, text = "Grabar datos")
        self.grabar.grid(row=0,column=1)
        self.botonGrabar = ttk.Button(self.grabar, text = "Grabar")
        self.botonGrabar.grid(row = 0, column=0)
        self.botonStop = ttk.Button(self.grabar, text = "Detener")
        self.botonStop.grid(row = 0, column=1)

    def grabar(self):
        datos=(self.CI.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][1])
            self.CI.set(respuesta[0][0])
            self.edad.set(respuesta[0][2])
            
        else:
            self.nombre.set('')
            self.CI.set('')
            self.edad.set('')
            mb.showinfo("Información", "No existe un paciente con dicho CI")
        



    def consultar(self):
        datos=(self.CI.get(), )
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][1])
            self.CI.set(respuesta[0][0])
            self.edad.set(respuesta[0][2])
            return(respuesta)
        else:
            self.nombre.set('')
            self.CI.set('')
            self.edad.set('')
            mb.showinfo("Información", "No existe un paciente con dicho CI")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="Paciente")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe1, width=30, height=15)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "CI:"+str(fila[0])+
                                              "\nNombre:"+fila[1]+
                                              "\nEdad:"+str(fila[2])+"\n\n")

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
        cantidad=self.articulo1.baja(datos)
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
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.CImod.get(),self.nommod.get(), self.edadmod.get(),self.CImod.get())
        cantidad=self.articulo1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el paciente")
        else:
            mb.showinfo("Información", "No existe un paciente con dicho CI")

    def consultar_mod(self):
        datos=(self.CImod.get(),)
        respuesta=self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.CImod.set(respuesta[0][0])
            self.nommod.set(respuesta[0][1])
            self.edadmod.set(respuesta[0][2])
            
        else:
            self.CImod.set('')
            self.nommod.set('')
            self.edadmod.set('')

            mb.showinfo("Información", "No existe un paciente con dicho CI")

    def aplicacion(self):
        self.pagina6 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina6, text="Jugar/evaluar")
        self.labelframe1=ttk.LabelFrame(self.pagina6, text="Jugar")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #self.label1=ttk.Label(self.labelframe1, text="INICIO")
        #self.label1.grid(column=0, row=0, padx=4, pady=4)


        self.boton1=ttk.Button(self.labelframe1, text="INICIAR", command=Sensores)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
class Pacientes:
    def __init__(self):
        self.abrir
    def abrir(self):
        try:
            conexion=sqlite3.connect("bases_de_datos/pacientes.db")
            return conexion
        except:
            CrearBD()
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
        sql="insert into pacientes(nombre,CI,edad) values (?,?,?)"
        self.creartablapaciente(datos[1])
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select CI, nombre,edad from pacientes where CI=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select CI, nombre,edad, CI from pacientes"
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
    
class CrearBD:
    def __init__(self):
        self.crearbd
    def crearbd(self):

        conexion=sqlite3.connect("bases_de_datos/pacientes.db")
        try:
            conexion.execute("""create table pacientes(
                                        CI integer,
                                        nombre text,
                                        edad integer,


                                    )""")
            print("se creo la tabla pacientes")                        
        except sqlite3.OperationalError:
            print("La base de datos ya existe")                    
        conexion.close()
class LeerDatosSensores:
    def __init__(self):
        super().__init__()
        self.abrirArduino
    def abrirArduino(self):
        self.arduino = serial.Serial('com6', 115200)
    def leerdatos(self):
        
        self.LineArdu = self.arduino.readline()
        self.LineArdu = self.LineArdu.decode('utf-8')
        time.sleep(2)
        self.datos = self.LineArdu.split(',')
        return self.datos
class Sensores:
    def __init__(self):
        self.sensores()

    def sensores(self):

        scene.range=5
        toRad=2*np.pi/360
        toDeg=1/toRad
        y = vector(0,1,0)
        yawmax=0

        scene.append_to_caption('\n\n')

        #scene.forward=vector(-1,-1,-1)
        
        scene.width=1000
        scene.height=1000

        scene.background=color.white

        #mano = box (pos = vector(0,0,0),length=5, height=0.5, width=2, color = color.purple, opacity = .8, axis = vector(0,0,0))


        arduino = serial.Serial('com6', 115200)
        LineArdu = arduino.readline()
        LineArdu = LineArdu.decode('utf-8')
        time.sleep(2)
        datos = LineArdu.split(',')

        mano1 = box (pos = vector(0,0,0),length=4, height=0.6, width=4, color = color.orange, opacity = 1)


        sensor =  box (pos = vector(0,.1,0),length=1, height=.6, width=1, color = color.red, opacity = .5)



        d1 = box (pos = vector(3,0,-1.5),length=3.5, height=0.5, width=.9, color = color.orange, opacity = 1)
        d2 = box (pos = vector(3,0,-0.5),length=4.5, height=0.5, width=.9, color = color.orange, opacity = 1)
        d3 = box (pos = vector(3,0,0.5),length=5, height=0.5, width=.9, color = color.orange, opacity = 1)
        d4 = box (pos = vector(3,0,1.5),length=4, height=0.5, width=.9, color = color.orange, opacity = 1)
        d5 = box (pos = vector(-1,0,2.5),length=4, height=0.5, width=.9, color = color.orange, opacity = 1)

        antebrazo = box (pos = vector(-1,0,0), length=2.5, height=0.5, width=3, color = color.yellow, opacity = .8)

        #ref = box (pos = vector(4,0,0), length=1, height=0.5, width=3, color = color.black, opacity = 1)
        ref = box (pos = vector(-5,0,0),length=10, height=0.1, width=.1, color = color.black, opacity = 1)

        road = box (pos = vector(-5,-4,0),length=1000, height=0.1, width=20, color = color.gray(0.2), opacity = 1)


        line = box (pos = vector(-5,-4,0),length=1000, height=0.15, width=0.5, color = color.white   , opacity = 1)

        suelo = box (pos = vector(-5,-4.1,0),length=1000, height=0.1, width=1000, color = color.green, opacity = 1)

        ring(pos=vector(20,1,1),
                axis=vector(1,0,0),
                radius=4, thickness=0.1)

        k1 = np.cos(35*toDeg)*np.cos(0)
        k2 = np.sin(0)
        k3 = np.sin(35*toDeg)*np.cos(0)
        k = vector(k1,k2,k3)

        s = cross(k,y)

        v = cross(s,k)

        d5.axis = k
        d5.up = v
        d5.size= vector(3,.5,.9)
        d5.pos = vector(1,0,2.5)
        mano = compound([mano1,d1,d2,d3,d4,d5,sensor,antebrazo,ref])



        xF = arrow(length = 2, axis = vector(1,0,0), color =color.red,shaftwidth=.1, opacity = .5)

        yF = arrow(length = 2, axis = vector(0,1,0), color =color.green,shaftwidth=.1, opacity = .5)

        zF = arrow(length = 2, axis = vector(0,0,1), color =color.blue,shaftwidth=.1, opacity = .5)

        #objeto=compound([mano,xF,yF,zF])

        time.sleep(2)

        cerrar = 0

        px,py,pz = 0,0,0

        while True:
            
            try:
                if keyboard.is_pressed('esc') or cerrar == 1:
                    #play()
                    break
                
                while (arduino.inWaiting()==0):
                    print('Cargando...')
                    
                    if keyboard.is_pressed('esc'):
                        cerrar = 1
                        #play()
                        break
                        
                    else:
                        pass

                LineArdu = arduino.readline()

                LineArdu = LineArdu.decode('utf-8')
                
                datos = LineArdu.split(' , ')

                if keyboard.is_pressed('0'):
                    yawmax=0

                pitch = float(datos[0])*toRad
                roll = float(datos[1])*toRad
                yaw = -float(datos[2])*toRad

                pitch1 = float(datos[3])*toRad
                roll1 = float(datos[4])*toRad
                yaw1 = float(datos[5])*toRad

                x1 = pitch + pitch1
                y1 = roll + roll1
                z1 = yaw - yaw1
                
                rate(50)
                
                if abs(yaw)>abs(yawmax):
                    yawmax = yaw
                    
                k1 = np.cos(yaw)*np.cos(pitch)
                k2 = np.sin(pitch)
                k3 = np.sin(yaw)*np.cos(pitch)
                k = vector(k1,k2,k3)

                s = cross(k,y)

                v = cross(s,k)

                vrot = v*np.cos(roll) + cross(k,v)*np.sin(roll)

            
                scene.caption = "Desvicacion ulnar-radial:",z1*toDeg,"°  ;",yawmax*toDeg,"""°
        Flexión-Extension: """,x1*toDeg,"°","""
        Pronacion-Supinación: """,y1*toDeg

                #xF.axis = k
                xF.length = 9

                #yF.axis = v        
                yF.length = 3
                
                #zF.axis = s
                zF.length = 3
                """
                if keyboard.is_pressed('w'):
                    mano.pos = vector(px+1,0,0)
                    px = px +1

                if keyboard.is_pressed('s'):
                    mano.pos = vector(px-1,0,0)
                    px = px - 1
                    
                if keyboard.is_pressed('d'):
                    mano.pos = vector(py+1,0,0)
                    py = py +1

                """
                #mano.pos = vector(px+0.1,0,0),
                #scene.camera.axis = vector(2,.1,0)
                mano.axis = k
                mano.up = vrot
                #mano.length=4
                #mano.width = 3
                #mano.height = .2
                px = px +0.1
            except:
                pass
                print("Hubo un error")

        
        arduino.close()

aplicacion = Principal()