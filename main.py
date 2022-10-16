from pong.jugar import Controlador

#Aqui va a arrancar la pantalla desde el menu y partida lo hacemos que arranque desde el bucle while de menu

juego=Controlador()
juego.jugar()

"""
en lugar de que uno elega si quiere poner el menu o la partida vamos
a hacer un bucle que primero salga el menu, luego salga la partida
y cuando se acabe la partida salga el menu.
QUE SEA UN BUCLE INFINITO


opcion= input("Partida o Menú (P/M)")
if opcion.upper ()== "P": #UPPER es para pasar a mayuscula la letra p/n
    #:abrir pygame con la partida de pong que tengamos
    juego=Partida () #aqui llamamos a la clase partida a partir de la creación de un objeto
    juego.bucle_ppal() #usamos la funcion bucle principal que esta en la clase para que cree la pantalla

   
elif opcion.upper()=="M":
    # abrir el pygame con la pantalla azul(donde esta el menu)
    juego=Menu()
    juego.bucle_ppal()
    
else:
    print ("opcion incorrecta")
       
#AQUI ESTABAN LOS OBJETOS CREADOS, AHORA SE PASARON A PANTALLAS COMO UNA CLASE DEBIDO A QUE SIEMPRE SE VAN A USAR DENTRO DEL JUEGO
import pygame as pg
from entidades import Bola,Raqueta
pg.init()


pantalla_principal=pg.display.set_mode ((800,600))
pg.display.set_caption("pong")
metodromo = pg.time.Clock()

game_over=False
bola=Bola(400,300,color=(255,255,255))
bola.vx=2
bola.vy=-2
raqueta1=Raqueta (20,300,w=20,h=120,color=(0,255,255))
raqueta2= Raqueta(780,300,w=20,h=120, color=(0,255,255))
raqueta2.vy=5
raqueta1.vy=5
puerta1=0
puerta2=0

#lo que hace el while not game over es pintar un fotograma y si entra nuevamente al while y si no es game over pinta el sgt fotograma, este lo controlamos para que pinte de manera indepentiente y se vean las cosas mas bonitas
while not  game_over:
 #eventos que hace el usuario y devuelve una lista de eventos   
    metodromo.tick(60)
    for evento in pg.event.get():
        if evento.type==pg.QUIT:
             game_over=True
        
        
#key es un modulo pg y get pressend devuelve el estado de la tecla que se esta pulsando en el momento que ejecutamos el programa
  
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    raqueta1.mover(pg.K_a,pg.K_z)
    quien=bola.mover() #quien hace referenca a la persona que se le va a asignar punto si sale la bola
    if quien =="RIGTH":
        puerta2 +=1
    elif quien =="LEFT":
        puerta1+=1




    bola.comprobar_choque(raqueta1,raqueta2)

        
    pantalla_principal.fill((0,0,0))
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    
        #le pasa la informacion a la tarjeta grafica de pygame (pg.display.filp)
    pg.display.flip() 

"""