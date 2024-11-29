import pyxel

from pacman import Pacman
from fantasma import Fantasma
from laberinto import Laberinto

W_ANCHURA = 224
W_ALTURA = 288

class App:
    def __init__(self):
        pyxel.init(W_ALTURA, W_ANCHURA, title="PAC-MAN", fps=60, quit_key=pyxel.KEY_Q)

        pyxel.load("assets.pyxres")

        # Inicializamos clases "Singleton" (mirar singleton.py)
        self.laberinto = Laberinto(W_ANCHURA, W_ALTURA)
        self.pacman = Pacman((W_ALTURA / 2) - (self.laberinto.tile_size * 4), (W_ANCHURA / 2) - (self.laberinto.tile_size - 4), 0.5)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.laberinto.update()
        self.pacman.update()
        
    def draw(self):
        pyxel.cls(0)
        self.laberinto.draw()
        self.pacman.draw()

App()