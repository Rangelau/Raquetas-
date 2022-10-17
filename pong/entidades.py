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

    #creeamos un diccionario de imagen para poder interar y decirle que imagen quiere un tomar izq o der

    file_imagenes= {
        "izquierda":["electric00_izq.png","electric01_izq.png","electric0_izq.png"],
        "derecha":["electric00_der.png","electric01_der.png", "electric02_der.png"],
    }
    def __init__(self,center_x,center_y,w=120,h=20,color=(255,255,0)):

        self.center_x=center_x
        self.center_y=center_y
        self.color= color
        self.w=w
        self.h=h

        self.vx=0
        self.vy=0

        #este se hace para cargar las 6 imagenes y self. imagenes va a ser el resultado de la funcion cargar imagenes
        #se ponen los __ para identificar que son metodos internos que aunque permitan llamarse son especificos de la clase
        self.imagenes= self.__cargar_imagenes()
        
        #hay que decirle a la raqueta en que direccion está
        self.direccion="izquierda"  
        #estamos diciendo que tome la posicion 0 de las imagenes que cargamos
        self.imagen_activa=0
        #cada 5 fotogramas va a cambiar la imagen de file imagen segun la posicion en este caso izqui
        self.cambio_cada_x_fotogramas=5
        #para saber cada cuanto fotogramas cambiamos la imagen

        

        """
        #self.imagen es una surfase una calcomania (podemos leerlo en la libreria pygame)
        #el metodo load se va a la ruta que le damos y crea la surfase
        # primero hacemos esto
        #self._imagen=pg.image.load(f"images/{self.imagenes['izquierda']}")
        """
    def __cargar_imagenes(self):
        imagenes={}
        #primer for recorre el lado( "izq o der")
        for lado in self.file_imagenes:
            imagenes [lado]=[] #se ponen estos[] porque son los que representan la imagen
            #segundo for recorre la segunda parte que esta despues del lado osea la imagen
            #si el nombre del fichero esta en el diccionario self imagen, entonces la foto me la vas a cargar con la siguiente ruta
            #en la primera interaccion nombre fichero equivale a electrico00_izq y lo transformo en una foto
            for nombre_fichero in self.file_imagenes[lado]:
                foto = pg.image.load(f"images/{nombre_fichero}")
                imagenes[lado].append(foto)    
                # imagen es el diccionario, la clave lado viene siendo(izq)y le vamos a agregar la foto
            return imagenes
    """ 
    YA NO VAMOS A USAR EL PROPERTY PORQUE VAMOS A CREAR UNA FUNCION QUE PERMITA CARGAR TODAS LAS IMAGENES  
    #luego que la cargamos creamos la funcion para cuando se invoque nos devuelva la imagen
    #el property convierte la funcion en un decorador, cuando la vayamos a usar no hay que hacer def imagen sino tomamos imagen
    @property
    def imagen (self):
        return self._imagen
        
    #ahora vamos a hacer un setter que nos va a permitir grabarle un valor a la funcion imagen ya que no queremos el que nos arroja por defecto la funcion

    @imagen.setter
    def imagen(self,valor):
        self._imagen=pg.image.load(f"images/{self.imagenes[valor]}")
    
    """
    def dibujar (self,pantalla):
        """
        pg.draw.rect(pantalla,self.color,(self.center_x-self.w //2,self.center_y-self.h//2, self.w,self.h))
        #aqui ya no queremos que nos pinte un rectangulo de la raqueta sino que nos pinte en el lienzo la imagen que cargamos

        #pantalla.blit(self._imagen,(self.center_x-self.w //2,self.center_y-self.h//2))

        Vamos decirle ahora que nos pinte las imagenes segun la imagenes, la direecion que le demos y la posicion de la imagen activa
        
        CON LA IMAGEN ACTIVA PRETENDEMOS QUE EN UN FOTOGRAMA ESTE LA FOTO NUMERO 1 EN EL OTRO FOTOGRAMA LA 2 Y DESPUES LA NUMERO 3 PARA QUE VAYA CAMBIANDO LA FOTO Y SE VEA ANIMADA
        """
        pantalla.blit(self.imagenes[self.direccion][self.imagen_activa],(self.center_x-self.w //2,self.center_y-self.h//2))
        
        self.cuenta_fotogramas +=1
        #para animarlo le suma una cada vez despues que lo dibuja, Para cuando la imagen activa sea mayor a longitud de izquierda (electric,00,electric001,electic002), vuelva a iniciar el conteo
        self.imagen_activa +=1
        if self.imagen_activa >= len(self.imagenes,[self.direccion]):
            self.imagen_activa=0
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