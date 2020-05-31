import tkinter as tk
from tkinter import ttk
import ventanas as vt
from tkinter import ttk
import sys
class Principal:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Rehab 1.0")
        self.ventana.geometry('300x300')
        self.botones()
        self.ventana.resizable(False,False)

        self.ventana.mainloop()
    def salir(self):
        sys.exit()
    def botones(self):
        self.botonPacientes = ttk.Button(self.ventana,  text = "Pacientes" , command= vt.BDPaciente)
        self.botonPacientes.grid(row=0,column=2)
        self.botoninfo =  ttk.Button(self.ventana,  text = "info" , command= vt.Leerpdf)
        self.botoninfo.grid(row=1,column=2)
        self.botoncerrar = ttk.Button(self.ventana, text = "Cerrar", command = self.salir)
        self.botoninfo.grid(row=2,column=2)

aplicacion = Principal()