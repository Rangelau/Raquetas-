
import pygame as pg

from pong import ALTO, ANCHO
from pong.pantallas import Menu, Partida


class Controlador:
    def __init__(self):

        #en el init agregamos todos los objetos que necesitamos cuando iniciamos la pantalla
        #la pantalla principal y el metronomo lo creamos en esta clase debido a que era algo en comun que debiamos crear en la clase menu y partida.
        #asi que solo se crea una sola vez

       
         #entonces se crea aca y en la funcion se piden los argumentos que lleva esa pantalla en cada clase 
        
        pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        metronomo = pg.time.Clock()  #tiempo que demora en entrar al bucle desde inicializo el metronomo

 
        self.pantallas= [Menu (pantalla_principal,metronomo), Partida(pantalla_principal,metronomo)]
        self.menu = Menu(pantalla_principal, metronomo)
        self.partida = Partida(pantalla_principal, metronomo)
    def jugar(self):

        #este buble se hace con el fin de que se salga del juego cuando pulse la x es decir salida es verdadero
        salida = False  #si la persona no pulso la tecla x para la salida entonces es false
        ix = 0 #(la posicion 0 es menu y la 1 es Partida)
        while not salida:
        #while bool(salida) == False:
            salida = self.pantallas[ix].bucle_ppal()
            ix += 1
            if ix >= len(self.pantallas):
                ix = 0

             
             
            