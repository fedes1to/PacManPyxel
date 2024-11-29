import pyxel

from pacman import Pacman
from fantasma import Fantasma
from laberinto import Laberinto

W_ANCHURA = 224
W_ALTURA = 288

P_SPEED = 0.5 # Velocidad del pacman

H_OFFSET = 3 # Distancia entre el techo y el laberinto

class App:
    def __init__(self):
        pyxel.init(W_ANCHURA, W_ALTURA, title="PAC-MAN", fps=60, quit_key=pyxel.KEY_Q)

        pyxel.load("assets.pyxres")

        # Inicializamos clases "Singleton" (mirar singleton.py)
        self.laberinto = Laberinto(W_ANCHURA, W_ALTURA, H_OFFSET)
        self.pacman = Pacman((W_ANCHURA / 2) , (W_ALTURA / 2), P_SPEED)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.laberinto.update()
        self.pacman.update()
        
    def draw(self):
        pyxel.cls(0)
        self.laberinto.draw()
        self.pacman.draw()

App()