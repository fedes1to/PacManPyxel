import random
import pyxel

class Frutas:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self._posicion_frutas = [] # Posiciones de las frutas
        self.fruta1_spawned = False
        self.fruta2_spawned = False

    @property
    def posicion_frutas(self):
        return self._posicion_frutas

    def spawn_fruta(self, is_fruta1): # Añade una fruta al tablero

        if is_fruta1 and not self.fruta1_spawned:
            self.fruta1_spawned = True
        elif not is_fruta1 and not self.fruta2_spawned:
            self.fruta2_spawned = True
        else:
            return # No spawnear más frutas

        pos = self.laberinto.get_random_pos()
        
        if pos:
            y, x = pos
            self._posicion_frutas.append((y, x))
            
            fruit = random.randint(5, 8) # Las frutas van del 5 al 8
            self.laberinto.grid[y][x] = fruit  # Añade la fruta al tablero

    def draw_fruits(self):
        # Dibuja las frutas dependiendo de su tipo
        for y, x in self._posicion_frutas:
            u_coord = 0
            if self.laberinto.grid[y][x] == 5:
                u_coord = 32
            elif self.laberinto.grid[y][x] == 6:
                u_coord = 48
            elif self.laberinto.grid[y][x] == 7:
                u_coord = 64
            elif self.laberinto.grid[y][x] == 8:
                u_coord = 80
            pyxel.blt(x * 8 - 22, y * 8 - 4, 0, u_coord, 48, 16, 16, scale=1, colkey=0)

    def check_colision(self, pacman): # Revisamos colisión con Pac-Man
        if (pacman.y_grid, pacman.x_grid) in self._posicion_frutas:
            self._posicion_frutas.remove((pacman.y_grid, pacman.x_grid))

            # Aumentamos el puntaje dependiendo de la fruta
            if self.laberinto.grid[pacman.y_grid][pacman.x_grid] == 5:
                pacman.score += 250
            elif self.laberinto.grid[pacman.y_grid][pacman.x_grid] == 6:
                pacman.score += 300
            elif self.laberinto.grid[pacman.y_grid][pacman.x_grid] == 7:
                pacman.score += 350
            elif self.laberinto.grid[pacman.y_grid][pacman.x_grid] == 8:
                pacman.score += 400

            self.laberinto.grid[pacman.y_grid][pacman.x_grid] = 0 # Eliminamos la fruta del tablero
            pyxel.play(3, 5) # Sonido de comerse a la fruta

            return True
        return False

    def reset_frutas(self):
        self._posicion_frutas = []
        self.fruta1_spawned = False
        self.fruta2_spawned = False