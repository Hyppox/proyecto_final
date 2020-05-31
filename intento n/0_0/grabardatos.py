import tkinter

class GuardarDatos:
    def __init__(self):
        self.iniciarconexion
    def iniciarconexion(self):
        self.arduino = serial.Serial('com6', 115200)
        self.LineArdu = self.arduino.readline()
        self.LineArdu = self.LineArdu.decode('utf-8')
        time.sleep(2)
        self.datos = self.LineArdu.split(',')
    def imprimirdatos(self):
        print(self.datos)

while True:
    GuardarDatos.imprimirdatos
arduino.close() 