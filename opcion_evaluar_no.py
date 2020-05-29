import tkinter as tk 
import tkinter.font as font

class Sinregistro:
    def __init__(self):
        super().__init__()
        self.pregunta

    def pregunta(self):
        self.preg = tk.Toplevel()
        self.preg.configure(bg = "#ffffff")
        self.preg.geometry("+500+208")
        self.label=tk.Label(self.preg,
                text="Ingrese CI del paciente:",
                bg='#ffffff')      
       
        self.preg.geometry("+436+583")
        
        tamano_texto = font.Font(size=12 )
