
import numpy as np
import keyboard,time, serial
#import play
arduino = serial.Serial('com6', 115200)

def sensores():

    toRad=2*np.pi/360
    toDeg=1/toRad

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

sensores()
arduino.close()

"""
Aviso contenido sensible jeje: 

Supongamos el hipotético caso donde los políticos corruptos  (solo aquellos que se sabe, porque el que sabe sabe ;) ;) )  fueran asesinados con las respectivas pruebas de corrupción ( abuso de poder, blanqueo de dinero o diferentes formas de robar capital publico o valerse de su cargo para su beneficio y el de sus allegados). Uds creen que se pueda generar una especie de miedo anticorrupción? tipo: yo ni mierdas robo, aunque tenga chance, porque quien sabe que puede pasar después. Uds creen que sea una solución para lo que está pasando? Bajo mi perspectiva, sí, lo sé lo sé, derechos humanos..., pero si esto sigue así quien sabe los derechos de cuantos más valgan V de Vendetta.  

Yo opino ( esto es solo una red social y no debemos darle peso jeje) que podríamos formar una "liga de justicieros" para terminar con la corrupción. No deben ser todos asesinos, se necesita gente que abra puertas, gente que mire a un lado cuando alguien tenga que pasar, hay muchas acciones necesarias para que todo salga como debe salir. Hace falta un verdadero trabajo de inteligencia para llevar la "justicia" a aquellos que creen que los demás estamos por debajo de ellos, que solo ellos tienen derecho a vivir bien, rodeados de lujos, con hijos en los mejores colegios privados, los mejores autos y viajando cada que pueden. OJO! Esto no es para nada negativo si lo haces con dinero ganado con el "sudor de tu frente", o simplemente no abusando de dinero público que podría ir a escuelas, hospitales, carreteras, conectividad, transporte, apoyo a emprendimientos, y todos los usos legales y correctos que se pueda dar al dinero público. Sé que muchos de uds. ni siiquiera se plantearían este HIPOTETICO caso ( ;) ;) ) Respeto que crean en algún Dios y/o tengan sus ideales bien formados, pero ningún Dios, ningún ideal individual va a terminar con lo que está pasando. Hay demasiadas variables humanas para que un evento aleatorio termine con la corrupción. Por un momento, planteenselo, podemos no conocernos, no haber intercambiado nunca una palabra, pero si todos tenemos el mismo objetivo, bien claro, terminar con la corrupción ( sé que en el mundo real esto es tanto imposible, pero podemos acercarnos), podremos tener un futuro mejor, seguridad social, poder salir a la calle en guayaquil (o cualquier otro sitio, solo es un ejemplo) sin miedo a ser robados, poder bañarnos en los rios LIMPIOS en las ciudades, y muchas cosas más que directa o indirectamente están asociados. No se ustedes, pero la realidad que yo quiero para mi futuro está muy lejos, y debemos aprender a planificar y construir a largo plazo, debemos aprender a trabajar en equipo. Paz a todos, cuidense mucho y éxito en lo que se propongan.

Fin del comunicado.

P.D. La imagen es solo representativa. Necesitamos nuestra propia revolución!!
J6LABP5T

#ConfesionarioYachayTech5712
Con respecto a ese sistema utópico revolucionario donde unos pocos formásemos esa "liga de justicieros" (uso ese nombre porque me parece algo bastante claro como nombre de variable). Obviamente como bien dicen "para un vivo existe otro vivo",y en este pais vivos es lo que sobran, y especificamente son unos pocos con los que hay que terminar. 

Yo sé que un gran poder conlleva una gran responsabilidad y lo que les propongo es un verdadero trabajo de inteligencia. No se cuanto sepan de corrupcion en este país, pero tenemos tráfico de armas, drogas y bastante tráfico de blancas. He tenido la oportunidad de "saborear" esta corrupción y conocer sujetos relacionados con esto y aunque si son bastantes (hace falta más datos :( ), realmente son pocas personas sin escrúpulos que tienen quien les obedezca por alguna necesidad inherente o de su familia, algo que me parece bastante triste, que muchas personas tengan que herir a otros de una u otra forma por "necesidad".

Alguien puso algo de corruptos con un armar legal como esta, propongo literalmente aniquilar a las fuentes de poder con corrupcion, eso muy legal no es, tal vez por parte de la justicia en China o Indonesia  (solo ejemplos)... No hipotetizo un caso donde la pena capital se vuelva algo normal. Ni tampoco creo que sería bueno tener un estado autoritario comunista o cosas parecidas donde una sola persona ( o pequeño grupo) toma el poder y le agarra cariño.

Por un lado, propongo estas malas mañas para "asustar" a los políticos corruptos no a todos los corruptos en general. Seamos sinceros, todos guardamos un poco de corrupción dentro, y simplemente porque somos animales y tenemos deseos (el que domine su relacion del Yo el Ello y el Superyo que se teletransporte aquí para planificar en chévere)  ; y de aquí históricamente surgen muchas corrientes filosóficas y religiones y blablaba para mantener el control de estos animalitos que se autodenominaron homo sapiens sapiens. SIn embargo habemos unos mas o menos animales que otros y lo ideal sería que los menos corruptos sean quienes se les de la oportunidad de administrar los recursos del país.

Por otro lado, la idea no es crear una cultura del miedo, lo ideal sería poder educar a las personas, desde niños establecer ciertas normas de comportamiento donde aprendan a convivir ellos para ellos y para su entorno, tanto social como natural. Y esto si necesita bastante apoyo. Sino que deben surgir dudas en ellos, por eso si se hace esto, no debería ser para nada discreto, por qué, si se hace en silencio no vale de nada, el rato que las personas (los niños principalmente) se empiecen a preguntar los por qués, esto actuará como un desencadenador que puede aprovecharse para enseñar a los niños por qué unos locos están acabando con algunos políticos de su país.

Antes de acabar, la clave fundamental para lograr una sociedad utópica donde todos puedan ser libres de ser quienes quieran ser aún está muy lejos, sin embargo, una sociedad educada puede brindarle a las personas una mejor calidad de vida y aproximarse a esa realidad ( y si le metes VR, controles hápticos y sensoriales la cosa se pone interesante, pero aún falta para esos capítulos de Black Mirror en el mundo real). Esto obviamente no se logra matando a nadie, requiere de diferentes aportes por parte de individuos o colectivos, proyectos educativos, divulgación de ciencia, y las ideas que se les ocurran.

Por último, una revolución requiere que cada uno tenga una revolución en su cabecita para entender los porqués, para esto: educación. Sin embargo, debemos avanzar pasito a pasito, y desafortunadamente aún nos faltan los pasos más duros, los pasos donde muere gente, los pasos donde la gente llora y sufre, donde podemos perder amigos o familia y aunque esto ya esté pasando, generalmente es por problemas de drogas, armas, placeres banales o problemas emocionales (solo ejemplos)  de esta sociedad que no sabe manejar...Asi que amigos justicieros, como les dije en el otro mensaje, no todos tenemos que ser asesinos psicópatas  ( se que algunos quieren, pero mantengan la calma), sino que para una verdadera revolución cada uno debe aportar desde su posición de manera pertinente e inteligente. No sería bueno (perdón por la crítica pero asies) parecer la hinchada brava de barcelona, emelec o "inserte aqui nombre de equipo de futbol popular" después de haber perdido un partido golpeando gente, quemando cosas etc etc. 
Los invito a aportar al cambio de manera inteligente, que parezca que Yachay Tech es el cambio que el país necesitaba y no solo otro desperdicio más de dinero público.

P.D Les recomiendo hablar de esto con sus amigos y planificar. 
P.D El gobierno debe estar a mano de personas responsables que sepan manejar los datos y las ciencias, tanto naturales como sociales, no cualquier tipo o tipo que por su atractivo físico y bromas se gana el favor de la gente, revisar: https://es.wikipedia.org/wiki/Efecto_halo  https://www.abtasty.com/es/blog/efecto-halo-como-utilizarlo/  . Amigos agraciados fisicamente usen responsablemente su poder, los no tan bonitos (por fuera jeje) tendremos que aprovechar otros sesgos cognitivos para esta llamemos "revoución" (https://es.wikipedia.org/wiki/Anexo:Sesgos_cognitivos) .

Les dejo este artículo que me pareció bastante interesante: https://brendonmarotta.com/1709/empathy-ultimate-persuasion-tool/ 

El conocimiento es poder.

XYZVFY10"""
