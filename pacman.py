import pyxel
from laberinto import normal_direction

class Pacman:
    def set_pacman(self):
        # Valores de pacman para resetear su estado y posición
        self.x = 104
        self.y = 184
        self.x_grid = 13
        self.y_grid = 23
        self.input_direction = 2
        self.direction = 2
        self.walking = True
        self.mouth = 2
        self.i_mouth = 0
        self.powered_time = False

    def __init__(self, laberinto): # Necesitamos una referencia al laberinto
        self.set_pacman()
        self.laberinto = laberinto
        self._score = 0
        self._lives = 3

    def draw_pacman(self):
        x = self.x - 2
        y = self.y - 3

        tile_x = {1: 19, 2: 3}
        tile_y = {0: 49, 1: 33, 2: 17, 3: 1}

        if self.mouth == 0:
            pyxel.blt(x, y, 1, 35, 1, 13, 13, 0)
        else:
            pyxel.blt(x, y, 1, tile_x[self.mouth], tile_y[self.direction], 13, 13, 0)

    def update(self):
        self.pacman_direction()
        self.pacman_mouth()

        if self.x % 8 == 0 and self.y % 8 == 0: # Se revisa solo en el centro de la celda
            self.x_grid = self.x // 8 + 2  # +2 = 2 columnas de offset
            self.y_grid = self.y // 8

            score_added = self.laberinto.pacman_eats(self.y_grid, self.x_grid) # Nos comemos el punto
            self.score += score_added # Nos comemos el bloque en el que estamos

            if score_added == 50: # Si nos hemos comido un punto grande
                self.powered_time = 600 # 10 segundos de power-up (60FPS)
            
            direction_result = self.laberinto.check_walls(self.input_direction, self.direction, self.y_grid, self.x_grid) # Revisamos colisiones
            if direction_result == 1: # Si no hay colisiones
                self.direction = self.input_direction
                self.walking = True
            elif direction_result == 2: # Si hay colisiones
                self.walking = False
            

        self.teleportation()
        self.pacman_movement()
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value
    
    @property
    def lives(self):
        return self._lives

    def lose_life(self):
        self._lives -= 1 # Restamos la vida

        # Reseteamos el estado de Pac-Man
        self.set_pacman()

    def pacman_direction(self):
        # Diccionario con las direcciones de pacman
        direction_keys = {
            0: (pyxel.KEY_DOWN, pyxel.KEY_S),
            1: (pyxel.KEY_UP, pyxel.KEY_W),
            2: (pyxel.KEY_LEFT, pyxel.KEY_A),
            3: (pyxel.KEY_RIGHT, pyxel.KEY_D)
        }

        for i, (key1, key2) in direction_keys.items():
            if pyxel.btn(key1) or pyxel.btn(key2):
                self.input_direction = i
                return

    def pacman_mouth(self):
        converter = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 1, 7: 1}

        if self.walking: # Si pacman está andando se hace la animación de la boca
            self.mouth = converter[self.i_mouth]
            self.i_mouth = (self.i_mouth + 1) % 8
        elif self.mouth == 0:
            self.i_mouth = 2
            self.mouth = 1
    
    def powered(self):
        if self.powered_time:
            return True
        return False

    # Si llega al extremo del mapa lo teletransporta al otro extremo
    def teleportation(self): 
        x = {2: 224, 3: -8}
        if self.x <= -8 or self.x >= 224:
            self.x = x[self.direction]

    # Movimiento de pacman
    def pacman_movement(self):
        if self.walking:
            offset_x, offset_y = normal_direction[self.direction]
            self.x += offset_x
            self.y += offset_y
