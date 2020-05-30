import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import ttk
from tkinter import messagebox as mb
# pylint: disable=E1101


class Errores:
    def __init__(self):
        
        
        self.incon = tk.Toplevel()  
        self.incon.title("Registro...")  
        self.listainconvenientes = st.ScrolledText(self.incon, width=100, height=25)
        self.listainconvenientes.grid(column=0,row=1, padx=10, pady=10)
        self.incon.geometry("+10+10")


        self.listainconvenientes.delete("1.0", tk.END) 


        lista = open('Lista_inconvenientes.txt','r')
        for linea in lista:
            self.listainconvenientes.insert(tk.END, linea)
        self.texto =tk.StringVar()    
        self.inconveniente=ttk.Entry(self.incon,
            textvariable=self.texto, width = 100)
        self.inconveniente.grid(column=0, row=2, padx=4, pady=6)
        boton=tk.Button(self.incon,
            text="+",
            command= self.agregar_inconvenientes)        
        boton.grid(column=1, row=2, padx=4, pady=4)
        
        boton1=tk.Button(self.incon,
            text="Recargar \n lista",
            command= self.recargar_lista)        
        boton1.grid(column=1, row=1, padx=4, pady=4)
              

    def recargar_lista(self):

        self.listainconvenientes.delete("1.0", tk.END) 
        lista = open('Lista_inconvenientes.txt','r')
        for linea in lista:
            self.listainconvenientes.insert(tk.END, linea)

    def agregar_inconvenientes(self):
        nlineas= str(sum(1 for line in open('Lista_inconvenientes.txt'))-2)
        lista = open('Lista_inconvenientes.txt','a')
        nueva_linea = self.texto.get()
        lista.write(nlineas+": "+nueva_linea +'\n')
        lista.close()
        self.inconveniente.delete(0, 'end')
        mb.showinfo("ok","Agregado!")
