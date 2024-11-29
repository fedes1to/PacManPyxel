import pyxel
from singleton import Singleton
from vector import Vector

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

    def __init__(self, dimensions, offset):
        self.reset_grid()

        self.grid_dimensions = Vector(len(self.grid_laberinto[0]), len(self.grid_laberinto)) # Dimensiones del laberinto
        self.dimensions = dimensions # Dimensiones de la pantalla
        self.offset = offset # distancia entre el techo y el laberinto
        self._tile_size = dimensions.x // self.grid_dimensions.x
    
    def get_tile_at_position(self, pos):
        tile_pos = pos // self.tile_size
        return self.grid_laberinto[tile_pos.y - self.offset][tile_pos.x]
    
    def empty_tile_at_position(self, pos):
        tile_pos = pos // self.tile_size
        self.grid_laberinto[tile_pos.y - self.offset][tile_pos.x] = 0
    
    def get_position_at_tile(self, pos):
        tile_pos = pos // self.tile_size
        return (tile_pos.x * 3/2 * self.tile_size, tile_pos.y * 3/2 * self.tile_size)

    @property
    def tile_size(self) -> int:
        return self._tile_size

    def draw(self):
        offset_in_pixels = self.tile_size * self.offset

        for y in range(self.grid_dimensions.y):
            for x in range(self.grid_dimensions.x):
                tile = self.grid_laberinto[y][x]
                x_pos = x * self.tile_size
                y_pos = y * self.tile_size + offset_in_pixels

                match (tile):
                    case 0: # Vacio
                        pyxel.rect(x_pos, y_pos, self.tile_size, self.tile_size, 0)
                    case 1: # Punto
                        scale_factor = 0.25
                        pyxel.rect(x_pos + (3 * self.tile_size * scale_factor / 2), y_pos + (3 * self.tile_size * scale_factor / 2), \
                            self.tile_size * scale_factor, self.tile_size * scale_factor, 7)
                    case 2: # Punto grande
                        scale_factor = 0.75
                        pyxel.rect(x_pos + (self.tile_size * scale_factor / 2), y_pos + (self.tile_size * scale_factor / 2), \
                            self.tile_size * scale_factor, self.tile_size * scale_factor, 8)
                    case 3: # Cereza
                        pyxel.rect(x_pos, y_pos, self.tile_size, self.tile_size, 9)
                    case 4: # Pared
                        scale_factor = 0.5
                        pyxel.rect(x_pos + (self.tile_size * scale_factor / 2), y_pos + (self.tile_size * scale_factor / 2), \
                            self.tile_size * scale_factor, self.tile_size * scale_factor, 1)
                    case 5: # Pared de fantasmas
                        scale_factor = 0.5
                        pyxel.rect(x_pos + (self.tile_size * scale_factor / 2), y_pos + (self.tile_size * scale_factor / 2), \
                            self.tile_size * scale_factor, self.tile_size * scale_factor, 2)
                    case 6: # Melon
                        pyxel.rect(x_pos, y_pos, self.tile_size, self.tile_size, 10)
                    case 7: # Fresa
                        pyxel.rect(x_pos, y_pos, self.tile_size, self.tile_size, 11)