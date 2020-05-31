
import numpy as np
import keyboard,time, serial
#import play
arduino = serial.Serial('com6', 115200)

class Sensores:
    def __init__(self):
        super().__init__()
        self.sensores()
    def sensores():

        scene.range=5
        toRad=2*np.pi/360
        toDeg=1/toRad
        y = vector(0,1,0)
        yawmax=0

        scene.append_to_caption('\n\n')

        #scene.forward=vector(-1,-1,-1)
        
        scene.width=1000
        scene.height=1000

        scene.background=color.white

        #mano = box (pos = vector(0,0,0),length=5, height=0.5, width=2, color = color.purple, opacity = .8, axis = vector(0,0,0))


        arduino = serial.Serial('com6', 115200)
        LineArdu = arduino.readline()
        LineArdu = LineArdu.decode('utf-8')
        time.sleep(2)
        datos = LineArdu.split(',')

        while True:
            
            try:
                if keyboard.is_pressed('esc') or cerrar == 1:
                    #play()
                    break
                
                while (arduino.inWaiting()==0):
                    print('Cargando...')
                    
                    if keyboard.is_pressed('esc'):
                        cerrar = 1
                        #play()
                        break
                        
                    else:
                        pass

                LineArdu = arduino.readline()

                LineArdu = LineArdu.decode('utf-8')
                
                datos = LineArdu.split(' , ')

                if keyboard.is_pressed('0'):
                    yawmax=0

                pitch = float(datos[0])*toRad
                roll = float(datos[1])*toRad
                yaw = -float(datos[2])*toRad

                pitch1 = float(datos[3])*toRad
                roll1 = float(datos[4])*toRad
                yaw1 = float(datos[5])*toRad
                print(pitch+','+roll+','+yaw)
            except:
                pass
                print("Hubo un error")

        

Sensores.__init__
arduino.close()
