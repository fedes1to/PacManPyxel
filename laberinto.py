import pyxel
from singleton import Singleton

class Laberinto(Singleton):

    def reset_grid(self):
        """
        Vacio 	0
        Punto 	1
        Punto grande 	2
        Cereza 	3
        Pared 	4
        Pared de fantasmas 	5
        Melon     6
        Fresa     7
        """
        # Como el mapa es simetríco respecto del eye OY en el centro, solo se necesita la mitad del mapa.
        self.grid_laberinto = [
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], # 0
            [4, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4], # 1
            [4, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 4], # 2
            [4, 2, 4, 0, 0, 4, 1, 4, 0, 0, 0, 4, 1, 4], # 3
            [4, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 4], # 4
            [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 5
            [4, 1, 4, 4, 4, 4, 1, 4, 4, 1, 4, 4, 4, 4], # 6
            [4, 1, 4, 4, 4, 4, 1, 4, 4, 1, 4, 4, 4, 4], # 7
            [4, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4], # 8
            [4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 0, 4], # 9
            [0, 0, 0, 0, 0, 4, 1, 4, 4, 4, 4, 4, 0, 4], # 10
            [0, 0, 0, 0, 0, 4, 1, 4, 4, 0, 0, 0, 0, 0], # 11
            [0, 0, 0, 0, 0, 4, 1, 4, 4, 0, 4, 4, 4, 5], # 12
            [4, 4, 4, 4, 4, 4, 1, 4, 4, 0, 4, 0, 0, 0], # 13
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0], # 14
            [4, 4, 4, 4, 4, 4, 1, 4, 4, 0, 4, 0, 0, 0], # 15
            [0, 0, 0, 0, 0, 4, 1, 4, 4, 0, 4, 4, 4, 4], # 16
            [0, 0, 0, 0, 0, 4, 1, 4, 4, 0, 0, 0, 0, 0], # 17
            [0, 0, 0, 0, 0, 4, 1, 4, 4, 0, 4, 4, 4, 4], # 18
            [4, 4, 4, 4, 4, 4, 1, 4, 4, 0, 4, 4, 4, 4], # 19
            [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4], # 20
            [4, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 4], # 21
            [4, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 4], # 22
            [4, 2, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 0], # 23
            [4, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 4, 4], # 24
            [4, 4, 4, 1, 4, 4, 1, 4, 4, 1, 4, 4, 4, 4], # 25
            [4, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4], # 26
            [4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4], # 27
            [4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4], # 28
            [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 29
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]  # 30
        ]

        self.grid_laberinto = [row + row[::-1] for row in self.grid_laberinto] # Rellenamos las zonas que faltan

    def __init__(self, height, width):
        self.reset_grid()

        self.grid_height = len(self.grid_laberinto) # Altura del laberinto
        self.grid_width = len(self.grid_laberinto[0]) # Anchura del laberinto

        self.height = height
        self.width = width

        self._tile_size = width // self.grid_width / 2
    
    def get_tile_at_position(self, x, y):
        x = int(x // 1)
        y = int(y // 1)
        return self.grid_laberinto[y][x]
    
    def empty_tile_at_position(self, x, y):
        x = int(x // 1)
        y = int(y // 1)
        self.grid_laberinto[y][x] = 0

    @property
    def tile_size(self) -> int:
        return self._tile_size
    
    @tile_size.setter
    def tile_size(self, value: int):
        self._tile_size = value

    def update(self):
        pass

    def draw(self):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                tile = self.grid_laberinto[y][x]
                if tile == 0:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 0)
                elif tile == 1:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 7)
                elif tile == 2:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 8)
                elif tile == 3:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 9)
                elif tile == 4:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 1)
                elif tile == 5:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 2)
                elif tile == 6:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 10)
                elif tile == 7:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 11)