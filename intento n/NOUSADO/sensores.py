from vpython import*
import numpy as np
import keyboard,time, serial
#import play

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

        mano1 = box (pos = vector(0,0,0),length=4, height=0.6, width=4, color = color.orange, opacity = 1)


        sensor =  box (pos = vector(0,.1,0),length=1, height=.6, width=1, color = color.red, opacity = .5)



        d1 = box (pos = vector(3,0,-1.5),length=3.5, height=0.5, width=.9, color = color.orange, opacity = 1)
        d2 = box (pos = vector(3,0,-0.5),length=4.5, height=0.5, width=.9, color = color.orange, opacity = 1)
        d3 = box (pos = vector(3,0,0.5),length=5, height=0.5, width=.9, color = color.orange, opacity = 1)
        d4 = box (pos = vector(3,0,1.5),length=4, height=0.5, width=.9, color = color.orange, opacity = 1)
        d5 = box (pos = vector(-1,0,2.5),length=4, height=0.5, width=.9, color = color.orange, opacity = 1)

        antebrazo = box (pos = vector(-1,0,0), length=2.5, height=0.5, width=3, color = color.yellow, opacity = .8)

        #ref = box (pos = vector(4,0,0), length=1, height=0.5, width=3, color = color.black, opacity = 1)
        ref = box (pos = vector(-5,0,0),length=10, height=0.1, width=.1, color = color.black, opacity = 1)

        road = box (pos = vector(-5,-4,0),length=1000, height=0.1, width=20, color = color.gray(0.2), opacity = 1)


        line = box (pos = vector(-5,-4,0),length=1000, height=0.15, width=0.5, color = color.white   , opacity = 1)

        suelo = box (pos = vector(-5,-4.1,0),length=1000, height=0.1, width=1000, color = color.green, opacity = 1)

        ring(pos=vector(20,1,1),
                axis=vector(1,0,0),
                radius=4, thickness=0.1)

        k1 = np.cos(35*toDeg)*np.cos(0)
        k2 = np.sin(0)
        k3 = np.sin(35*toDeg)*np.cos(0)
        k = vector(k1,k2,k3)

        s = cross(k,y)

        v = cross(s,k)

        d5.axis = k
        d5.up = v
        d5.size= vector(3,.5,.9)
        d5.pos = vector(1,0,2.5)
        mano = compound([mano1,d1,d2,d3,d4,d5,sensor,antebrazo,ref])



        xF = arrow(length = 2, axis = vector(1,0,0), color =color.red,shaftwidth=.1, opacity = .5)

        yF = arrow(length = 2, axis = vector(0,1,0), color =color.green,shaftwidth=.1, opacity = .5)

        zF = arrow(length = 2, axis = vector(0,0,1), color =color.blue,shaftwidth=.1, opacity = .5)

        #objeto=compound([mano,xF,yF,zF])

        time.sleep(2)

        cerrar = 0

        px,py,pz = 0,0,0

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

                x1 = pitch + pitch1
                y1 = roll + roll1
                z1 = yaw - yaw1
                
                rate(50)
                
                if abs(yaw)>abs(yawmax):
                    yawmax = yaw
                    
                k1 = np.cos(yaw)*np.cos(pitch)
                k2 = np.sin(pitch)
                k3 = np.sin(yaw)*np.cos(pitch)
                k = vector(k1,k2,k3)

                s = cross(k,y)

                v = cross(s,k)

                vrot = v*np.cos(roll) + cross(k,v)*np.sin(roll)

            
                scene.caption = "Desvicacion ulnar-radial:",z1*toDeg,"°  ;",yawmax*toDeg,"""°
        Flexión-Extension: """,x1*toDeg,"°","""
        Pronacion-Supinación: """,y1*toDeg

                #xF.axis = k
                xF.length = 9

                #yF.axis = v        
                yF.length = 3
                
                #zF.axis = s
                zF.length = 3
                """
                if keyboard.is_pressed('w'):
                    mano.pos = vector(px+1,0,0)
                    px = px +1

                if keyboard.is_pressed('s'):
                    mano.pos = vector(px-1,0,0)
                    px = px - 1
                    
                if keyboard.is_pressed('d'):
                    mano.pos = vector(py+1,0,0)
                    py = py +1

                """
                #mano.pos = vector(px+0.1,0,0),
                #scene.camera.axis = vector(2,.1,0)
                mano.axis = k
                mano.up = vrot
                #mano.length=4
                #mano.width = 3
                #mano.height = .2
                px = px +0.1
            except:
                pass
                print("Hubo un error")

        
        arduino.close()


