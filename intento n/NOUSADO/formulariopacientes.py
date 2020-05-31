import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from PIL import ImageTk, Image
import ventanas as vt


class BDPaciente:
    def __init__(self):
        self.articulo1=vt.Pacientes()
        """
        self.ventana_principal = tk.Tk()
        """
        self.ventana_pacientes=tk.Tk()
        self.ventana_pacientes.title("Rehab 1.0")
        self.cuaderno1 = ttk.Notebook(self.ventana_pacientes)
        self.sensores = vt.Sensores                
        self.carga_pacientes()
        self.consulta_por_CI()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.aplicacion()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana_pacientes.resizable(False,False)
        #self.ventana_pacientes.mainloop()

        """self.labelframe1=ttk.LabelFrame(self.ventana_principal, text="Opciones: ")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.boton_pacientes=ttk.Button(self.labelframe1, text="Confirmar", command=self.crear_ventana_pacientes)
        self.boton_pacientes.grid(column=1, row=3, padx=4, pady=4)"""

        self.ventana_pacientes.mainloop() 
    #PENDIENTE
    def crear_ventana_pacientes(self):
        self.ventana_pacientes=tk.Tk()
        self.ventana_pacientes.title("Rehab 1.0")
        self.cuaderno1 = ttk.Notebook(self.ventana_pacientes)
        self.sensores = vt.Sensores                
        self.carga_pacientes()
        self.consulta_por_CI()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.aplicacion()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        #self.ventana_pacientes.resizable(False,False)
        #self.ventana_pacientes.mainloop()
    def abrirBD(self):
        self.ventana2= tk.Toplevel()
        self.ventana2.title("Datos del paciente "+self.CI)

    #checkpoint
    #Consulta para carga
    
    def consultar_carga(self):
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
        #comparara en base de datos
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
        
        """
        cargarimagen = Image.open('imagen.jpg')
        cargarimagen = cargarimagen.resize((250, 250))
        imagen = ImageTk.PhotoImage(cargarimagen)

        LabelImagen = tk.Label(self.pagina2,image = imagen )

        LabelImagen.image= imagen 
        
        LabelImagen.place(x=250,y=40)"""

        
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

    def consultar(self):
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


        self.boton1=ttk.Button(self.labelframe1, text="INICIAR", command=vt.Sensores)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
#aplicacion1=BDPaciente()