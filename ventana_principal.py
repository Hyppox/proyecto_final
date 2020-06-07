import tkinter as tk
import tkinter.font as font

#llama de un archivo opcion_****.py cada ventana
import opcion_pacientes
import opcion_evaluar  
import opcion_aprender as oa
import errores

class Principal:
    def __init__(self):
        self.principal()
        super().__init__()       
        

    def cerrar(self):
        
        MsgBox = tk.messagebox.askquestion ('Cerrar Aplicación','¿Desea cerrar la aplicación?',icon = 'warning')
        if MsgBox == 'yes':
            self.root.destroy()
        else:
            tk.messagebox.showinfo('Regresar','Regresará a la aplicación')
      
    def principal(self):
                
        self.root = tk.Tk()
        self.root.title("Rehab 0.0 Alpha")
        self.root.configure(bg = "#ffffff")
        self.root.geometry("+10+40")
        self.imagenboton = tk.PhotoImage(file ="lupa.png")

        #Estas son etiquetas vacias para ordenar los botones
        self.vacio = tk.Label(self.root,
                 text= "\t",
                bg='#ffffff')
        self.vacio.grid(row=0,column=0)

        self.vacio2 = tk.Label(self.root,
                 text= "\t",
                bg='#ffffff')

        self.vacio2.grid(row=3,column=2)

        self.vacio3 = tk.Label(self.root,
                 text= "\t",

                bg='#ffffff')

        self.vacio3.grid(row=5,column=0)

        self.vacio4 = tk.Label(self.root,
                 text= "\t",
                bg='#ffffff')

        self.vacio4.grid(row=7,column=0)
        
        self.vacio5 = tk.Label(self.root,
                 text= "\t",
                bg='#ffffff')

        self.vacio5.grid(row=9,column=0)



        #CREACION DE BOTONES
        #configuración del texto en los botones
        tamano_texto = font.Font(size=12, weight = "bold" )
        self.errores = tk.Button(self.root,
                image = self.imagenboton,
                text="?",
                command = errores.Errores,
                height = 1,
                width = 1,
                bg='#ffffff',
                fg='#000000')
        self.errores.grid(row=10, column=2)
        
        

        self.pacientes = tk.Button(self.root,
                text="Pacientes",
                command = opcion_pacientes.BDPaciente,
                height = 5,
                width = 20,
                bg='#ffffff',
                fg='#000000')
        
        
        self.pacientes['font'] = tamano_texto
        self.pacientes.grid(row=1, column=1)
        
        self.evaluar = tk.Button(self.root,
                text="Evaluar/Agregar",
                command = opcion_evaluar.Evaluar,
                height = 5,
                width = 20,
                bg='#ffffff',
                fg='#000000')
                
        self.evaluar['font'] = tamano_texto
        self.evaluar.grid(row=4, column=1)
        
        self.aprender = tk.Button(self.root,
                text="Aprender",
                command =oa.Aprender,
                height = 5,
                width = 20,
                bg='#ffffff',
                fg='#000000')

        self.aprender['font'] = tamano_texto
        self.aprender.grid(row=6, column=1)

        self.cerrar = tk.Button(self.root,
                text="Cerrar",
                command = self.cerrar,
                height = 5,
                width = 20,
                bg='#ffffff',
                fg='#000000')

        self.cerrar['font'] = tamano_texto
        self.cerrar.grid(row=8, column=1)

        self.root.resizable(False,False)
        self.root.mainloop()
    
aplicacion = Principal()