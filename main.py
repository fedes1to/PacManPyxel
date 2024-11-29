import pyxel

from pacman import Pacman
from fantasma import Fantasma
from laberinto import Laberinto
from vector import Vector

W_ANCHURA = 224
W_ALTURA = 288

P_SPEED = 1 # Velocidad del pacman
F_SPEED = 0.75 # Velocidad de los fantasmas

H_OFFSET = 3 # Distancia en tiles entre el techo y el laberinto

class App:
    def __init__(self):
        self.resolution = Vector(W_ANCHURA, W_ALTURA) * 2
        pyxel.init(self.resolution.x, self.resolution.y, title="PAC-MAN", fps=60, quit_key=pyxel.KEY_Q, display_scale=1)
        pyxel.load("assets.pyxres")
        self.started = False
        pyxel.run(self.update, self.draw)

    def init_game(self):
        # Inicializamos clases "Singleton" (mirar singleton.py)
        self.laberinto = Laberinto(self.resolution, H_OFFSET)
        pacman_spawn = Vector((self.resolution.x / 2), (self.resolution.y / 2) + (self.laberinto.tile_size * (H_OFFSET - 1/2)))
        fantasmas_spawn = self.resolution // 2
        self.pacman = Pacman(pacman_spawn, P_SPEED)
        self.fantasma = Fantasma(fantasmas_spawn, F_SPEED)

    def update(self):
        if (not self.started):
            # if (pyxel.btnp(pyxel.KEY_RETURN)):
                self.init_game()
                self.started = True

        if (self.started):
            self.pacman.update()
            self.fantasma.update()
        
    def draw(self):
        pyxel.cls(0)
        if (self.started):
            self.laberinto.draw()
            self.pacman.draw()
            self.fantasma.draw()

App()