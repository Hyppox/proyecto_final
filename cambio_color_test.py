import tkinter as tk
import time
from tkinter import ttk
class Cambiar:
    def __init__(self):
        self.ventana=tk.Tk()
        self.marco=tk.LabelFrame(self.ventana, text="test").grid(row=0,column=0)
        self.color = tk.Label(self.marco,text = " ", bg="blue")
        self.color.grid(row=0,column=0)

        
        self.tiempo=tk.StringVar()
        self.entrada_num=ttk.Entry(self.ventana, textvariable=self.tiempo   )
        self.entrada_num.grid(column=1, row=1)

        self.n_rep=tk.StringVar()
        self.entrada_rep=ttk.Entry(self.ventana, textvariable=self.n_rep   )
        self.entrada_rep.grid(column=1, row=2)
        

        self.boton = tk.Button(self.marco, text = "cambiar",command = self.actualizar)
        self.boton.grid(row=0,column=1)
        self.num = 0
        self.ventana.mainloop()
    def actualizar(self):
        limite = ("after#"+self.entrada_rep.get())
        t = int(self.entrada_num.get())*1000
        if self.num == 0:
            self.num=1
            ahora = "sip"
            self.color.config(text = ahora,bg="blue")
            ID =self.color.after(t, self.actualizar)
        
        else:
            self.num=0
            ahora = "nel"
            self.color.config(text = ahora,bg="red")
            ID = self.color.after(t, self.actualizar)
        print(type(ID))
        print(ID)
        if limite == ID:
            self.color.after_cancel(ID)

    def ventanacolor(self):
        self.ven = tk.Toplevel()

Cambiar()
