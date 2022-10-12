
from pickle import TRUE
import pygame as pg
from pong.entidades import Bola,Raqueta
from pong import ALTO,ANCHO,BLANCO, NARANJA,NEGRO,FPS, PRIMER_AVISO, ROJO, SEGUNDO_AVISO,TIEMPO_MAX_PARTIDA,AMARILLO


class Partida:
    def __init__(self):# es la infraestructura principal del juego cosas que son constantes

        self.pantalla_principal=pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("pong")
        self.metronomo=pg.time.Clock() #tiempo que demora en entrar al bucle desde inicializo el metronomo
        self.temporizador= TIEMPO_MAX_PARTIDA  #self.cronomrtro es el tiempo que demora en terminar la partida

       

        self.bola =Bola(ANCHO//2,ALTO//2,color=BLANCO)
        self.raqueta1=Raqueta (20,ALTO,w=20,h=120,color=BLANCO)
        self.raqueta1.vy=5
        self.raqueta2= Raqueta(ANCHO-20,ALTO//2,w=20,h=120, color=BLANCO)
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

        game_over= False

        while not  game_over and\
              self.puntuacion1< 10 and\
              self.puntuacion2< 10 and\
              self.temporizador > 0:
            
            #se mantiene dentro del  bucle mientras el temporizador sea mayor que 0

            #para calcular el tiempo en el tick desde que se inicio el metronomo
            #tick cuenta los tiempos en milisegundos desde que paso por el inicio del bucle

            salto_tiempo= self.metronomo.tick(FPS)
            self.temporizador -= salto_tiempo

            for evento in pg.event.get():
                if evento.type==pg.QUIT:
                    game_over=True
                
            
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


