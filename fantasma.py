import pyxel

from laberinto import normal_direction
from pacman import teleportation
import random

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
        self.in_cage = True

    def __init__(self, laberinto, pacman): # Necesitamos una referencia al laberinto
        self.set_fantasma()
        self.pacman = pacman
        self.laberinto = laberinto

    # Devuelve una dirección aleatoria
    def get_direction_random(self):
        if (self.in_cage):
            return 1 # Salir de la carcel
        else:
            return random.choice([0, 1, 2, 3])
        
    # Devuelve una direccion hacia Pac-Man
    def get_direction_pacman(self, emboscada=False):
        if self.in_cage:
            return 1  # Salir de la carcel

        pacman_direction = self.pacman.direction
        pacman_x, pacman_y = self.pacman.x_grid, self.pacman.y_grid

        if emboscada:
            # Moverse en frente de Pac-Man
            if pacman_direction == 0:  # Abajo
                target_x, target_y = pacman_x, pacman_y + 2
            elif pacman_direction == 1:  # Arriba
                target_x, target_y = pacman_x, pacman_y - 2
            elif pacman_direction == 2:  # Izquierda
                target_x, target_y = pacman_x - 2, pacman_y
            else:  # Derecha
                target_x, target_y = pacman_x + 2, pacman_y
        else:
            # Nos movemos hacia Pac-Man
            target_x, target_y = pacman_x, pacman_y

        possible_directions = [0, 1, 2, 3]
        random.shuffle(possible_directions)

        best_direction = None
        min_distance = float('inf')

        for direction in possible_directions:
            offset_x, offset_y = normal_direction[direction]
            new_x, new_y = self.x_grid + offset_x, self.y_grid + offset_y

            if not self.laberinto.check_walls(direction, self.direction, self.y_grid, self.x_grid, is_ghost=True):
                distance = (new_x - target_x) ** 2 + (new_y - target_y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    best_direction = direction

        if best_direction is not None:
            return best_direction

        # Si no hay dirección válida, devolvemos la dirección anterior
        return self.direction

    def update(self):
        if (self.in_cage): # Lo echamos de la carcel primero
            self.in_cage = self.laberinto.check_cage(self.y_grid, self.x_grid)

        self.is_scared = self.pacman.powered_time > 0

        self.input_direction = self.get_direction_pacman()

        if self.x % 8 == 0 and self.y % 8 == 0: # Se revisa solo en el centro de la celda
            self.x_grid = self.x // 8 + 2  # +2 = 2 columnas de offset
            self.y_grid = self.y // 8

            # Le dejamos salir de la carcel
            if (self.in_cage):
                direction_result = self.laberinto.check_walls(self.input_direction, self.direction, \
                                                            self.y_grid, self.x_grid, is_ghost=True) 
            else:
                direction_result = self.laberinto.check_walls(self.input_direction, self.direction, \
                                                            self.y_grid, self.x_grid, is_ghost=False) 
            
            # Revisamos colisiones
            if direction_result == 1: # Si no hay colisiones
                self.direction = self.input_direction
                self.walking = True
            elif direction_result == 2: # Si hay colisiones
                self.walking = False

        # Movemos al fantasma
        teleportation(self)
        if self.walking:
            offset_x, offset_y = normal_direction[self.direction]
            self.x += offset_x
            self.y += offset_y


    def draw_fantasma(self):
        # Mismos valores que pacman
        x = self.x - 2
        y = self.y - 3

        pyxel.rect(x, y, 13, 13, 1)