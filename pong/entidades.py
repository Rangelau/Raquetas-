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

    def mover(self, x_max=800, y_max=600):
        self.center_x += self.vx
        self.center_y += self.vy
        
        if self.center_y >= y_max - self.radio or self.center_y < - self.radio : #y_max limitr inferior y 0 limite superior
            self.vy= self.vy * -1 #hace un cambio en la velocidad permanente

            if self.center_x >= x_max:
                self.center_x= x_max //2 #si la condicion anterior se cumple entonces center_x me lo vas a poner en el centro es decir x_max//
                self.center_y= y_max //2

                self.vx *= -1 #hace un cambio de direccion contraria a lo que ha  entrado de las esquinas
                self.vy *= -1
                return "LEFT"

            if self.center_x <0:
                self.center_x= x_max //2 #si la condicion anterior se cumple entonces center_x me lo vas a poner en el centro es decir x_max//
                self.center_y= y_max //2

                self.vx *= -1 #hace un cambio de direccion contraria a lo que ha  entrado de las esquinas
                self.vy *= -1
                return "RIGHT"
    
    def comprobar_choque(self,*raquetas):
        for raqueta_activa in raquetas:
            if  self.derecha>=raqueta_activa.izquierda and \
            self.izquierda<=raqueta_activa.derecha and \
            self.abajo>=raqueta_activa.arriba and\
            self.arriba<= raqueta_activa.abajo:
              self.vx*=-1
           

    #estos atributos como son dinamicos porque cambian con cada fotograma, no los creamos como atributo sino como metodos
    @property
    def izquierda(self) : #creamos un metodo de direccion izquierda para que cuando se invoque la funcion de la cordenada de la bola
        return self.center_x-self.radio
    # PROPETY sirve para convertir el metodo en un atributo a la hora de llamarlo.
    # @propety
    #bola.izquierda = 300 no hay necesidad que se pongan () ya que izquiera lo toma como un atributo
    @property
    def derecha(self):
        return self.center_x+self.radio
    @property
    def arriba(self):
        return self.center_y-self.radio
    @property

    def abajo(self):
        return self.center_y+self.radio
    
    
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
    @property
    def izquierda(self) : #creamos un metodo de direccion izquierda para que cuando se invoque la funcion de la cordenada de la bola
        return self.center_x-self.w//2
 
    @property
    def derecha(self):
        return self.center_x+self.w//2

    @property
    def arriba(self):
        return self.center_y-self.h//2

    @property

    def abajo(self):
        return self.center_y+self.h//2

  
        
    #vamos a limitar la raqueta