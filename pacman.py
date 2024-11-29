import pyxel

from laberinto import Laberinto
from singleton import Singleton
from vector import Vector

P_HEIGHT = 16 # Altura del pacman
P_WIDTH = 16 # Anchura del pacman

class Pacman(Singleton):

    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

        self.direction = Vector(0, 0)
        self.score = 0
        self.rotation = 0
        self.animation_cycle = 0
        self.boca_cerrada = False
        self._power_time_left = 0
        self._dead = False

        self.laberinto = Laberinto._instance # Como es un singleton, no se necesita instanciarlo
    
    def process_movement(self):
        tile = self.laberinto.get_tile_at_position(self.position)

        match tile:
            case 1:
                self.score += 10
                self.laberinto.empty_tile_at_position(self.position)
            case 2:
                self._power_time_left = 600 # 10 segundos de power-up
                self.score += 50
                self.laberinto.empty_tile_at_position(self.position)

        forward_position = self.position + Vector(self.direction.x, self.direction.y) * self.laberinto.tile_size / 2
        forward_tile = self.laberinto.get_tile_at_position(forward_position)

        match forward_tile:
            case 4:
                self.direction = Vector(0, 0)
            case 5:
                self.direction = Vector(0, 0)
            
    
    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.direction = Vector(-1, 0)
            self.rotation = 180
        elif pyxel.btn(pyxel.KEY_D):
            self.direction = Vector(1, 0)
            self.rotation = 0
        elif pyxel.btn(pyxel.KEY_W):
            self.direction = Vector(0, -1)
            self.rotation = 90
        elif pyxel.btn(pyxel.KEY_S):
            self.direction = Vector(0, 1)
            self.rotation = 270

        self.process_movement()

        self.position += self.direction * self.speed

        if (pyxel.frame_count % 10 == 0): # Sabemos que el juego siempre esta a 60fps por tanto esta animación no se verá cambiada
            self.boca_cerrada = not self.boca_cerrada

        if self._power_time_left > 0:
            self._power_time_left -= 1
    
    @property
    def power_time_left(self) -> int:
        return self._power_time_left
    
    @property
    def dead(self) -> bool:
        return self._dead
    
    @dead.setter
    def dead(self, value: bool):
        self._dead = value
    
    def draw(self):
        x_draw_pos = self.position.x - self.laberinto.tile_size / 2
        y_draw_pos = self.position.y - self.laberinto.tile_size / 2

        if self.boca_cerrada and self.direction != Vector(0, 0):
            pyxel.blt(x_draw_pos, y_draw_pos, 0, 16, 16, P_WIDTH, P_HEIGHT, colkey=0, rotate=self.rotation)
        else:
            pyxel.blt(x_draw_pos, y_draw_pos, 0, 0, 16, P_WIDTH, P_HEIGHT, colkey=0, rotate=self.rotation)