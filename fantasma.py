import pyxel
from laberinto import Laberinto
from pacman import Pacman
from vector import Vector

DIMENSION_PACMAN = Vector(16, 16)  # Dimensiones del pacman

class Fantasma:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed
        self.direction = Vector(0, 0)
        self.animation_cycle = 0

        # Referencia a laberinto y pacman
        self.laberinto = Laberinto._instance
        self.pacman = Pacman._instance

    def update(self):
        pacman_pos = self.pacman.position
        direction_vector = pacman_pos - self.position

        if direction_vector.magnitude() > 0:
            direction_vector = direction_vector.normalized()

        self.position += direction_vector * self.speed

        if self.laberinto.get_tile_at_position(position) == 4:
            self.position -= direction_vector * self.speed

    def draw(self):
        x_draw_pos = self.position.x - (self.laberinto.tile_size / 2)
        y_draw_pos = self.position.y - (self.laberinto.tile_size / 2)

        pyxel.blt(x_draw_pos, y_draw_pos, 0, 0, 32, DIMENSION_PACMAN.x, DIMENSION_PACMAN.y, colkey=0)