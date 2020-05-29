import tkinter as tk
from tkinter import ttk

class Agregar_ejercicio(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nombre_etiqueta=ttk.Label(ventana_aprender,text ="Nombre del ejercicio")
        self.nombre_ejercicio = ttk.Entry(self)
        self.nombre_ejercicio.pack()
        
        self.greet_button = ttk.Button(
            self, text="Aceptar", command=self.say_hello)
        self.greet_button.pack()
        
        self.greet_label = ttk.Label(self)
        self.greet_label.pack()
    
    def say_hello(self):
        self.greet_label["text"] = \
            "¡Hola, {}!".format(self.nombre_ejercicio.get())

class Eliminar_ejercicio(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.label = ttk.Label(self)
        self.label["text"] = ("Eliminar Ejercicio")
        self.label.pack()
        
        self.boton_eliminar = ttk.Button(self, text="Eliminar")
        self.boton_eliminar.pack(pady=10)
        

class Application(ttk.Frame):
    
    def __init__(self, ventana_aprender):
        super().__init__(ventana_aprender)
        ventana_aprender.title("Agregar nuevo ejercicio")
        
        self.notebook = ttk.Notebook(self)
        
        self.greeting_frame = Agregar_ejercicio(self.notebook)
        self.notebook.add(
            self.greeting_frame, text="Agregar", padding=10)
        
        self.about_frame = Eliminar_ejercicio(self.notebook)
        self.notebook.add(
            self.about_frame, text="Acerca de", padding=10)
        
        self.notebook.pack(padx=10, pady=10)
        self.pack()
ventana_aprender = tk.Tk()
app = Application(ventana_aprender)
app.mainloop()
           




    def usuario_registrado(self):
        self.opciones_evaluar = tk.Toplevel()
        self.opciones_evaluar.title("Elija una opcion")
        
        self.etiqueta_usuario_registrado = ttk.Frame(self.opciones_evaluar)
        self.opciones_evaluar.add(self.etiqueta_usuario_registrado, text="Usuario registrado:")


        self.boton_evaluar = tk.Button(self.opciones_evaluar,
                text="Nueva evaluación para "+self.respuesta[0][1],
                command =print("eva"),
                height = 10,
                width = 10,
                bg='#ffffff',
                fg='#000000')
        self.boton_evaluar.grid(row=0, column=1)


        self.boton_registro = tk.Button(self.opciones_evaluar,
                text="Ver registro de "+self.respuesta[0][1],
                command =print("ver registro"),
                height = 10,
                width = 10,
                bg='#ffffff',
                fg='#000000')
        self.boton_registro.grid(row=0, column=2)
