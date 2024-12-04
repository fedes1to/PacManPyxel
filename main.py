import pyxel

# Mapa 1 del juego en una matriz (siempre igual al principio)
grid1 = [  # 0 = vacío, 1 = pared, 2 = punto, 3 = punto grande, 4 = pared atravesable por fantasmas
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 4, 4, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1, 1, 1],
        [1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

# TODO: Mapa 2 y 3

def get_grid(level):
    if level == 0:
        return grid1
    if level == 1:
        return grid2
    if level == 2:
        return grid3

# Diccionario para los offsets de las direcciones (unitario)
normal_direction = {
    0: (0, 1),  # Abajo
    1: (0, -1),  # Arriba
    2: (-1, 0),  # Izquierda
    3: (1, 0)  # Derecha
}


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
        self._level = 0

    def __init__(self):
        self.set_pacman()

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

    def main(self):
        self.pacman_direction()
        self.pacman_mouth()

        if self.x % 8 == 0 and self.y % 8 == 0: # Se revisa solo en el centro de la celda
            self.x_grid = self.x // 8 + 2  # +2 = 2 columnas de offset
            self.y_grid = self.y // 8
            self.pacman_eats()
            self.check_walls()

        self.teleportation()
        self.pacman_movement()
    
    @property
    def score(self):
        return self._score
    
    @property
    def lives(self):
        return self._lives

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

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
                break

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

    def pacman_eats(self): # Si pacman se encuentra con un punto
        if get_grid(self.level)[self.y_grid][self.x_grid] == 2: # Si es un punto pequeño
            get_grid(self.level)[self.y_grid][self.x_grid] = 0
            self._score += 10 # Sumamos 10 puntos
        elif get_grid(self.level)[self.y_grid][self.x_grid] == 3: # Si es un punto grande
            self._score += 50 # Sumamos 50 puntos
            self.powered_time = 600 # 10 segundos de power-up (60FPS)
        get_grid(self.level)[self.y_grid][self.x_grid] = 0

    # Comprueba si hay paredes en la dirección que se quiere mover
    def check_walls(self):
        x_offset, y_offset = normal_direction[self.input_direction]
        x_offset2, y_offset2 = normal_direction[self.direction]

        if get_grid(self.level)[self.y_grid + y_offset][self.x_grid + x_offset] != 1:
            self.direction = self.input_direction
            self.walking = True
        elif get_grid(self.level)[self.y_grid + y_offset2][self.x_grid + x_offset2] == 1:
            self.walking = False

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


class App:
    def __init__(self):
        self.level = 0
        pyxel.init(224, 280, "Pac-Man", 65, pyxel.KEY_ESCAPE, 4)
        pyxel.load("theme.pyxres")
        self.pacman = Pacman()
        self.pacman.level = 0
        pyxel.run(self.update, self.draw)

    # Devuelve False si no hay puntos en el tablero
    def draw_dots(self):
        dot_exists = False
        for column_number in range(2, len(get_grid(self.level)[0])):  # 2 = dos columnas de offset
            for line_number in range(len(get_grid(self.level))):
                if get_grid(self.level)[line_number][column_number] == 2:
                    pyxel.rect(column_number * 8 + 3 - 16, line_number * 8 + 3, 2, 2, 2)  # -16 = dos columnas de offset
                    dot_exists = True
                elif get_grid(self.level)[line_number][column_number] == 3:
                    pyxel.blt(column_number * 8 - 16, line_number * 8, 0, 224, 0, 8, 8, 0)  # -16 = dos columnas de offset
                    dot_exists = True
        return dot_exists

    def change_level(self):
        self.level += 1
        self.pacman.level = self.level

    def update(self):
        self.pacman.main()

    def draw(self):
        pyxel.cls(0)
        if (self.pacman.lives == 0):
            pyxel.text(100, 140, "GAME OVER", 7)
        elif (self.draw_dots()): # Si hay puntos en el tablero
            pyxel.blt(0, 0, 0, 0, 0, 224, 248, 0)
            self.pacman.draw_pacman()
            pyxel.text(2, 250, "Puntaje: " + str(self.pacman.score), 7)
            pyxel.text(2, 260, "Vidas: " + str(self.pacman.lives), 7)
        elif (self.level < 3): # Si no es el último nivel
            self.change_level()
            self.pacman.set_pacman() # Reseteamos a Pac-Man
        else: # Si llega al último nivel
            pyxel.text(100, 140, "HAS GANADO !!!", 7)


App()