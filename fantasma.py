import pyxel

from laberinto import normal_direction
from pacman import teleportation
import random
import time

sprite_x = (0, 16, 32, 48, 64, 80, 96, 112) # Animación de los fantasmas
sprite_y = (64, 80, 96, 112) # por cada tipo de fantasma
sprite_scared_x = (
                    (128, 144), # Animación de los fantasmas asustados (Azules)
                    (160, 176)  # Animación de los fantasmas asustados (Blancos)
                   ) 

class Fantasma:
    def set_fantasma(self):
        # Valores del fantasma para resetear su estado y posición
        # Cambiamos ligeramente la x inicial para cada fantasma
        if self.fantasma_type == 0:
            self.x = 112
        elif self.fantasma_type == 1:
            self.x = 116
        elif self.fantasma_type == 2:
            self.x = 108
        else:
            self.x = 120
        self.y = 112
        self.x_grid = 13
        self.y_grid = 23
        self.input_direction = 2
        self.direction = 2
        self.walking = True
        self.is_scared = False
        self.in_cage = True
        self.is_dying = False

    def __init__(self, laberinto, pacman, fantasma_type): # Necesitamos una referencia al laberinto
        """
        TIPOS DE FANTASMA:
        0 = Blinky
        1 = Pinky
        2 = Inky
        3 = Clyde
        """
        self.fantasma_type = fantasma_type

        # Para dibujar el sprite de asustado
        self.scared_type = 0
        self.set_fantasma()
        self.pacman = pacman
        self.laberinto = laberinto

    # Devuelve una dirección aleatoria
    def get_direction_random(self):
        if (self.in_cage):
            return 1 # Salir de la carcel
        else:
            return random.choice([0, 1, 2, 3])
    
    def is_touching_pacman(self):
        if self.pacman.invulnerability_time > 0: # Protección de spawn
            return False
        return abs(self.x - self.pacman.x) < 8 and abs(self.y - self.pacman.y) < 8

    # Devuelve una direccion hacia Pac-Man
    def get_direction_pacman(self, emboscada=False, scared=None):
        if scared is None:
            scared = self.is_scared
        
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

        best_direction = None
        # Calculamos la dirección que nos acerque mas a Pac-Man
        min_distance = float('inf')

        for direction in possible_directions:
            offset_x, offset_y = normal_direction[direction]
            new_x, new_y = self.x_grid + offset_x, self.y_grid + offset_y

            # Si no hay paredes en la dirección que estamos mirando
            if not self.laberinto.check_walls(direction, self.direction, self.y_grid, self.x_grid, is_ghost=True):
                # Distancia = raiz de sus elementos al cuadrado
                distance = (new_x - target_x) ** 2 + (new_y - target_y) ** 2
                if scared:
                    distance = -distance  # Invertimos la distancia si el fantasma está asustado
                if distance < min_distance:
                    # Si la distancia es menor, actualizamos la dirección
                    min_distance = distance
                    best_direction = direction

        # Si encontramos una dirección válida, la devolvemos
        if best_direction is not None:
            return best_direction

        # Si no hay dirección válida, devolvemos una dirección aleatoria
        return self.get_direction_random()

    def get_direction(self):
        """
        0 = Blinky (Persigue directamente a Pac-Man)
        1 = Pinky (Intenta emboscar a Pac-Man)
        2 = Inky (Cortando / Retirandose)
        3 = Clyde (A veces se acerca a Pac-Man, a veces se aleja)
        """
        if self.fantasma_type == 0:
            return self.get_direction_pacman() # Persigue directamente a Pac-Man
        elif self.fantasma_type == 1:
            return self.get_direction_pacman(emboscada=True) # Intenta emboscar a Pac-Man
        # Hacemos el patron mas errático metiendo movimientos random
        elif self.fantasma_type == 2:
            if random.randint(0, 3): # Hacemos que se retire menos que corte
                return self.get_direction_pacman(emboscada=True) # Cortando
            else:
                return self.get_direction_pacman(scared=True) # Retirandose
        elif self.fantasma_type == 3:
            if random.randint(0, 3): # Hacemos que se retire menos que corte
                return self.get_direction_pacman() # Acerca a Pac-Man
            else:
                return self.get_direction_pacman(scared=True) # Aleja


    def update(self):

        if self.is_dying:
            time.sleep(0.25) # Esperamos un tiempo para que el jugador pueda ver que se lo comió
            self.pacman.score += 200 # 200 puntos por comerse un fantasma
            self.set_fantasma() # Reseteamos al fantasma

        if (self.pacman.powered() and self.is_touching_pacman()):
            self.is_dying = True
            pyxel.play(3, 5) # Sonido de comerse al fantasma
        elif (self.is_touching_pacman() and not self.is_scared):
            self.pacman.is_dying = True
            pyxel.play(3, 8) # Sonido de morir

        if (self.in_cage): # Lo echamos de la carcel primero
            self.in_cage = self.laberinto.check_cage(self.y_grid, self.x_grid)

        self.is_scared = self.pacman.powered_time > 0

        self.input_direction = self.get_direction()

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

            # Movemos al fantasma pero un poco más lento que Pac-Man
            self.x += offset_x
            self.y += offset_y


    def draw_fantasma(self):
        # Mismos valores que pacman
        x = self.x - 2
        y = self.y - 3

        if pyxel.frame_count % 20 == 0: # Cada 20 frames
            # Si el tiempo de power-up es menor a 3 segundos
            if self.pacman.powered_time < 180 and self.pacman.powered_time > 0:
                self.scared_type = not self.scared_type # Cambiamos el tipo de fantasma asustado
                pyxel.play(3, 6) # Sonido cuando al fantasma le queda poco tiempo
            else:
                self.scared_type = 0
            self.scared_animacion = random.randint(0, 1) # Cambiamos la animación de los fantasmas asustados
            self.animacion = random.randint(0, 5) # Cambiamos la animación

        if self.is_dying:
            pyxel.blt(x, y, 0, 131, 81, 13, 13, 0) # Sprite ojos fantasma
        else:
            if self.is_scared:
                pyxel.blt(x, y, 0, sprite_scared_x[self.scared_type][self.scared_animacion] + 3, 65, 13, 13, 0)
            else:
                # Animación de los fantasmas
                pyxel.blt(x, y, 0, sprite_x[self.animacion] + 3, sprite_y[self.fantasma_type] + 1, 13, 13, 0)