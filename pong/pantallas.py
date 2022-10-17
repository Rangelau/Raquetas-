import pygame as pg

import pong
from pong import (ALTO, AMARILLO, ANCHO, BLANCO, FPS, MAGENTA, NARANJA, NEGRO,
                  PRIMER_AVISO, PUNTUACION_GANADORA, ROJO, SEGUNDO_AVISO,
                  TIEMPO_MAX_PARTIDA)
from pong.entidades import Bola, Raqueta


class Partida:
    #como creamos la pantalla en la clase jugar que es la principal aca lo que hacemos es llamar el objeto
    #cuando creemes la partida debemos decir que lleva el atributo pantalla y el metronomo
    def __init__(self,pantalla,metronomo):# es la que tiene los objetos y la bucle principal del juego cosas que son constantes
        #pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        self.pantalla_principal = pantalla
        self.metronomo = metronomo #tiempo que demora en entrar al bucle desde inicializo el metronomo
        pg.display.set_caption("pong")
       
        self.temporizador= TIEMPO_MAX_PARTIDA  #self.cronomrtro es el tiempo que demora en terminar la partida

       

        self.bola =Bola(ANCHO//2,ALTO//2,color=BLANCO)
        #aqui ponemos en w y h el tamaño de la imagen que cargamos de la raqueta
        self.raqueta1=Raqueta (20,ALTO//2,w=30,h=114)
        #self.raqueta1.fileimg="electric00_izq.png" esto ya no hace falta porque por defecto va la raqueta izquierda
        self.raqueta1.vy=5
        
        self.raqueta2= Raqueta(ANCHO-20,ALTO//2,w=30,h=114)
        self.raqueta2.direccion="derecha" #como es un setter lo tomo como un aributo  y le asigno un valor con el =
        self.raqueta2.vy=5

        self.puntuacion1=0
        self.puntuacion2=0

        #vamos a crear la fuente para que pueda arrojar mensaje de la puntuación
        self.fuenteMarcador= pg.font.Font("fonts/Silkscreen",40)
        self.fuentetemporizador=pg.font.Font("fonts/Silkscreen",20)

        self.contadorFotogramas = 0
        self.fondoPantalla=NEGRO


    
    def fijar_fondo(self):
        self.contadorFotogramas += 1

        if self.temporizador > PRIMER_AVISO:
            self.contadorFotogramas = 0
        elif self.temporizador > SEGUNDO_AVISO:
            # cada 10 fotogramas cambia de naranja a negro y viceversa
            if self.contadorFotogramas == 10:
                if self.fondoPantalla == NEGRO:
                    self.fondoPantalla = NARANJA 
                else:
                    self.fondoPantalla = NEGRO
                    self.contadorFotogramas = 0
        else:
            # cad 5 fotogramas cambia de rojo a negro y viceversa
            if self.contadorFotogramas >= 5: #como el >= 5 va a estar en color narajan y me lo va a poner en negro y si el negro me lo va a convertir en rojo
                if self.fondoPantalla == NEGRO:
                    self.fondoPantalla = ROJO
                else:
                    self.fondoPantalla = NEGRO
                    self.contadorFotogramas = 0


        return self.fondoPantalla
        
        #cada 5 fotogramas cambia de rojo a negro y viceversa

    
    
    #se  le llama bucle principal porque cada vez que una persona quiera iniciar partida debe volver al inicio del juego
    
    
    def bucle_ppal(self):
        #antes de iniciar la partida inicializamos la bola
        self.bola.vx=5
        self.bola.vy=-5
        #antes de inciar la la partida inicializamos  la puntuacion 1 y 2
        self.puntuacion1=0
        self.puntuacion2=0
        self.temporizador=TIEMPO_MAX_PARTIDA

        game_over= False
        self.metronomo.tick()

#EL METRONO DEBE PONERSE EN 0 ANTES DE QUE INICIE LA PARTIDA CON UN TICK
 
        print(self.metronomo.tick())
        while not  game_over and\
              self.puntuacion1<PUNTUACION_GANADORA and\
              self.puntuacion2<PUNTUACION_GANADORA and\
              self.temporizador > 0:
            
            #se mantiene dentro del  bucle mientras el temporizador sea mayor que 0

            #para calcular el tiempo en el tick desde que se inicio el metronomo
            #tick cuenta los tiempos en milisegundos desde que paso por el inicio del bucle

            salto_tiempo= self.metronomo.tick(FPS)
        
            self.temporizador -= salto_tiempo

            for evento in pg.event.get():
                if evento.type==pg.QUIT:
                    return True
               
            
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.raqueta1.mover(pg.K_a,pg.K_z)
            quien=self.bola.mover() #quien hace referenca a la persona que se le va a asignar punto si sale la bola

            if quien == "RIGHT":
                self.puntuacion2 += 1
 
            elif quien =="LEFT":
                self.puntuacion1 += 1


           
          
         

            #para que se salga del  programa cuando completen los 9 puntos
            """if self.puntuacion1>9 or self.puntuacion2 >9:
                game_over= True
            
            """
                
            self.bola.comprobar_choque(self.raqueta2,self.raqueta1)
 
            colorFondo=self.fijar_fondo() # esto se hace para que pueda fijar el color del fondo que retorno arriba con el def lo que hicimos fue crear la clase
            #creamos una variable color fondo que va a almacenar el color que se fijo 
            #luego definimos el color con el fill en la pantalla  
            #cada vez que fijamos fondo de crea un nuevo fotograma
                
            self.pantalla_principal.fill(colorFondo)
            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            p1=self.fuenteMarcador.render(str(self.puntuacion1),True,BLANCO)
            p2=self.fuenteMarcador.render(str(self.puntuacion2),True,BLANCO)

            contador = self.fuentetemporizador.render (str(self.temporizador/1000),True,BLANCO)
            #el cronometro se divide entre 1000 para que muestre el valor en segundos
            self.pantalla_principal.blit(p1,(10,10))
            self.pantalla_principal.blit(p2,(ANCHO-45,10))
            self.pantalla_principal.blit (contador,(ANCHO//2,10))
            
                #le pasa la informacion a la tarjeta grafica de pygame (pg.display.filp)
            pg.display.flip()        

class Menu:     #es la pantalla del menu principal
    def __init__(self,pantalla,metronomo): #creamos los objetos que necesitamos
        self.pantalla_principal=pantalla 
        self.metronomo=metronomo
     
        pg.display.set_caption("Menu")

        
        self.imagenFondo = pg.image.load("images/portada2.png")#tomamos un metodo de la libreria pg, que toma una imagen y la convierte en una calcomania que luego hay que ponerla en la superficie de la pantalla
        self.fuenteComenzar= pg.font.Font("fonts/Silkscreen",50) #para decirle que fuente le vamos a poner a lo que antes era una calcomania
        self.musica= pg.mixer.Sound("pong/sounds/duelo.ogg")


    #1) cargamos imagen de fondo/ 2) establecimos el tipo de fuente 3) usamos el blit para poner sobre la superficie que tenemos otra superficie en este caso es la foto que cargamos
    #4)sobre esa imagen con el render le vamos a poner un texto 5)Ahora hacemos un blit para que nos ponga sobre la pantalla el menu
    def bucle_ppal (self):
        game_over = False

        # queremos reproducir la musica con ciertas especificaciones
        #1. queremos que una vez acabe la musica siga hasta que la persona pulse enter

        self.musica.play(-1)
        #EL RELOJ DEBE PONERSE EN 0 ANTES DE QUE INICIE LA PARTIDA CON UN TICK
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True  
                #si se presenta que la persona presiona x= quit(salida) eso es igual a verdadero porque es lo mismo
                #si la persona no presiona otra tecla diferente a esa es es falso

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
            
        #BLIT lo usamos para dibujar en la superficie, la imagen del objeto que tenemos

            self.pantalla_principal.blit(self.imagenFondo,(0,0))

        #render se usa para difubar la imagen de un objeto surface sobre otro objeto surface
            menu=self.fuenteComenzar.render("Pulsa ENTER para comentar",True,AMARILLO)
            self.pantalla_principal.blit(menu,(ANCHO//2,ALTO-200)) 
            
            pg.display.flip()

        self.musica.stop()


        
