import pyxel
from laberinto import Laberinto
from pacman import Pacman
from vector import Vector

DIMENSION_PACMAN = Vector(16, 16) # Dimensiones del pacman

class Fantasma:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

        self.direction = Vector(0, 0)
        self.rotation = 0
        self.animation_cycle = 0

        self.laberinto = Laberinto._instance # Como es un singleton, no se necesita instanciarlo
        self.pacman = Pacman._instance # Como es un singleton, no se necesita instanciarlo

    def update(self):
        if self.position == self.pacman.position: # Si el fantasma y el pacman estan en la misma posicion
            if (not self.pacman.dead):
                self.pacman.score = 0 # El pacman pierde
                self.pacman.dead = True
        else: # Si no, se mueve hacia el pacman
            possible_directions = [Vector(0, -1), Vector(0, 1), Vector(-1, 0), Vector(1, 0)] # Arriba, abajo, izquierda, derecha
            distances = []
            for direction in possible_directions:
                pos = self.position + direction * self.laberinto.tile_size
                if self.laberinto.get_tile_at_position(pos) == 4:
                    possible_directions.remove(direction)
                else:
                    distances.append(pos.distance_to(self.pacman.position))
            
            if len(distances) > 0:
                self.direction = possible_directions[distances.index(min(distances))]
            else:
                self.direction = Vector(0, 0)

        self.position += self.direction * self.speed
    
    def draw(self):
        print(self.position)
        x_draw_pos = self.position.x - (self.laberinto.tile_size / 2)
        y_draw_pos = self.position.y - (self.laberinto.tile_size / 2)

        pyxel.blt(x_draw_pos, y_draw_pos, 0, 0, 32, DIMENSION_PACMAN.x, DIMENSION_PACMAN.y, colkey=0, rotate=self.rotation)