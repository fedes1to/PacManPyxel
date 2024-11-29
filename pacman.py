import pyxel

from laberinto import Laberinto
from singleton import Singleton

P_HEIGHT = 8 # Altura del pacman
P_WIDTH = 8 # Anchura del pacman

class Pacman(Singleton):

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = [0, 0]
        self.is_empowered = False
        self.score = 0
        self.laberinto = Laberinto._instance # Como es un singleton, no se necesita instanciarlo
    
    def process_movement(self):
        direction_x = int(self.direction[0])
        direction_y = int(self.direction[1])

        tile_size = self.laberinto.tile_size # optimización ligera para no tener que acceder continuamente a la clase
        tile = self.laberinto.get_tile_at_position((self.x // tile_size) + direction_x, (self.y // tile_size) + direction_y)

        match (tile):
            case 1:
                self.score += 10
                self.laberinto.empty_tile_at_position((self.x // tile_size) + direction_x, (self.y // tile_size) + direction_y)
            case 2:
                self.is_empowered = True
                self.score += 50
                self.laberinto.empty_tile_at_position((self.x // tile_size) + direction_x, (self.y // tile_size) + direction_y)
            case 4:
                self.direction = [0, 0]
            case 5:
                self.direction = [0, 0]
    
    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.direction = [-1, 0]
        elif pyxel.btn(pyxel.KEY_D):
            self.direction = [1, 0]
        elif pyxel.btn(pyxel.KEY_W):
            self.direction = [0, -1]
        elif pyxel.btn(pyxel.KEY_S):
            self.direction = [0, 1]

        self.process_movement()

        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
    
    def draw(self):
        pyxel.rect(self.x - (P_HEIGHT / 2), self.y - (P_WIDTH / 2), P_HEIGHT, P_WIDTH, 9)