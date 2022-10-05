import pygame as pg

class Bola():
    def __init__(self,center_x,center_y,radio=10,color=(255,255,0)):
        self.center_x=center_x
        self.center_y=center_y
        self.color= color
        self.radio=radio

        self.vx=0
        self.vy=0

    def dibujar (self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.center_x,self.center_y), self.radio)

class Raqueta:
    def __init__(self,center_x,center_y,w=120,h=20,color=(255,255,0)):
        self.center_x=center_x
        self.center_y=center_y
        self.color= color
        self.w=w
        self.h=h

        self.vx=0
        self.vy=0

    def dibujar (self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.center_x-self.w //2,self.center_y-self.h//2, self.w,self.h))

#get pressend es una funcion que en momento que se invoca va al teclado y devuelve el estado del teclado
 #devuelve false en el caso de que no se toque tecla y true en el caso de que este presionada
    def mover(self,tecla_arriba,tecla_abajo, y_max=600,x_max=0):
        estado_teclas = pg.key.get_pressed() 
        if estado_teclas [tecla_arriba] and self.center_y > 0+ self.h//2:
            self.center_y -= self.vy
        if self.center_y < 0+ self.h//2:
            self.center_y=self.h//2
        if estado_teclas [tecla_abajo]:
            self.center_y += self.vy
        if self.center_y > y_max-self.h//2:
            self.center_y=y_max-self.h//2

        #estamos diciendo que si se cumple la condicion de qie center_y es mayor que y_max-restarle la altua
        #entonces center_y llegue hasta el valor que de ymax - alt


#vamos a limitar la raqueta