import serial
import time
arduino = serial.Serial('com3', 115200)
while True:
    LineArdu = arduino.readline()
    LineArdu = LineArdu.decode('utf-8')
    datos = LineArdu.split(',')
    print(datos)
    time.sleep(0.05)
