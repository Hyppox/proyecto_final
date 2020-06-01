import tkinter as tk
import time

class Cambiar:
    def __init__(self):
        self.ventana=tk.Tk()
        self.marco=tk.LabelFrame(self.ventana, text="test").grid(row=0,column=0)
        self.color = tk.Label(self.marco,text = " ", bg="blue")
        self.color.grid(row=0,column=0)
        self.boton = tk.Button(self.marco, text = "cambiar",command = self.actualizar)
        self.boton.grid(row=0,column=1)
        self.num = 0
        self.ventana.mainloop()
    def actualizar(self):
        if self.num == 0:
            ahora = "2nd round bitch"
            self.color.after(1000, self.actualizar)
            
        ahora = time.time()
        self.color.config(text = ahora)
        self.color.after(1000, self.actualizar)
       
        self.color.after(1000, self.actualizar)

    def ventanacolor(self):
        self.ven = tk.Toplevel()

Cambiar()
