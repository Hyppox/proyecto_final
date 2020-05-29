import tkinter

class Agregar:
    def __init__(self):
        self.Agregar

    def agregar(self):
        datos=(self.nombrecarga.get(),
         self.cargarpaciente.get(),
         self.edadpaciente.get(),
         self.sexopaciente.get())

        self.BDpacientes.alta(datos)

        mb.showinfo("Información", "Los datos fueron cargados")
        
        self.entrynombre.set("")
        self.entryCI.set("")
        self.entryedad.set("")
        self.entrysexopaciente.set("")
    