import pyxel

from laberinto import normal_direction
from pacman import teleportation

class Fantasma:
    def set_fantasma(self):
        # Valores del fantasma para resetear su estado y posición
        self.x = 112
        self.y = 112
        self.x_grid = 13
        self.y_grid = 23
        self.input_direction = 2
        self.direction = 2
        self.walking = True
        self.is_scared = False

    def __init__(self, laberinto, pacman): # Necesitamos una referencia al laberinto
        self.set_fantasma()
        self.pacman = pacman
        self.laberinto = laberinto

    def get_best_direction(self, possible_directions):
        for direction in possible_directions:
                x_offset, y_offset = normal_direction[direction]
                if self.laberinto.grid[self.y_grid + y_offset][self.x_grid + x_offset] != 1:
                    return direction
        else:
            for direction in [0, 1, 2, 3]:
                x_offset, y_offset = normal_direction[direction]
                if self.laberinto.grid[self.y_grid + y_offset][self.x_grid + x_offset] != 1:
                    return direction

    def update(self):
        self.is_scared = self.pacman.powered_time > 0

        if self.x % 8 == 0 and self.y % 8 == 0:
            self.x_grid = self.x // 8 + 2
            self.y_grid = self.y // 8
            
            # CÓDIGO MOVIMIENTO NARANJA !!!
            
        direction_result = self.laberinto.check_walls(self.input_direction, self.direction, self.y_grid, self.x_grid)
        if direction_result == 2:  # No hay colisión
            self.direction = self.input_direction
            self.walking = True
        elif direction_result == 1:  # Hay colisión
            self.walking = False

        # Movemos al fantasma
        teleportation(self)
        if self.walking:
            offset_x, offset_y = normal_direction[self.direction]
            self.x += offset_x
            self.y += offset_y


    def draw_fantasma(self):
        if (self.is_scared):
            pyxel.rect(self.x - 8, self.y - 8, 16, 16, 2)
        else:
            pyxel.rect(self.x - 8, self.y - 8, 16, 16, 7)