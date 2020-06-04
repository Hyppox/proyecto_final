import serial
import time
from serial import Serial

def aprendizaje(t,n):
        
    # set up the serial line
    ser = serial.Serial('COM3', 115200)
    time.sleep(2)
    # Read and record the data
    #t = int(input("Ingrese tiempo de toma de datos: "))
    #n = int(input("ingrese el número de repeticiones: "))
    data =[]                       # empty list to store the data

    contador = 0
    while contador < n:
        inicio = time.time()
        ahora = time.time()        
        while (ahora-inicio) < t:
            b = ser.readline()         # read a byte string
            string_n = b.decode()  # decode byte string into Unicode  
            string = string_n.rstrip() # remove \n and \r

            #print(string)
            data.append(string)           # add to the end of data list
            time.sleep(0.1)            # wait (sleep) 0.1 seconds
            ahora = time.time()
            
        marcador = "----------" # -*10
        data.append(marcador)
        contador +=1
        fin = time.time()
        print("La vuelta ",contador," duró: ",round(fin-inicio,2), "s")
    for line in data:
            
        print(line)
    ser.close()
