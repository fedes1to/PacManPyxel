import pyxel
import time
from laberinto import normal_direction

# Si llega al extremo del mapa lo teletransporta al otro extremo
def teleportation(player): 
    x = {2: 224, 3: -8}
    if player.x <= -8 or player.x >= 224:
        player.x = x[player.direction]

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
        self._powered_time = False
        self.is_dying = False
        self._invulnerability_time = 180 # 180 / 60FPS = 3 segundos

    def __init__(self, laberinto): # Necesitamos una referencia al laberinto
        self.set_pacman()
        self.laberinto = laberinto
        self._score = 0
        self._lives = 3

    @property
    def invulnerability_time(self):
        return self._invulnerability_time

    @property
    def powered_time(self):
        return self._powered_time
    
    @powered_time.setter
    def powered_time(self, value):
        self._powered_time = value

    def draw_pacman(self):
        x = self.x - 2
        y = self.y - 3

        tile_x = {1: 19, 2: 3}
        tile_y = {0: 49, 1: 33, 2: 17, 3: 1}

        if self.is_dying:
            pyxel.blt(x, y, 0, 208, 0, 13, 13, 0)
            self._lives -= 1 # Restamos la vida
        elif self.mouth == 0:
            pyxel.blt(x, y, 0, 35, 1, 13, 13, 0)
        else:
            pyxel.blt(x, y, 0, tile_x[self.mouth], tile_y[self.direction], 13, 13, 0)

    def update(self):
        self.pacman_direction()
        self.pacman_mouth()

        if self.is_dying:
            time.sleep(1) # Esperamos un segundo para que el jugador murió
            self.set_pacman() # Reseteamos el estado de Pac-Man

        if self.powered_time:
            self.powered_time -= 1

        if self.invulnerability_time:
            self._invulnerability_time -= 1

        if self.x % 8 == 0 and self.y % 8 == 0: # Se revisa solo en el centro de la celda
            self.x_grid = self.x // 8 + 2  # +2 = 2 columnas de offset
            self.y_grid = self.y // 8

            score_added = self.laberinto.pacman_eats(self.y_grid, self.x_grid) # Nos comemos el punto
            self.score += score_added # Nos comemos el bloque en el que estamos

            if score_added == 50: # Si nos hemos comido un punto grande
                self.powered_time = 420 # 7 segundos de power-up (60FPS)
            
            direction_result = self.laberinto.check_walls(self.input_direction, self.direction, \
                                                          self.y_grid, self.x_grid, is_ghost=False) 
            # Revisamos colisiones
            if direction_result == 1: # Si no hay colisiones
                self.direction = self.input_direction
                self.walking = True
            elif direction_result == 2: # Si hay colisiones
                self.walking = False
            

        teleportation(self)
        # Movemos a Pac-Man
        if self.walking:
            offset_x, offset_y = normal_direction[self.direction]
            self.x += offset_x
            self.y += offset_y

            if pyxel.frame_count % 20 == 0:
                pyxel.play(2, 4)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value
    
    @property
    def lives(self):
        return self._lives
    
    @lives.setter
    def lives(self, value):
        self._lives = value

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