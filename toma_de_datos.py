import serial
import time
from serial import Serial

# set up the serial line
ser = serial.Serial('COM3', 115200)
time.sleep(2)
# Read and record the data
t = int(input("Ingrese tiempo de toma de datos"))
data =[]                       # empty list to store the data
for i in range(t):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r

    print(string)
    data.append(string)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()
# show the data

for line in data:
    print(line)# -*- coding: utf-8 -*-

