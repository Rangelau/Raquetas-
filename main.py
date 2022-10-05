import pygame as pg
from entidades import Bola,Raqueta
pg.init()


pantalla_principal=pg.display.set_mode ((800,600))
pg.display.set_caption("pong")
metodromo = pg.time.Clock()

game_over=False
bola=Bola(400,300,color=(255,255,255))
raqueta1=Raqueta (20,300,w=20,h=120,color=(255,255,255))
raqueta2= Raqueta(780,300,w=20,h=120, color=(255,255,255))
raqueta2.vy=5
raqueta1.vy=5

#lo que hace el while not game over es pintar un fotograma y si entra nuevamente al while y si no es game over pinta el sgt fotograma, este lo controlamos para que pinte de manera indepentiente y se vean las cosas mas bonitas
while not  game_over:
 #eventos que hace el usuario y devuelve una lista de eventos   
    metodromo.tick(60)
    for evento in pg.event.get():
        if evento.type==pg.QUIT:
             game_over=True

        
#key es un modulo pg y get pressend devuelve el estado de la tecla que se esta pulsando en el momento que ejecutamos el programa
    raqueta2.mover(pg.K_UP,pg.K_DOWN,)
    raqueta1.mover(pg.K_a,pg.K_z)

        
    pantalla_principal.fill((0,0,0))
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    
        #le pasa la informacion a la tarjeta grafica de pygame (pg.display.filp)
    pg.display.flip() 